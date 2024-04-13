---
title: USB H.264 Video Cameras Support
description: Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported.
ms.date: 06/19/2020
---

# USB H.264 video cameras support

Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported. A codec is based on algorithms for encoding and decoding video data that allow for high quality and high resolution video streaming. The following are some of the features supported by the Windows 8 UVC class driver, Usbvideo.sys, out of the box:

- Discovery of the features supported by an H.264 video camera.

- Session negotiation for H.264 stream on a video camera.

- Streaming H.264 payload from a camera.

- Discovery of the features supported by an H.264 video camera.

The H.264 codec uses an efficient video compression to reduce and remove redundant video data. This allows for digital video files to be efficiently stored and exchanged over the network.

If you choose to use the UVC class driver Usbvideo.sys and not a proprietary driver, you must implement video streaming firmware on your device according to the guidelines described next.

## Firmware Guidelines

The UVC class driver Usbvideo.sys queries the video camera directly to obtain its capabilities and then drives the device, with no proprietary driver required. For information on the current implementation of the guidelines, you must refer to the Microsoft Specification of Video Class Driver for H.264/MPEG-4. Also refer to the [Microsoft Proposed Extensions to the USB Video Class for H.264](/previous-versions/windows/hardware/download/dn550976(v=vs.85)).

> [!NOTE]
> The official guidelines will be published in a future standard document to be found at this location: [Universal Serial Bus Device Class Definition for Video Devices Specification](https://www.usb.org/documents).

## Related topics

[**KS\_DATAFORMAT\_H264VIDEOINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_dataformat_h264videoinfo)  

[**KS\_DATARANGE\_H264\_VIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_h264_video)  

[**KS\_H264VIDEOINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_h264videoinfo)
