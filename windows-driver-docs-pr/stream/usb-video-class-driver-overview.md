---
title: USB Video Class driver overview
description: Provides information about using the system-supplied USB Video Class (UVC) driver, Usbvideo.sys. 
keywords:
- USB Video Class drivers WDK AVStream , about USB Video Class drivers
- Video Class drivers WDK USB , about USB Video Class drivers
- UVC drivers WDK AVStream , about USB Video Class drivers
- user-mode clients WDK USB Video Class
ms.date: 01/02/2024
---

# USB Video Class driver overview

If you're providing a driver for a webcam or a digital camcorder, consider using the system-supplied USB Video Class (UVC) driver, Usbvideo.sys. The USB Video Class (UVC) driver is a Microsoft-provided AVStream minidriver that provides driver support for USB Video Class devices. When your device uses UVC, you don't need to supply your own driver. Instead, the device works automatically with the system-supplied driver.

In the USB Video Class model, vendors don't write driver. Instead, vendors implement video streaming hardware according to the guidelines in the *Universal Serial Bus Device Class Definition for Video Devices Specification* document located on the [USB Implementers Forum](https://www.usb.org/documents) website. The UVC driver queries the hardware directly to obtain its capabilities and then drives the device, with no proprietary driver required.

You can optionally extend UVC driver functionality to add vendor-specific processing.

The following table shows support for UVC in different versions of Windows:

| UVC Version | Windows 7 | Windows 8 |
|--|--|--|
| USB Video Class 1.5 (H.264 video codec) | Not supported | Supported |
| USB Video Class 1.1 | Supported | Supported |
| USB Video Class 1.0 | Supported | Supported |

Beginning with Windows 8, the H.264 video codec (encoder/decoder) is supported. H.264 is an open standard that allows efficient video compression techniques for reducing the use of network bandwidth and storage space. This approach leads to a higher video quality for a given bit rate. For more information, see [USB H.264 Video Cameras Support](usb-h-264-video-cameras-support.md). Also refer to [Microsoft Proposed Extensions to the USB Video Class for H.264](/previous-versions/windows/hardware/download/dn550976(v=vs.85)).

The following list shows some advantages to using the Usbvideo.sys driver:

- No CD required for installation

- No driver writing cost

- No maintenance cost

- Opportunity for vendors to add functionality

- Easier debugging with public symbols

- Works with Driver Verifier

- Works with checked OS builds

- Compliant with ACPI power management

- Compliant with Selective Suspend power management

- Supports multimedia APIs in Media Foundation and DirectShow

The system-supplied Usbvideo.sys driver supports the following UVC features in different versions of Windows:

| UVC feature | Windows 7 | Windows 8 |
|--|--|--|
| Single video control interface and one or more video streaming interfaces | Supported | Supported |
| Standard units and terminals, including Extension units | Supported | Supported |
| Still image capture support for all three methods defined in the UVC specification | Supported | Supported |
| Bulk and isochronous devices | Supported | Supported |
| Streaming parameter negotiation using probe commit controls | Supported | Supported |
| Compressed formats: MJPEG, DV | Supported | Supported |
| Uncompressed formats: YUY2, NV12 | Supported | Supported |
| Supports both capture and render devices | Supported | Supported |
| Compressed format: MPEG2TS | Not Supported | Not Supported |
| Stream-based and frame-based formats | Supported | Supported |
| H.264 video codec | Not Supported | Supported |

## Customizing the UVC driver

You can customize your support for UVC by supplying an [Extension Unit plug-in](introduction-to-usb-video-class-extension-units.md). Extension units provide a private control channel between device and vendor-supplied application.

## Other resources

To test your UVC implementation, you can use the following tools:

- GraphEdit

- KsStudio

- USBView

For more information about these tools, see [AVStream Testing and Debugging](avstream-testing-and-debugging.md).

You can find specifications for USB Video Class 1.1 on the [USB Implementers Forum](https://www.usb.org/documents) website.
