---
title: USB Video Class Driver Overview
author: windows-driver-content
description: USB Video Class Driver Overview
ms.assetid: 890d448e-bfee-462d-8cce-a2cca42f2f6d
keywords:
- USB Video Class drivers WDK AVStream , about USB Video Class drivers
- Video Class drivers WDK USB , about USB Video Class drivers
- UVC drivers WDK AVStream , about USB Video Class drivers
- user-mode clients WDK USB Video Class
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USB Video Class Driver Overview


If you are providing a driver for a webcam or a digital camcorder, consider using the system-supplied universal serial bus (USB) Video Class driver, Usbvideo.sys. The USB Video Class (UVC) driver is a Microsoft-provided AVStream minidriver that provides driver support for USB Video Class devices. When your device uses UVC, you do not need to supply your own driver. Instead, the device works automatically with the system-supplied driver.

In the USB Video Class model, vendors do not write drivers; instead, vendors implement video streaming hardware according to the guidelines in the [Universal Serial Bus Device Class Definition for Video Devices Specification](http://go.microsoft.com/fwlink/p/?linkid=516989). The UVC driver queries the hardware directly to obtain its capabilities and then drives the device, with no proprietary driver required.

You can optionally extend UVC driver functionality to add vendor-specific processing.

The following table shows support for UVC in different versions of Windows:

| UVC Version                             | Windows Vista/XP | Windows 7     | Windows 8 |
|-----------------------------------------|------------------|---------------|-----------|
| USB Video Class 1.5 (H.264 video codec) | Not supported    | Not supported | Supported |
| USB Video Class 1.1                     | Not supported    | Supported     | Supported |
| USB Video Class 1.0                     | Supported        | Supported     | Supported |

 

Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported. H.264 is an open standard that allows efficient video compression techniques for reducing the use of network bandwith and storage space. This leads to a higher video quality for a given bit rate. For more information, see [USB H.264 Video Cameras Support](usb-h-264-video-cameras-support.md). Also refer to the [Microsoft Proposed Extensions to the USB Video Class for H.264](http://go.microsoft.com/fwlink/p/?LinkId=233063).

The following list shows some advantages to using the Usbvideo.sys driver:

-   No CD required for installation
-   No driver writing cost
-   No maintenance cost
-   Opportunity for vendors to add functionality
-   Easier debugging with public symbols
-   Works with Driver Verifier
-   Works with checked OS builds
-   Compliant with ACPI power management
-   Compliant with Selective Suspend power management
-   Supports multimedia APIs in Media Foundation and DirectShow

The system-supplied Usbvideo.sys driver supports the following UVC features in different versions of Windows:

| UVC feature                                                                        | Windows Vista/XP | Windows 7     | Windows 8     |
|------------------------------------------------------------------------------------|------------------|---------------|---------------|
| Single video control interface and one or more video streaming interfaces          | Supported        | Supported     | Supported     |
| Standard units and terminals, including Extension units                            | Supported        | Supported     | Supported     |
| Still image capture support for all three methods defined in the UVC specification | Supported        | Supported     | Supported     |
| Bulk and isochronous devices                                                       | Supported        | Supported     | Supported     |
| Streaming parameter negotiation using probe commit controls                        | Supported        | Supported     | Supported     |
| Compressed formats: MJPEG, DV                                                      | Supported        | Supported     | Supported     |
| Uncompressed formats: YUY2, NV12                                                   | Supported        | Supported     | Supported     |
| Supports both capture and render devices                                           | Supported        | Supported     | Supported     |
| Compressed format: MPEG2TS                                                         | Not Supported    | Not Supported | Not Supported |
| Stream-based and frame-based formats                                               | Not supported    | Supported     | Supported     |
| H.264 video codec                                                                  | Not Supported    | Not Supported | Supported     |

 

## Customizing the UVC Driver


You can customize your support for UVC by supplying an [Extension Unit plug-in](introduction-to-usb-video-class-extension-units.md). Extension units provide a private control channel between device and vendor-supplied application.

## Additional Resources


To test your UVC implementation, you can use the following tools:

-   GraphEdit
-   KsStudio
-   USBView

For more information about these tools, see [AVStream Testing and Debugging](avstream-testing-and-debugging.md).

You can download a compressed set of specifications for USB Video Class 1.1 from the [Device Class page](http://go.microsoft.com/fwlink/p/?linkid=517016) on the USB Implementers Forum website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USB%20Video%20Class%20Driver%20Overview%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


