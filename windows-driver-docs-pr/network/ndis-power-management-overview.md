---
title: NDIS Power Management Overview
description: NDIS Power Management Overview
ms.assetid: 8ae3803f-c3e4-4499-9e61-678f4ab61fbc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Power Management Overview





This section provides an overview of the features that are provided with the power management interface that is introduced in Windows 7 for NDIS 6.20 drivers.

Miniport drivers and protocol drivers that support NDIS 6.20 and later versions of NDIS must support the NDIS 6.20 power management interface. However, NDIS provides translation to the previous interface for older network adapters and NDIS 6.1 or earlier miniport drivers that do not support the NDIS 6.20 power management features. For more information about NDIS 6.20 backward compatibility issues, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md).

The NDIS 6.20 power management interface supports:

-   Wake-on-LAN (WOL) patterns that are based on the packet type in addition to the NDIS 6.1 and earlier methods. Therefore, NDIS 6.20 WOL patterns can be more specific to avoid unnecessary wake-up events. For example, a network adapter can identify TCP synchronize (SYN) packets. For more information about WOL methods, see [WOL Methods in NDIS 6.20](wol-methods-in-ndis-6-20.md).

-   Protocol offloads to network adapters for some of the most common protocols. Because the protocols are offloaded to the network adapter, it can respond on behalf of the computer to avoid unwanted wake-up events. For example, a network adapter can handle IPv4 Address Resolution Protocol (ARP) and IPv6 Neighbor Solicitation (NS) protocol packets without waking the computer. For more information about power management protocol offloads, see [Protocol Offloads for NDIS Power Management](protocol-offloads-for-ndis-power-management.md).

For information about the WOL event sequences that NDIS uses to set a low-power state and restore full power, see [Low Power for Wake on LAN](low-power-for-wake-on-lan.md).

The NDIS 6.20 power management also supports:

-   NDIS 6.20 can return the network adapter to a full-power state when the media connects. The operating system puts the network adapter in a low-power state when the media is disconnected. For more information about setting a low-power state when media disconnects, see [Low Power on Media Disconnect](low-power-on-media-disconnect.md).

This section includes the following topics:

[WOL Methods in NDIS 6.20](wol-methods-in-ndis-6-20.md)

[WOL Patterns for NDIS Power Management](wol-patterns-for-ndis-power-management.md)

[Protocol Offloads for NDIS Power Management](protocol-offloads-for-ndis-power-management.md)

 

 





