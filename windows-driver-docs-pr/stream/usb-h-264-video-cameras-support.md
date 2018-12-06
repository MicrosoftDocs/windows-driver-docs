---
title: USB H.264 Video Cameras Support
description: Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported.
ms.assetid: EB73E2B2-B34E-4DC1-807A-4990A54E6E8D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB H.264 Video Cameras Support


Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported. A codec is based on algorithms for encoding and decoding video data that allow for high quality and high resolution video streaming. The following are some of the features supported by the Windows 8 UVC class driver, Usbvideo.sys, out of the box:

-   Discovery of the features supported by an H.264 video camera.
-   Session negotiation for H.264 stream on a video camera.
-   Streaming H.264 payload from a camera.
-   Discovery of the features supported by an H.264 video camera.

The H.264 codec uses an efficient video compression to reduce and remove redundant video data. This allows for digital video files to be efficiently stored and exchanged over the network.

If you choose to use the UVC class driver Usbvideo.sys and not a proprietary driver, you must implement video streaming firmware on your device according to the guidelines described next.

### Firmware Guidelines

The UVC class driver Usbvideo.sys queries the video camera directly to obtain its capabilities and then drives the device, with no proprietary driver required. For information on the current implementation of the guidelines, you must refer to the Microsoft Specification of Video Class Driver for H.264/MPEG-4. Also refer to the [Microsoft Proposed Extensions to the USB Video Class for H.264](http://go.microsoft.com/fwlink/p/?LinkId=233063).

**Note**  The official guidelines will be published in a future standard document to be found at this location: [Universal Serial Bus Device Class Definition for Video Devices Specification](http://go.microsoft.com/fwlink/p/?linkid=516989).

 

## Related topics
[**KS\_DATAFORMAT\_H264VIDEOINFO**](https://msdn.microsoft.com/library/windows/hardware/hh463996)  
[**KS\_DATARANGE\_H264\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/hh464002)  
[**KS\_H264VIDEOINFO**](https://msdn.microsoft.com/library/windows/hardware/hh464008)  



