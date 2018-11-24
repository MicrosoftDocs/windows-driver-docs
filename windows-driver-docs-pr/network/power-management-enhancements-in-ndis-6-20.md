---
title: Power management enhancements in NDIS 6.20
description: Introduces NDIS 6.20 power management enhancements to reduce computer power consumption
ms.assetid: 99900def-66f8-4ba1-a7c1-3a5e9f456ca1
keywords:
- NDIS 6.20 WDK , power management enhancements
- power management WDK networking , NDIS 6.20 enhancements
- power management enhancements WDK NDIS 6.20
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management Enhancements in NDIS 6.20





NDIS 6.20 introduces power management enhancements to reduce computer power consumption. NDIS 6.20 power management support is mandatory for NDIS 6.20 and later drivers.

The NDIS 6.20 power management interface is backward compatible with NICs and miniport drivers that do not support the latest power management features.

The power management interface in NDIS 6.20 and later supports:

-   Wake on LAN (WOL) patterns that are based on the packet type in addition to the NDIS 6.1 and earlier methods that support an offset and pattern match. Therefore, NDIS 6.20 and later WOL patterns can be more specific to avoid unnecessary wake up events. For example, a NIC can identify TCP synchronize (SYN) packets.

-   Protocol offloads to NICs for some of the most common protocols. Because the protocols are offloaded to the NIC, it can respond on behalf of the computer to avoid unwanted wake up events. For example, a NIC can handle IPv4 Address Resolution Protocol (ARP) and IPv6 Neighbor Solicitation (NS) protocol packets without waking the computer.

The power management interface in NDIS 6.20 and later also supports:

-   WOL WLAN enhancements. If necessary, a NIC can handle IEEE 802.11 group temporal key (GTK) rekey requests in a low power state.

-   NDIS 6.20 and later can wake the computer when media connects. The operating system puts the NIC in a low power state when the media is disconnected.

Some of the NDIS device driver interface elements are obsolete for NDIS 6.20 and later drivers. For more information about obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

For more information about power management for NDIS 6.20 and later versions of NDIS, see [Power Management (NDIS 6.20)](power-management--ndis-6-20-.md).

## Related topics


[Power Management Enhancements in NDIS 6.30](introduction-to-ndis-6-30.md)

 

 






