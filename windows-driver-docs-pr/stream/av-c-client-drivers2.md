---
title: AV/C Client Drivers
description: AV/C Client Drivers
ms.assetid: 70d98c31-2da6-455b-91d8-59bed306b574
keywords:
- AVStream WDK , AV/C
- AV/C WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Client Drivers





Microsoft provides support for the IEEE Audio/Video Control (AV/C) protocol in Windows XP and later operating systems. The AV/C protocol defines methods for issuing commands to and sending responses from subunits on AV/C-compliant devices. You can control subunits on devices that conform to the AV/C protocol across the IEEE 1394 serial bus if you write a driver to support the subunit hardware. Note that you do not need to write a subunit driver to support tape subunits because Microsoft supplies two other drivers for this functionality, *Msdv.sys* and *Mstape.sys*.

To support the AV/C protocol, Microsoft supplies the following two drivers:

-   *Avc.sys*

-   *Avcstrm.sys*

*Avc.sys* is a function driver that provides support to establish and manage subunit/unit plug connections. *Avcstrm.sys* is a lower-filter driver that adds support to assist with streaming the following specific data formats:

-   Standard definition digital video (SDDV, the 61883-2 specification)

-   MPEG2-TS (the 61883-4 specification)

Depending on the functionality of your device, you can use the optional support provided in *Avcstrm.sys* to assist with streaming SDDV and/or MPEG2-TS data. If *Avcstrm.sys* does not support a format used by your device, then you can use the connection management and data streaming functionality exposed by *61883.sys*, which is located lower in the driver stack.

Subunit drivers should follow the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM) architecture. Subunit drivers can use either the Stream class interface or the AVStream interface. AVStream is the preferred interface for developing a subunit driver. The Stream class interface is obsolete, and Microsoft has discontinued its further development. For more information about these two interfaces, see [AV/C Kernel-Streaming Interface and KS Proxy Plug-ins](av-c-kernel-streaming-interface-and-kernel-streaming-proxy-plug-ins.md).

For more information about how to write an AV/C subunit driver, see [AV/C Overview](av-c-overview.md). For more information about how to use *Avcstrm.sys* to assist streaming data, see [AV/C Streaming Overview](av-c-streaming-overview.md).

AV/C protocol support is built on the IEEE 1394 driver stack and the IEC-61883 standards. For more information about the IEC-61883 driver stack, see [IEC-61883 Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff537188).

 

 




