---
title: Streaming Minidrivers
author: windows-driver-content
description: Streaming Minidrivers
ms.assetid: 9f669a1a-50fd-482f-a5af-28e5685dc68c
keywords:
- Windows 2000 Kernel Streaming Model WDK , streaming minidrivers
- Streaming Model WDK Windows 2000 Kernel , streaming minidrivers
- Kernel Streaming Model WDK , streaming minidrivers
- Stream.sys class driver WDK Windows 2000 Kernel
- streaming minidrivers WDK Windows 2000 Kernel
- minidrivers WDK Windows 2000 Kernel Streaming
- Stream.sys class driver WDK Windows 2000 Kernel ,
- streaming minidrivers WDK Windows 2000 Kernel ,
- minidrivers WDK Windows 2000 Kernel Streaming ,
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Streaming Minidrivers


## <a href="" id="ddk-streaming-minidrivers-ksg"></a>


**Note**   This section details the outdated *Stream.sys* class driver. With the release of Microsoft Windows XP, Microsoft supports *Stream.sys* only for existing drivers. As of this release, Microsoft recommends that vendors consider developing new video or audio/video multimedia drivers using the AVStream class driver model. See details in the [AVStream Overview](avstream-overview.md). If developing an audio-only driver, you should write an audio miniport driver under the Microsoft-provided *Portcls.sys* class driver. For details, see [Audio Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff536206).

 

Vendors can support video-only or audio/video devices by providing a minidriver that runs under the Microsoft-provided *Stream.sys* class driver. In this documentation, vendor-provided minidrivers under *Stream.sys* are referred to as *streaming minidrivers*.

For instance, video capture devices and DVD players can be supported with streaming minidrivers. For technology-specific information, see [Video Capture Devices](video-capture-devices.md) and [DVD Decoder Minidrivers](dvd-decoder-minidrivers2.md).

Streaming minidrivers support kernel streaming semantics. To use this document, driver developers should be familiar with basic kernel streaming concepts, as explained in [Kernel Streaming](kernel-streaming.md).

The stream class driver is designed to make writing hardware drivers for streaming devices simpler by handling many of the aspects of interacting with the operating system.

-   The minidriver can allow the stream class driver to handle synchronization on its behalf. For example, the stream class driver can optionally serialize I/O requests for the minidriver. Allowing the class driver to handle synchronization makes the minidriver multiprocessor-safe but nonreentrant. This is suitable for low-end to medium-end hardware.

-   The class driver automatically synchronizes file operations. For example, the opening of a stream and a device are correctly serialized without the minidriver using mutexes, semaphores, or events.

-   The class driver abstracts the implementation of kernel streaming semantics from the minidriver.

-   The class driver handles all interaction with the PnP manager. For example:
    -   The class driver creates the functional device object on the minidriver's behalf.
    -   The class driver manages resource configuration (such as translating port addresses, translating and mapping memory ranges, and connecting interrupts).
    -   The class driver handles PnP IRPs, such as [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749), or [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755).
-   All low-level buffer management is handled by the class driver:
    -   Allocating DMA adapter object, if necessary.
    -   Mapping buffers and building scatter/gather lists for DMA.
    -   Locking and flushing buffers correctly for both DMA and PIO.
-   All IOCTL parameter validation is performed by the class driver.

-   All requests are timed by the class driver with a watchdog timer.

-   The minidriver does not create a device object, but shares the class driver's device object as necessary. This saves system resources.

-   Only one device object is created per adapter. Multiple subdevices (called *streams*) supported by the adapter are represented by kernel streaming pins.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Streaming%20Minidrivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


