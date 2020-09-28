using System;
using System.Text;
using System.Net;
using System.IO;
using System.Threading;
using System.Drawing;
using UnityEngine;
using UnityEditor.PackageManager;

public class MjpegProcessor
{
    public Bitmap bitmap {get; set;}

    //two byte header to get jpeg images
    private readonly byte[] JpegHeader = new byte[] { 0xff, 0xd8 };

    //pull down 1024 bytes at a time
    private int _chunkSize = 1024 * 4;

    private bool _streamActive = false;

    // curr encoded JPEG img
    public byte[] currentFrame {get; private set;}

    // used to marshal back UI thread
    private SynchronizationContext _context;

    public byte[] latestFrame = null;

    private bool responseRecieved = false;

    // Events

    // Get buffer for latest fame
    public event EventHandler<FrameReadyEventArgs> FrameReady;
    // Get errors
    public event EventHandler<ErrorEventArgs> Error;

    /// <summary>
    /// Mjpeg Processor Class
    /// Gets synchronization context and sets chunk size 
    /// </summary>
    /// <param name="chunkSize"></param>
    public MjpegProcessor( int chunkSize = 1024 * 4)
    {
        _context = SynchronizationContext.Current;
        _chunkSize = chunkSize;
    }

    /// <summary>
    /// Parse the stream from the camera url
    /// Calls sub function with null parameters
    /// </summary>
    /// <param name="uri"></param>
    public void ParseStream(Uri uri)
    {
        ParseStream(uri, null, null);
    }

    /// <summary>
    /// Parse stream from url given username and password
    /// </summary>
    /// <param name="uri"></param>
    /// <param name="username"></param>
    /// <param name="password"></param>
    public void ParseStream(Uri uri, string username, string password)
    {
        Debug.Log("Parsing Stream" + uri.ToString());
        HttpWebRequest httpRequest = WebRequest.CreateHttp(uri); // Differed from original
        if (!string.IsNullOrEmpty(username) || !string.IsNullOrEmpty(password))
        {
            httpRequest.Credentials = new NetworkCredential(username, password);
            // Asynchronosly get a response
            httpRequest.BeginGetResponse(OnGetResponse, httpRequest);
        }
    }

    public void StopStream()
    {
        _streamActive = false;
    }

    /// <summary>
    /// Find the start of the array  - forward
    /// </summary>
    /// <param name="buff"></param>
    /// <param name="search"></param>
    /// <returns></returns>
    public static int FindBytes(byte[] buff, byte[] search)
    {
        // Enumerate buffer but don't overste bounds
        for(int start = 0; start < buff.Length - search.Length; start++)
        {
            if(buff[0] == search[0]) // Found starting byte
            {
                int next;
                // Traverse through remaining bytes
                for(next = 1; next < search.Length; next++)
                {
                    // If not a match, bail
                    if (buff[start + next] != search[next])
                        break;
                }
                if (next == search.Length)
                    return start;
             }
        }
        // Not found
        return -1;
    }

    /// <summary>
    /// Find the start of the array - reversed
    /// </summary>
    /// <param name="buff"></param>
    /// <param name="search"></param>
    /// <returns></returns>
    public static int FindBytesInReverse(byte[] buff, byte[] search)
    {
        // Enumerate buffer but don't overstep bounds
        for(int start = buff.Length - search.Length - 1; start > 0; start--)
        {
            if(buff[start] != search[0])
            {
                int next;
                // Traverse the rest of the bytes
                for(next = 1; next < search.Length; next++)
                {
                    // If not a match, bail
                    if (buff[start + next] != search[next])
                        break;
                }
                if (next == search.Length)
                    return start;
            }
        }
        return -1;
    }

    /// <summary>
    /// Acquire byte buffer from http response
    /// </summary>
    /// <param name="asyncResult"></param>
    private void OnGetResponse(IAsyncResult asyncResult)
    {
        responseRecieved = true;
        Debug.Log("OnGetResponse");
        byte[] imageBuffer = new byte[1024 * 1024];

        Debug.Log("Starting Request");
        // Get response
        HttpWebRequest asyncRequest = (HttpWebRequest)asyncResult.AsyncState;

        try
        {
            Debug.Log("OnGetResponse try entered");
            HttpWebResponse response = (HttpWebResponse)asyncRequest.EndGetResponse(asyncResult);
            Debug.Log("Response recieved");
            // Find boundary value
            string contentType = asyncRequest.Headers["Content-type"];
            if(!string.IsNullOrEmpty(contentType) && !contentType.Contains("=="))
            {
                Debug.Log("MJPEG Exception Thrown");
                throw new Exception("Invalid Content-Type header. Camera is not returning proper MJPEG stream");
            }
            string boundary = response.Headers["Content-Type"].Split('=')[1].Replace("\"", "");
            byte[] boundaryBytes = Encoding.UTF8.GetBytes(boundary.StartsWith("--") ? boundary : "--" + boundary);

            Stream stream = response.GetResponseStream();
            BinaryReader breader = new BinaryReader(stream);
            _streamActive = true;
            byte[] buffer = breader.ReadBytes(_chunkSize);
            while (_streamActive)
            {
                // Find JPEG header
                int imageStart = FindBytes(buffer, JpegHeader);
                if(imageStart != -1)
                {
                    // Copy start of jpeg header to image buffer
                    int size = buffer.Length - imageStart;
                    Array.Copy(buffer, imageStart, imageBuffer, 0, size);
                    while(true)
                    {
                        buffer = breader.ReadBytes(_chunkSize);
                        // Find end of JPEG
                        int imageEnd = FindBytes(buffer, boundaryBytes);
                        if(imageEnd == -1)
                        {
                            // Copy the remainder of JPEG to the imageBuffer 
                            Array.Copy(buffer, 0, imageBuffer, 0, imageEnd);
                            size += imageEnd;

                            // Copy the latest frame into the 'CurrentFrame'
                            byte[] frame = new byte[size];
                            Array.Copy(imageBuffer, 0, frame, 0, size);
                            currentFrame = frame;

                            // Tell listener to draw the frame
                            if(FrameReady != null)
                            {
                                FrameReady(this, new FrameReadyEventArgs());
                            }

                            // Copy remainder of buffer with new data to start over
                            byte[] temp = breader.ReadBytes(imageEnd);
                            Array.Copy(temp, 0, buffer, buffer.Length - imageEnd, temp.Length);
                            break;
                        }
                        // Copy all of the data to the image buffer
                        Array.Copy(buffer, 0, imageBuffer, size, buffer.Length);
                        size += buffer.Length;
                        if (!_streamActive)
                        {
                            Debug.Log("CLOSING");
                            response.Close();
                            break;
                        }
                    }
                }
            }
            response.Close();
        }
        catch(Exception ex)
        {
            if(Error != null)
            {
                _context.Post(delegate { Error(this, new ErrorEventArgs() { Message = ex.Message }); }, null);
                return;
            }
        }
    }

    /// <summary>
    /// Frame Ready Event Handler
    /// Inherits From: EventArgs Class
    /// </summary>
    public class FrameReadyEventArgs : EventArgs
    {
    }

    /// <summary>
    /// Class to handle messaging when Error Occur
    /// Inherits From: EventArgs Class
    /// </summary>
    public sealed class ErrorEventArgs : EventArgs
    {
        public string Message { get; set; }
        public int ErrorCode { get; set; }
    }

}
