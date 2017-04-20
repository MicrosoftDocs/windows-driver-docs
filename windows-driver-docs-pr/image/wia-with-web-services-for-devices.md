---
title: WIA with Web Services for Devices
author: windows-driver-content
description: WIA with Web Services for Devices
ms.assetid: e1f91963-503b-4766-a6f1-c334465f0e73
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA with Web Services for Devices


In Windows Vista and later versions of Windows, the operating system supports network-connected image scanner devices that implement Web Services for Devices (WSD).

The WSD Scan driver is an inbox Microsoft Windows Image Acquisition (WIA) class driver for web services scanners. This driver is compliant with the Windows Device Protocol (WDP) for scanners and is new with Windows Vista.

The WSD Scan driver package contains a reusable kernel driver component, *WSDScan.sys*, that is intended specifically to install web services scanner devices. Windows Vista also includes the *WSD Challenger*, which is a module that enables web services clients to challenge disconnected devices to reestablish device communication when the device comes back online.

The following sections describe how to use *WSDScan.sys* to install a WIA driver for a web services scanner, how to use function discovery to initialize SOAP communications with the scanner device from within the WIA driver, and how to challenge a disconnected device by using the WSD Challenger:

[Installing a WIA Scanner Driver with WSD](installing-a-wia-scanner-driver-with-wsd.md)

[SOAP Communications for WIA Scanners](soap-communications-for-wia-scanners.md)

[Challenging a Disconnected Scanner with WSD](challenging-a-disconnected-scanner-with-the-wsd-challenger.md)

Although WDP for scanners is well suited for a home office or small office environment, it cannot conveniently handle more than a few users. In Windows Server 2008 R2, the operating system supports WSD Distributed Scan Management. This feature augments WDP with a new WSD protocol to enable IT administrators to provide scanning services to large organizations. A web services scanner device that supports WSD Distributed Scan Management must implement the following two web services protocols:

-   The WSD Enterprise Scan Web Service (EWS) protocol, which is a subset of WDP.

-   The WSD Repository Processing Web Service (RPWS) protocol.

The following section provides more information about WSD Distributed Scan Management:

[Web Services for Devices Distributed Scan Management](distributed-scan-management--dsm-.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20with%20Web%20Services%20for%20Devices%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


