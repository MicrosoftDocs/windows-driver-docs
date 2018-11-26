---
title: WIA with Web Services for Devices
description: WIA with Web Services for Devices
ms.assetid: e1f91963-503b-4766-a6f1-c334465f0e73
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA with Web Services for Devices


In Windows, the operating system supports network-connected image scanner devices that implement Web Services for Devices (WSD).

The WSD Scan driver is an inbox Microsoft Windows Image Acquisition (WIA) class driver for web services scanners. This driver is compliant with the Windows Device Protocol (WDP) for scanners.

The WSD Scan driver package contains a reusable kernel driver component, *WSDScan.sys*, that is intended specifically to install web services scanner devices. 

Windows also includes the *WSD Challenger*, which is a module that enables web services clients to challenge disconnected devices to reestablish device communication when the device comes back online.

> [!IMPORTANT]  
> WSD Challenger functionality has been deprecated and all WSD Challenger-related documentation will be removed in 2018.

The following sections describe how to use *WSDScan.sys* to install a WIA driver for a web services scanner, how to use function discovery to initialize SOAP communications with the scanner device from within the WIA driver, and how to challenge a disconnected device by using the WSD Challenger:

[Installing a WIA Scanner Driver with WSD](installing-a-wia-scanner-driver-with-wsd.md)

[SOAP Communications for WIA Scanners](soap-communications-for-wia-scanners.md)

[Challenging a Disconnected Scanner with WSD](challenging-a-disconnected-scanner-with-the-wsd-challenger.md)

