---
title: AV/C Overview
author: windows-driver-content
description: AV/C Overview
ms.assetid: ff9e6dfc-7ab4-4b56-8b47-d3ea46b579e0
keywords:
- AV/C WDK , about AV/C
- Avc.sys function driver WDK
- peer Avc.sys mode WDK AV/C
- virtual Avc.sys mode WDK AV/C
- Avc.sys function driver WDK , about Avc.sys function driver
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AV/C Overview


## <a href="" id="ddk-av-c-subunit-drivers-ksg"></a>


This section describes the Microsoft-supplied *Avc.sys* function driver that provides support for the IEEE 1394 Audio/Video Control (AV/C) protocol. This section also provides guidelines to develop AV/C subunit drivers for your AV/C-compliant device. Details of the AV/C protocol are available on the [1394 Trade Association's](http://go.microsoft.com/fwlink/p/?linkid=518448) website. Note that vendors might use the Microsoft-supplied drivers, *Msdv.sys* or *Mstape.sys*, to support their tape subunits, if applicable. These two class drivers make writing drivers for tape subunits unnecessary.

*Avc.sys* provides two operating modes: peer and virtual. The *Avc.sys* peer mode supports subunits on external AV/C devices. The *Avc.sys* virtual mode enables computer functionality to be exposed as an AV/C subunit, and therefore to make the computer a valid target for AV/C commands and requests from other AV/C devices across the IEEE 1394 serial bus.

*Avc.sys* uses separate driver stacks to support peer subunit and virtual subunits. Note that the different modes do not support identical functionality. For more information about the peer subunit and virtual subunit driver stacks, see [AV/C Driver Stacks](av-c-driver-stacks.md).

*Avc.sys* generates device identifiers (IDs) for both peer and virtual subunits. The device identifiers associate the correct INF files and subunit drivers with the subunits. When an AV/C device connects to the computer, *Avc.sys* enumerates the active subunits as peer subunits. Windows then loads the corresponding subunit driver. For more information about the format of both peer and virtual subunit device identifier strings, see [AV/C Device IDs](av-c-device-identifiers.md).

*Avc.sys* provides the following functionality:

-   Interim responses within the 100 millisecond requirement as defined by the AV/C specification on behalf of peer subunit drivers. *Avc.sys* returns only the final response of an AV/C command or query. Virtual subunit drivers must still generate interim and final responses.

-   Routing responses from AV/C subunits to their respective subunit drivers. Subunit drivers receive responses from only their hardware.

-   IEC-61883 plug enumeration and control within the kernel-streaming (KS) framework. For more information about plug connections and data formats, see [AV/C Subunit Plug Connection and Format Management](av-c-subunit-plug-connection-and-format-management.md).

Subunit drivers can use either the Stream class interface or the newer AVStream interface. Furthermore, a subunit driver can provide its own KS proxy plug-in to expose custom property pages to user-mode applications. For more information, see [AV/C Kernel-Streaming Interface and KS Proxy Plug-ins](av-c-kernel-streaming-interface-and-kernel-streaming-proxy-plug-ins.md).

Typically, vendors write an AV/C subunit driver to provide support to:

-   Control the subunit based on a device type defined by the [1394 Trade Association specifications](http://go.microsoft.com/fwlink/p/?LinkId=518448) website

-   Manage plug connections to stream data based on IEC-61883 standards across the IEEE 1394 bus. For more information about the 61883 standards, see the [IEC](http://go.microsoft.com/fwlink/p/?linkid=8732) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Overview%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


