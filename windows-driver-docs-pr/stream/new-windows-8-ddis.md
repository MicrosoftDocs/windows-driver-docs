---
title: New AVStream Interfaces for Windows 8
ms.assetid: B3C223BD-2A00-4B87-9D0E-557C0CA3F2DE
description: Provides information about AVStream streaming media driver interfaces that are new or updated for Windows 8.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New AVStream Interfaces for Windows 8


These AVStream streaming media driver interfaces are new or updated for Windows 8:

## Extended camera control interface


This extension of an existing interface is used to control camera features during image capture. See [Extended Camera Control Properties](extended-camera-control-properties.md).

## USB Video Class 1.5 driver update (H.264 video codec)


A new version 1.5 of the USB Video Class driver is supported starting with Windows 8. This driver update incorporates the H.264 video codec standard and is described in these topics:

-   [USB Video Class Driver Overview](usb-video-class-driver-overview.md)
-   [USB H.264 Video Cameras Support](usb-h-264-video-cameras-support.md)
-   [**KS\_DATAFORMAT\_H264VIDEOINFO**](https://msdn.microsoft.com/library/windows/hardware/hh463996)
-   [**KS\_DATARANGE\_H264\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/hh464002)
-   [**KS\_H264VIDEOINFO**](https://msdn.microsoft.com/library/windows/hardware/hh464008)

In addition, a new constant value has been added to the [**KS\_VideoControlFlags**](https://msdn.microsoft.com/library/windows/hardware/ff567696) enumeration.

## Image data format structures


These structures are used with JPEG image capture and encoding to specify image data on a pin (or stream).

-   [**KS\_DATAFORMAT\_IMAGEINFO**](https://msdn.microsoft.com/library/windows/hardware/jj151598)
-   [**KS\_DATARANGE\_IMAGE**](https://msdn.microsoft.com/library/windows/hardware/jj151599)

## Device removal and preemption


This new interface is used when a camera device has been removed from the system (lost) or has been preempted by a new UWP app.

-   [**KSEVENTSETID\_Device**](https://msdn.microsoft.com/library/windows/hardware/jj156036)
-   [**KSEVENT\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/jj151588)
-   [**KSEVENT\_DEVICE\_LOST**](https://msdn.microsoft.com/library/windows/hardware/jj156039)
-   [**KSEVENT\_DEVICE\_PREEMPTED**](https://msdn.microsoft.com/library/windows/hardware/jj156040)

 

 




