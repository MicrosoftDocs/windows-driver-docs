---
title: Video Capture Devices
description: Video Capture Devices
ms.assetid: ed02e6c8-fd82-488b-a0dc-8e83a842bcc4
keywords:
- capturing video WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




