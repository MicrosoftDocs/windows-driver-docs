---
title: Programming Considerations for RSC Drivers
description: The following sections describe issues to consider when implementing a receive-segment coalescing (RSC)-capable miniport driver.
ms.assetid: 03FDD557-3918-408A-BD79-64CD52BDD43A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Programming Considerations for RSC Drivers


The following sections describe issues to consider when implementing a receive-segment coalescing (RSC)-capable miniport driver.

-   [Responding to Queries for RSC Statistics](#responding-to-queries-for-rsc-statistics)
-   [Forwarded TCP Packets](#forwarded-tcp-packets)
-   [RSC Support for Lightweight Filters and MUX Intermediate Drivers](#rsc-support-for-lightweight-filters-and-mux-intermediate-drivers)
-   [Windows Filtering Platform (WFP) Inspection and Callout Drivers](#windows-filtering-platform-wfp-inspection-and-callout-drivers)

## Responding to Queries for RSC Statistics


NDIS, overlying drivers, and user-mode applications use the [OID\_TCP\_RSC\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/hh451929) OID to get the RSC statistics of a miniport adapter. RSC-capable miniport drivers must support this OID.

## Forwarded TCP Packets


The miniport driver shouldn't perform RSC on segments in TCP packets that aren't intended for the host but are being forwarded out on another interface.

The host TCP/IP stack will disable RSC on any interface that has forwarding enabled. Weak host forwarding does not affect RSC.

## RSC Support for Lightweight Filters and MUX Intermediate Drivers


All NDIS 6.30 lightweight filter drivers must support receive packets that are larger than the link maximum transmission unit (MTU). For more information about segment size limits, see [Indicating Coalesced Segments](indicating-coalesced-segments.md).

NDIS will disable RSC on an interface if any lightweight filter driver or MUX intermediate driver in the host stack is NDIS 6.20 or lower.

A MUX intermediate driver may disable RSC on an interface, even if the interface's NDIS version is 6.30 or higher.

## Windows Filtering Platform (WFP) Inspection and Callout Drivers


WFP callout drivers provide additional filtering functionality by adding custom callout functions to the filter engine at one or more of the kernel-mode filtering layers. Callouts support deep inspection and packet as well as stream modification.

WFP callout drivers may support handling of support receive packets that are larger than the link MTU. (For more information about packet size limits, see [Tracking and Indicating Coalesced Segments](https://msdn.microsoft.com/library/windows/hardware/jj853326).) Such WFP callout drivers should do the following:

-   Opt in during registration to handle large packets.

-   Set the callout driver flag as specified in the reference page for the [**FWPS\_CALLOUT2**](https://msdn.microsoft.com/library/windows/hardware/hh439700) structure.

Whenever a callout driver that has not opted in to handle large packets is registered, WFP will notify TCP/IP in the context of the registration. As part of handling this notification, TCP/IP will disable RSC on the interface.

If there is active TCP traffic during callout registration, TCP/IP will notify WFP. WFP will delay calling the registered filters until RSC is disabled. This will protect callout drivers from large packets.

 

 





