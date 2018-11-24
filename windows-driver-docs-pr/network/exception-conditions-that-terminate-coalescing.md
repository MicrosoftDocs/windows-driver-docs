---
title: Exception Conditions that Terminate Coalescing
description: This section defines the checks that a receive segment coalescing (RSC)-capable miniport driver must perform on a segment before it can be coalesced.
ms.assetid: 6294541A-AF32-46CF-81AB-5855EA440053
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exception Conditions that Terminate Coalescing


This section defines the checks that a receive segment coalescing (RSC)-capable miniport driver must perform on a segment before it can be coalesced.

A segment must pass both of the following types of checks before it can be coalesced:

-   Checks for presence of a certain condition in the segment. For example, the presence of a SYN flag in the TCP header would trigger an exception and the segment would not be coalesced. These types of checks are defined below.

-   Checks that depend on inspecting and correlating information from previously coalesced segments and the currently examined segments. For example, checking if the received segment is a duplicate acknowledgment falls in this category of checks. These types of checks are defined in [Rules for Coalescing TCP/IP Segments](rules-for-coalescing-tcp-ip-packets.md).

If a check fails, an exception is triggered, and the miniport driver must terminate coalescing for that TCP connection and treat segments as follows:

-   TCP segments that were coalesced before the exception was detected should be indicated as a single unit.

-   TCP segments that are coalesced after the exception is detected should be indicated as a separate unit.

**Note**  For exceptions 7 and 8 below, the miniport driver should resume coalescing starting with the segment that triggered the exception.

 

Receiving a segment that meets any of the following criteria must trigger an exception:

1.  The hardware resource constraints in the NIC prevent coalescing.

2.  The segment has an invalid TCP or IP checksum.

3.  The segment contains any of the SYN, URG, RST, FIN in its TCP header, as defined in section 3.1 of [RFC 793](http://www.ietf.org/rfc/rfc793.txt). More broadly, if the segment contains any flag other than PSH or ACK, it should trigger an exception. For ECN flags, see exception 8 below.

4.  The segment contains one or more TCP options other than the TCP timestamp option. See [RFC 1323](http://www.ietf.org/rfc/rfc1323.txt) for a discussion of the TCP timestamp option.

5.  The segment contains IPv4 options or IPv6 extension headers.

6.  The segment is an IPv4 fragment.

7.  Coalescing the currently received segment will cause the single coalesced unit to exceed the maximum legal IP Datagram length. This exception requires special handling. For more information, see:

    -   The first flowchart in [Rules for Coalescing TCP/IP Packets](rules-for-coalescing-tcp-ip-packets.md)

    -   "Responding to Queries for RSC Statistics" in [Programming Considerations for RSC Drivers](programming-considerations-for-rsc-drivers.md).

8.  The segment contains ECN flags, as defined in [RFC 3168](http://www.ietf.org/rfc/rfc3168.txt), that meet one or both of the following criteria:

    1.  The segment contains a different value for the ECN field (ECT, CE) in the IP header than the previous segment.

    2.  The segment has a different value for the ECN flags (ECE and CWR) in the TCP header than the previous segment.

 

 





