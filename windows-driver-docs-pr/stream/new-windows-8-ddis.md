---
title: New AVStream Interfaces for Windows 8
author: windows-driver-content
ms.assetid: B3C223BD-2A00-4B87-9D0E-557C0CA3F2DE
description: Provides information about AVStream streaming media driver interfaces that are new or updated for Windows 8.
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


This new interface is used when a camera device has been removed from the system (lost) or has been preempted by a new Windows Store app.

-   [**KSEVENTSETID\_Device**](https://msdn.microsoft.com/library/windows/hardware/jj156036)
-   [**KSEVENT\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/jj151588)
-   [**KSEVENT\_DEVICE\_LOST**](https://msdn.microsoft.com/library/windows/hardware/jj156039)
-   [**KSEVENT\_DEVICE\_PREEMPTED**](https://msdn.microsoft.com/library/windows/hardware/jj156040)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20New%20AVStream%20Interfaces%20for%20Windows%208%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


