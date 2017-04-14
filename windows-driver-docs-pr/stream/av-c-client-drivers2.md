---
title: AV/C Client Drivers
author: windows-driver-content
description: AV/C Client Drivers
ms.assetid: 70d98c31-2da6-455b-91d8-59bed306b574
keywords: ["AVStream WDK , AV/C", "AV/C WDK"]
---

# AV/C Client Drivers


## <a href="" id="ddk-av-c-client-drivers-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Client%20Drivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


