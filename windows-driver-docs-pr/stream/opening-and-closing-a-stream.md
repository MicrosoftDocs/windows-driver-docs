---
title: Opening and Closing a Stream
author: windows-driver-content
description: Opening and Closing a Stream
MS-HAID:
- 'vidcapds\_92e4a8d7-c44e-44db-9c58-e64ee9908e4e.xml'
- 'stream.opening\_and\_closing\_a\_stream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a4895e99-ab2e-482e-b89f-04b01177ec03
keywords: ["video capture WDK AVStream , opening streams", "capturing video WDK AVStream , opening streams", "video capture WDK AVStream , closing streams", "capturing video WDK AVStream , closing streams", "opening streams WDK AVStream", "closing streams WDK AVStream"]
---

# Opening and Closing a Stream


The Stream class interface sends an [**SRB\_OPEN\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff568191) request to a Stream class minidriver to open a stream with the selected video format. Information passed in SRB\_OPEN\_STREAM includes the index of the stream to be open and a pointer to a pointer to a [**KS\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567700) structure. The stream index corresponds to the index of the stream in the array of [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628) structures returned by the minidriver in response to an earlier [**SRB\_GET\_STREAM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568173) request. For more information about handling SRB\_GET\_STREAM\_INFO, see [Stream Categories](stream-categories.md).

The following example code obtains the stream index, kernel streaming data format, and kernel streaming video info header.

```
int StreamNumber = pSrb->StreamObject->StreamNumber;
PKS_DATAFORMAT_VIDEOINFOHEADER  pKSDataFormat = 
    (PKS_DATAFORMAT_VIDEOINFOHEADER) pSrb->CommandData.OpenFormat;
PKS_VIDEOINFOHEADER pVideoInfoHdrRequested = 
    &pKSDataFormat->VideoInfoHeader;
```

Minidrivers should verify that they can support the requested stream format. In particular, the contents of the [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305) structure should be verified, along with cropping and scaling information specified by the **rcSource** and **rcTarget** members.

If the device hardware cannot support the capture frame rate requested in the **AvgTimePerFrame** member of KS\_VIDEOINFOHEADER, it should always select the next *lower* frame rate available. For example, if a camera can support a capture frame rate of 7 frames per second (fps) and 15 fps, and a client application attempts to open the stream at a capture frame rate of 10 fps, the camera should create a 7-fps physical stream.

For a ten-second capture in which all 70 available physical frames are captured, the minidriver should report 100 frames captured, 30 frames of which were dropped by the [**KSPROPERTY\_DROPPEDFRAMES\_CURRENT**](https://msdn.microsoft.com/library/windows/hardware/ff565135) property.

Special rules apply when the output buffer is a DirectDraw surface. In this case, the **biWidth** member of the KS\_BITMAPINFOHEADER structure actually represents the stride of the destination DirectDraw surface, which typically is larger than the video image width. The stride of a surface is usually the width of the surface multiplied by its byte-depth. For example, for a surface that is 640 pixels wide with a color depth of 32 bits-per-pixel, the stride would be 2560 bytes.

To determine the requested image width, use the following code example:

```
if (IsRectEmpty(&pVideoInfoHdrRequested->rcTarget) {
    Width =  pVideoInfoHdrRequested->bmiHeader.biWidth;
    Height = pVideoInfoHdrRequested->bmiHeader.biHeight;
} 
else {
    Width = pVideoInfoHdrRequested->rcTarget.right − 
            pVideoInfoHdrRequested->rcTarget.left;
    Height = pVideoInfoHdrRequested->rcTarget.bottom − 
             pVideoInfoHdrRequested->rcTarget.top;
}
```

The Stream class interface sends an [**SRB\_CLOSE\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff568165) request to the minidriver to close a stream. The minidriver should then return all outstanding stream SRBs to the Stream class interface.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Opening%20and%20Closing%20a%20Stream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


