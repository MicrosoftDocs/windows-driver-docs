---
title: Video Capture Devices
author: windows-driver-content
description: Video Capture Devices
ms.assetid: ed02e6c8-fd82-488b-a0dc-8e83a842bcc4
keywords:
- capturing video WDK AVStream
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Capture Devices


This section describes how to create video capture minidrivers, which follow the Windows Driver Model (WDM) architecture. It assumes familiarity with concepts discussed in [Kernel Streaming](kernel-streaming.md). For information on creating a minidriver for audio-only devices, the [Audio devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff536191).

With the integration of DVD, MPEG decoders, video decoders and tuners, video port extensions (VPEs), and audio codecs on single adapters, a unified driver model that supports all these devices and handles resource contention simplifies development efforts.

The [AVStream](avstream-minidrivers-design-guide.md) and [Stream class](https://msdn.microsoft.com/library/windows/hardware/ff568275) interfaces both provide a framework that provide support for integrated devices. These interfaces support data transfer between kernel-mode drivers. These data transfers do not require a thread to transition to user mode, thereby avoiding a performance hit.

Both interfaces support a uniform streaming model for standard and custom data types. Microsoft defines property sets for most standard devices. Vendors can provide additional property sets if needed.

Microsoft recommends that all new video capture drivers use the AVStream interface. Microsoft provides the Stream class interface for backward compatibility. However, the Stream class interface is obsolete, and Microsoft has discontinued its further development.

**Note**  : This section does not describe the obsolete Video for Windows (VfW) technology. VfW was optimized for capturing movies to disk. Features important to video conferencing, TV viewing, capture of video fields, and ancillary data streams are missing from the VfW architecture. To circumvent these limitations, vendors have added proprietary extensions to VfW. However, without standardized interfaces, applications that use these features must include hardware-dependent code.
To bridge the VfW and WDM driver models, Microsoft provides a VfW-to-WDM mapper as part of the operating system. This component enables WDM drivers to appear as VfW drivers for legacy VfW applications.

 

This section includes:

[Video Capture Overview](video-capture-overview.md)

[Implementing Video Capture Support](implementing-video-capture-support.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Devices%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


