using UnityEngine;
using System;
using static MjpegProcessor;

/// <summary>
/// MjpegTexture class : Displays the bytes provided by the Mjpeg processor on a texture.
/// Modified & Updated by: Alexis Koopmann & Jenna Webster
/// Modified from https://github.com/DanielArnett/SampleUnityMjpegViewer for use with Unity 2019 and Oculus Quest.
/// Original Author: Daniel Arnett
/// </summary>
public class MjpegTexture : MonoBehaviour
{
    [Tooltip("Set this to the address of the mjpg stream,")]
    public string streamAddress;

    [Tooltip("Chunk size for stream processor in kilobytes.")]
    public int chunkSize = 4;
    Texture2D tex;
    const int initWidth = 2;
    const int initHeight = 2;
    bool updateFrame = false;
    MjpegProcessor mjpeg;
    float deltaTime = 0.0f;
    float mjpegDeltaTime = 0.0f;

    public void Start()
    {
        mjpeg = new MjpegProcessor(chunkSize * 1024);
        mjpeg.FrameReady += OnMjpegFrameReady;
        Uri mjpegAddress = new Uri(streamAddress);
        mjpeg.ParseStream(mjpegAddress);
        tex = new Texture2D(initWidth, initHeight, TextureFormat.PVRTC_RGBA4, false);
    }

    private void OnMjpegFrameReady(object sender, FrameReadyEventArgs e)
    {
        updateFrame = true;
    }

    void OnMjpegError(object sender, ErrorEventArgs e)
    {
        Debug.Log("Error recieved while reading the MJPEG.");
    }

    void Update()
    {
        deltaTime += Time.deltaTime;

        if (updateFrame)
        {
            tex.LoadImage(mjpeg.CurrentFrame);
            GetComponent<Renderer>().material.mainTexture = tex;
            updateFrame = false;
            mjpegDeltaTime += (deltaTime - mjpegDeltaTime) * 0.2f;
            deltaTime = 0.0f;
        }
    }

    void OnDestroy()
    {
        mjpeg.StopStream();
    }
}