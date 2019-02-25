---
title: WOL Methods in NDIS 6.20
description: WOL Methods in NDIS 6.20
ms.assetid: A46C213D-B356-44A3-8863-D7B183B73C77
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WOL Methods in NDIS 6.20





The power management capabilities that are supported in NDIS 6.20 and later versions of NDIS consist of the following wake-on-LAN (WOL) methods:

-   Wake on magic packet

-   Wake on pattern match

-   Wake device on media connect

For more information about the power management capabilities in previous versions of Windows, see [Power Management (NDIS 6.0 and Later)](https://msdn.microsoft.com/library/windows/hardware/hh205401).

The *wake on magic packet* method wakes the computer when the network adapter receives a *magic packet*. A *magic packet* contains 16 contiguous copies of the receiving network adapter's Ethernet address.

The *wake on magic packet* method is separate from the *wake on pattern match* method. WOL patterns include other packet types or a bitmap. For more information about WOL patterns, see [WOL Patterns for NDIS Power Management](wol-patterns-for-ndis-power-management.md).

Although some network adapters report support for the *wake device on media connect* method, previous versions of Windows did not. Windows 7 fully supports the *wake device on media connect* method if an NDIS 6.20 miniport driver reports support. NDIS sets the network adapter to a low power state if the media is disconnected.

For more information about the *wake device on media connect* method, see [Low Power on Media Disconnect](low-power-on-media-disconnect.md).

 

 





