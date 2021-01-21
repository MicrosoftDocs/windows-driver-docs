---
title: Overview of NDIS packet timestamping
description: NDIS packet timestamping supports NICs' hardware timestamping capabilities
ms.date: 12/31/2020
ms.localizationpriority: medium
---

# Overview of NDIS packet timestamping

Starting with NDIS 6.82, the NDIS packet timestamping interface enables Windows to support the hardware timestamping capability of network cards for the Precision Time Protocol (PTP) version 2 protocol. 

Many network cards support the ability to generate a timestamp in their hardware when a packet is received or transmitted. The timestamp is generated using the NIC’s own hardware clock. This ability is particularly utilized by the PTP which is a time synchronization protocol that makes provision to use such hardware timestamps within the protocol itself. Such timestamps can be used to compute the time a packet spends within the network stack of the machine before being sent from or received by the wire. These calculations can then be used to improve the accuracy of time synchronization by PTP.

NDIS packet timestamping enables drivers of network cards to support hardware timestamps. It also enables network drivers to generate timestamps in software. To learn more about how user mode applications can query timestamp configuration, see the Iphlpapi packet timestamping documentation. For more information on how user mode applications can consume timestamps associated with packets, see the WinSock timestamping documentation. 

NDIS packet timestamping enables PTP version 2 applications (as defined by IEEE) operating in the two-step mode to use the NIC’s hardware timestamping capabilities. Two-step refers to the mode in which the actual timestamps in the PTP packets are not generated on the fly in the hardware but are retrieved from the hardware and conveyed as separate messages (for example, using a follow up message).  

NDIS packet timestamping provides the ability to:

* Discover the NIC hardware’s timestamping capabilities.

* Associate the NIC hardware clock’s timestamps to PTP version 2 traffic running over UDP (using the standard UDP ports defined for PTP, for example 319 and 320).

* Use the NIC hardware’s clock as a free running clock. The ability to query the network hardware’s clock and establish a relation between the network hardware clock and a system clock makes this possible.

The target of the NDIS packet timestamping interface is Ethernet hardware. It's intended to work both with NICs that specifically support generating hardware timestamps for PTP version 2 traffic as well as NICs that can generate hardware timestamps for all traffic, as these NICs work with PTP traffic as well.

The following sections describe the NDIS packet timestamping interface:

[Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md)

[Attaching timestamps to packets](attaching-timestamps-to-packets.md)

[Querying timestamping capabilities and configuration](querying-timestamping-capabilities-and-configuration.md)

[Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md)

## NDIS packet timestamping implementation requirements

When implementing support for packet timestamping, keep the following in mind:

* An implementation must support hardware timestamps. Software timestamps are optional.

* Cross timestamps must be supported when supporting hardware timestamps. 

* When recognizing PTP version 2 packets to generate hardware timestamps, the implementation should aim as much as possible to not restrict timestamp generation to only those packets which are using the multicast addresses (both IPv4 and IPv6) which are specified by the PTP specification. The implementation should try to recognize PTP packets in other ways, e.g. based on the UDP header, or the PTP payload. This would help in scenarios where a PTP implementation might not be using the multicast addresses specified in the PTP specification e.g. unicast address are being used.

* If an implementation finds both hardware and software timestamps as enabled through the keywords, then the miniport should only generate hardware timestamps and disable software timestamps.

