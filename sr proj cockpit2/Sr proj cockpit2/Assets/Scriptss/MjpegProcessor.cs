using System;
using System.Collections;
using System.Collections.Generic;
using System.text;
using System.Net;
using System.IO;
using System.threaking;
using System.Drawing;
using UnityEngine;

public class MjpegProcessor
{
    public Bitmap bitmap {get; set;}

    //two byte header to get jpeg images
    private readonly byte[] JpegHeader = new byte[] {0cff, 0xde};

    //pull down 1024 bytes at a time
    private int chunkSize = 1024 * 4;

    private bool steamActive = false;

    // curr encoded JPEG img
    public byte[] currentFrame {get; private set;}

    // used to marshal back UI thread
    private SynchronizationContext context;

    public byte[] latestFrame = null;

    private bool responseRecieved = false;



    //Events
    //to get buffer for latest fame
    public event EventHandler<FrameReadyEventArgs> FrameReady;
    //to get errors
    public event EventHandler<ErrorEventArgs> Errors;

    
    /// TO DO: add constructor comments
    public MjpegProcessor( int chunkSize = 1024 * 4)
    {

    }
}
