---
title: New AVStream Interfaces for Windows 8
description: Provides information about AVStream streaming media driver interfaces that are new or updated for Windows 8.
ms.date: 04/20/2017
---

# New AVStream Interfaces for Windows 8


These AVStream streaming media driver interfaces are new or updated for Windows 8:

## Extended camera control interface


This extension of an existing interface is used to control camera features during image capture. See [Extended Camera Control Properties](extended-camera-control-properties.md).

## USB Video Class 1.5 driver update (H.264 video codec)


A new version 1.5 of the USB Video Class driver is supported starting with Windows 8. This driver update incorporates the H.264 video codec standard and is described in these topics:

-   [USB Video Class Driver Overview](usb-video-class-driver-overview.md)
-   [USB H.264 Video Cameras Support](usb-h-264-video-cameras-support.md)
-   [**KS\_DATAFORMAT\_H264VIDEOINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_dataformat_h264videoinfo)
-   [**KS\_DATARANGE\_H264\_VIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_h264_video)
-   [**KS\_H264VIDEOINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_h264videoinfo)

In addition, a new constant value has been added to the [**KS\_VideoControlFlags**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ks_videocontrolflags) enumeration.

## Image data format structures


These structures are used with JPEG image capture and encoding to specify image data on a pin (or stream).

-   [**KS\_DATAFORMAT\_IMAGEINFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_dataformat_imageinfo)
-   [**KS\_DATARANGE\_IMAGE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_image)

## Device removal and preemption


This new interface is used when a camera device has been removed from the system (lost) or has been preempted by a new UWP app.

-   [**KSEVENTSETID\_Device**](./kseventsetid-device.md)
-   [**KSEVENT\_DEVICE**](/windows-hardware/drivers/ddi/ks/ne-ks-ksevent_device)
-   [**KSEVENT\_DEVICE\_LOST**](./ksevent-device-lost.md)
-   [**KSEVENT\_DEVICE\_PREEMPTED**](./ksevent-device-preempted.md)

 

