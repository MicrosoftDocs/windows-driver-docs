---
title: Indicating Coalesced Segments
description: This section describes how to indicate coalesced segments
ms.assetid: 79A37DAB-D9B3-4FA2-8258-05E10BD6E3CB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Coalesced Segments


A single coalesced unit (SCU) is a sequence of TCP segments that are coalesced into a single TCP segment according to the rules defined in [Rules for Coalescing TCP/IP Segments](rules-for-coalescing-tcp-ip-packets.md). This section describes how to indicate the resulting coalesced segments.

An SCU must:

-   Be indicated by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

-   Look like a normal TCP segment that is received over the wire.

-   Be no larger than the maximum legal IP datagram length, as defined in section 3.1 of [RFC 791](http://www.ietf.org/rfc/rfc791.txt).

    **Note**  Because segments with IPv6 extension headers cannot be coalesced (see [Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md)), the size of the SCU for IPv6 datagrams is also limited by the maximum legal datagram length.

     

The NIC or miniport driver should recompute the TCP and IPv4 checksums, if applicable, before indicating the coalesced segment. If the NIC or miniport driver validates the TCP and IPv4 checksums but does not recompute them for the coalesced segment, it must set the **TcpChecksumValueInvalid** and **IpChecksumValueInvalid** flags in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877) structure. Additionally, in this case the NIC or miniport driver may optionally zero out the TCP and IPv4 header checksum values in the segment.

The NIC and miniport driver must always set the **IpChecksumSucceeded** and **TcpChecksumSucceeded** flags in the [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877) structure before indicating the coalesced segment.

For more information about coalescing rules, see [Rules for Coalescing TCP/IP Segments](rules-for-coalescing-tcp-ip-packets.md).

For more information about exceptions, see [Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md).

Coalescing is expected to be performed on a best-effort basis. The hardware might not be able to coalesce in some cases, for example due to lack of resources. The requirements stated here are primarily to specify when not to coalesce and how to coalesce.

At a high level, the NIC and miniport driver must handle the receipt of a TCP segment over the wire as follows:

-   Check the incoming segment for an exception as follows:

    1.  If no exception was encountered, check whether the segment can be coalesced with the last segment that was received for the same TCP connection per the rules.

    2.  If the segment triggered an exception, or if coalescing it with the previously received segment is not possible, then indicate the segment individually.

-   The NIC and miniport driver must not indicate coalesced segments until the protocol driver enables RSC as described in [Querying and Changing RSC State](querying-and-changing-rsc-state.md).

-   For a given TCP connection, a data indication from the miniport adapter to the host TCP/IP stack may consist of one or more coalesced segments, separated by one or more individual segments that could not be coalesced.

-   The NIC and miniport driver must not delay the indication of TCP segments, whether coalesced or not. Specifically, the NIC and miniport driver must not delay the indication of segments from one deferred procedure call (DPC) to the next in order to attempt to coalesce the segments.

-   The NIC and miniport driver may use timers to determine the end of coalescing. However, the handling of latency sensitive workloads must be as effective as the DPC boundary requirement.

 

 





