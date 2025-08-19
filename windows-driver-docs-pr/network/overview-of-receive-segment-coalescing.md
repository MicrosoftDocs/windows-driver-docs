---
title: Overview of Receive Segment Coalescing
description: Learn how to use receive segment coalescing (RSC) to reduce overhead by coalescing a sequence of received segments and passing them to the host TCP/IP stack.
ms.date: 01/07/2024
ms.topic: concept-article
---

# Overview of receive segment coalescing

When receiving data, the miniport driver, Network Driver Interface Specification (NDIS), and TCP/IP must all look at each protocol data unit (PDU) header information separately. When large amounts of data are being received, a large amount of overhead is created. Receive segment coalescing (RSC) reduces this overhead by coalescing a sequence of received segments and passing them to the host TCP/IP stack in one operation, so that NDIS and TCP/IP need to only look at one header for the entire sequence.

RSC is intended to support coalescing in a way that:

- Doesn't interfere with the normal operation of TCP's congestion and flow control mechanisms.

- Coalesces packets without discarding information that is used by the TCP stack.

RSC-capable miniport drivers for network cards must:

- Follow a standard set of rules when coalescing segments.

- Provide certain out-of-band information to the host TCP/IP stack.

## Related content

The following sections provide an overview of RSC.

- [Rules for Coalescing TCP/IP Segments](rules-for-coalescing-tcp-ip-packets.md)
- [Updating the IP Headers for Coalesced Segments](updating-the-ip-headers-for-coalesced-segments.md)
- [Examples of Receive Segment Coalescing](examples-of-receive-segment-coalescing.md)
- [Indicating Coalesced Segments](indicating-coalesced-segments.md)
- [Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md)
