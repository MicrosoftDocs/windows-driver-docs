---
title: USBCAMD minidriver library
description: USBCAMD minidriver Library
keywords:
- Windows 2000 Kernel Streaming Model WDK , USBCAMD2 minidriver library
- Streaming Model WDK Windows 2000 Kernel , USBCAMD2 minidriver library
- Kernel Streaming Model WDK , USBCAMD2 minidriver library
- USBCAMD2 minidriver library WDK Windows 2000 Kernel Streaming
- USB-based streaming cameras WDK USBCAMD2
- cameras WDK USBCAMD2
ms.date: 06/19/2020
---

# USBCAMD minidriver library

USBCAMD2 is a kernel-mode minidriver library that simplifies driver development for USB-based streaming cameras. The USBCAMD2 minidriver library interfaces with the Stream class (*stream.sys*) and USB bus drivers so that you can focus on implementing support for the camera's properties and image processing.

Microsoft released the original USBCAMD minidriver library with the Microsoft Windows 98 Driver Development Kit (DDK). The original library was updated to USBCAMD2 in the Windows Server 2003, Windows XP, and Windows 2000 DDKs and in the Windows Driver Kit (WDK). USBCAMD2 adds [new features](usbcamd2-features.md) to provide support for still pins, power management (such as hibernation) and extended versions of the original APIs.

In addition to the USBCAMD2 minidriver library, Microsoft also supplies the [USB Video class (UVC) driver](usb-video-class-driver.md) to support USB-based cameras. UVC supports a superset of the features in USBCAMD2. Microsoft recommends using the UVC driver for all new hardware development. If, however, the hardware design cannot be changed to be UVC-compliant, then you must write a USBCAMD2 minidriver.

The minidriver library manages the data stream on the USB bus from the device, which includes handling the start, stop, synchronization, and error recovery issues associated with maintaining the stream on the USB bus. USBCAMD2 calls vendor-implemented callback functions to handle hardware specific operations, such as kernel streaming property support, selecting alternate USB interface settings, and image decompression and processing.

The camera minidriver is responsible for:

- Implementing support for kernel streaming properties, such as [PROPSETID\_VIDCAP\_VIDEOPROCAMP](./propsetid-vidcap-videoprocamp.md) and [PROPSETID\_VIDCAP\_CAMERACONTROL](./propsetid-vidcap-cameracontrol.md).

- Determining whether the data stream is valid and part of the current or next video frame in the camera minidriver's [*CamProcessUSBPacketEx*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-pcam_process_packet_routine_ex) callback function.

- Extracting video frames from the stream and performing processing on video frames before they are returned to the calling application in the camera minidriver's [*CamProcessRawVideoFrameEx*](/windows-hardware/drivers/ddi/usbcamdi/nc-usbcamdi-pcam_process_raw_frame_routine_ex) callback function.

The original USBCAMD minidriver library is supported on Windows 98 as *usbcamd.sys*, but is not supported on Windows 2000. USBCAMD2 is supported on Windows 2000 and later and on Windows Millennium Edition and later as both *usbcamd.sysand usbcamd2.sys*. Neither the original USBCAMD minidriver library nor USBCAMD2 are supported on 64-bit platforms.

For Windows 2000 and later and Windows Millennium Edition and later operating systems, camera vendors should use the USBCAMD2 minidriver library instead of the original library to develop camera minidrivers.

You can use the *usbintel* example camera minidriver as a starting point. This sample is available in the Driver Development Kit (DDK) and Windows Driver Kit (WDK) for Windows XP through Windows 7 (Build 7600). The WDK installs this sample to *src\\wdm\\videocap\\usbintel* (if it was selected as an option to install).

## Additional Resources

Developers should familiarize themselves with the material in [Kernel Streaming](kernel-streaming.md), [Streaming Minidrivers](/windows-hardware/drivers/ddi/_stream/index), and [Video Capture Devices](video-capture-devices.md).

For additional developer information, including the USB specifications, see [USB-IF Developers Area](https://www.usb.org/developers).

For general or consumer information, see [USB Implementers Forum](https://www.usb.org/).
