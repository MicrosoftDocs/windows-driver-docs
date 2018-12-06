---
title: Opening and Closing a Stream
description: Opening and Closing a Stream
ms.assetid: a4895e99-ab2e-482e-b89f-04b01177ec03
keywords:
- video capture WDK AVStream , opening streams
- capturing video WDK AVStream , opening streams
- video capture WDK AVStream , closing streams
- capturing video WDK AVStream , closing streams
- opening streams WDK AVStream
- closing streams WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening and Closing a Stream


The Stream class interface sends an [**SRB\_OPEN\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff568191) request to a Stream class minidriver to open a stream with the selected video format. Information passed in SRB\_OPEN\_STREAM includes the index of the stream to be open and a pointer to a pointer to a [**KS\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567700) structure. The stream index corresponds to the index of the stream in the array of [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628) structures returned by the minidriver in response to an earlier [**SRB\_GET\_STREAM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568173) request. For more information about handling SRB\_GET\_STREAM\_INFO, see [Stream Categories](stream-categories.md).

The following example code obtains the stream index, kernel streaming data format, and kernel streaming video info header.

```cpp
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

```cpp
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

 

 




