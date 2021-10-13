---
title: Smart Card Reader Devices Design Guide
description: Design guide for developing drivers for smart card reader devices.
ms.assetid: e0827569-6c76-42a1-b94f-29235646519f
keywords:
- smart card drivers WDK
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Smart Card Reader Devices Design Guide

Design guide for developing drivers for smart card reader devices.

## In this section

|Topic|Description|
|----|----|
|[Smart Card Driver Environment](smart-card-driver-environment.md)|Describes the standard environment for the smart card reader driver.|
|[Management of IOCTL Requests in a Smart Card Reader Driver](management-of-ioctl-requests-in-a-smart-card-reader-driver.md)|Explains how reader drivers manage IOCTL requests, how the callback routine mechanism works, and what a reader driver must do to initialize its callback routines.|
|[WDM Reader Driver](wdm-reader-driver.md)|Lists the routines that are required by a WDM reader driver.|
|[Smart Card Minidrivers](smart-card-minidrivers.md)|The smart card minidriver provides a simpler alternative to developing a legacy cryptographic service provider (CSP) by encapsulating most of the complex cryptographic operations from the card minidriver developer.|
|[Smart Card Reader States](smart-card-reader-states.md)|A table listing the Smart Card reader states and their meanings.|
|[Installing Smart Card Reader Drivers](installing-smart-card-reader-drivers.md)|Provides installation information that is specific to smart card reader drivers for Windows.|
|[Registering a WDM Smart Card Reader Driver](registering-a-wdm-smart-card-reader-driver.md)|Provides required registry values and their descriptions for registering a WDM Smard Card Reader driver.|
|[Enabling Smart Card Event Logging in the Registry](enabling-smart-card-event-logging-in-the-registry.md)|Registry value name and contents of the registry value for event logging.|
|[WDM Device Names for Smart Card Readers](wdm-device-names-for-smart-card-readers.md)|Instructions for complying with the naming conventions for device names in Windows operating systems.|
|[Smart Card Driver Debugging](smart-card-driver-debugging.md)|Describes the smart card driver libraries support of debugging features.|
|[Specifications and Resources](specifications-and-resources.md)|To work with the smart card support in Microsoft Windows operating systems, smart card readers and cards should be compatible with Interoperability Specification for ICCs and Personal Computer Systems. Smart card readers and device drivers should also be Plug and Play compliant.</p></td>
</tr>
</tbody>
</table>

 

 

 





