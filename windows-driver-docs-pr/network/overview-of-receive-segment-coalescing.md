---
title: Overview of Receive Segment Coalescing
description: When receiving data, the miniport driver, NDIS, and TCP/IP must all look at each segment's header information separately.
ms.assetid: 1E9BC335-BB62-415B-B242-D63672A4E406
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Receive Segment Coalescing


When receiving data, the miniport driver, NDIS, and TCP/IP must all look at each segment's header information separately. When large amounts of data are being received, this creates a large amount of overhead. Receive segment coalescing (RSC) reduces this overhead by coalescing a sequence of received segments and passing them to the host TCP/IP stack in one operation, so that NDIS and TCP/IP need only look at one header for the entire sequence.

RSC is intended to support coalescing in a way that:

-   Doesn't interfere with the normal operation of TCP's congestion and flow control mechanisms.

-   Coalesces packets without discarding information that is used by the TCP stack.

RSC-capable miniport drivers for network cards must:

-   Follow a standard set of rules when coalescing segments.

-   Provide certain out-of-band information to the host TCP/IP stack.

The following sections provide an overview of RSC.

-   [Rules for Coalescing TCP/IP Segments](rules-for-coalescing-tcp-ip-packets.md)
-   [Updating the IP Headers for Coalesced Segments](updating-the-ip-headers-for-coalesced-segments.md)
-   [Examples of Receive Segment Coalescing](examples-of-receive-segment-coalescing.md)
-   [Indicating Coalesced Segments](indicating-coalesced-segments.md)
-   [Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md)

 

 





