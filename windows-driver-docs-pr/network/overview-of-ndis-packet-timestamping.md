---
title: Overview of NDIS packet timestamping
description: NDIS packet timestamping supports NICs' hardware timestamping capabilities
ms.date: 01/31/2021
ms.localizationpriority: medium
---

# Overview of NDIS packet timestamping

Starting with NDIS 6.82, the NDIS packet timestamping interface supports the hardware timestamping capability of a network interface card (NIC) for the Precision Time Protocol (PTP) version 2 protocol. 

Many NICs support timestamp generation in their hardware when a packet is received or transmitted. Timestamps are generated using the NIC’s hardware clock.  The PTP, a time synchronization protocol that makes provision to use such hardware timestamps within the protocol itself, particularly utilizes this ability. The PTP can use timestamps to compute the time a packet spends within the network stack of the machine before being sent from or received by the wire. The PTP can use these calculations to improve time synchronization accuracy.

NDIS packet timestamping enables NIC drivers to support hardware timestamps and also generate timestamps in software. To learn more about how user mode applications can query timestamp configuration, see the Iphlpapi packet timestamping documentation. For more information on how user mode applications can consume timestamps associated with packets, see the WinSock timestamping documentation. 

NDIS packet timestamping enables PTP version 2 applications (as defined by IEEE) operating in the two-step mode to use the NIC’s hardware timestamping capabilities. Two-step refers to the mode in which the timestamps in the PTP packets are not generated on the fly in the hardware, but are rather retrieved from the hardware and conveyed as separate messages.  

NDIS packet timestamping provides the ability to:

* Discover the NIC hardware’s timestamping capabilities.

* Associate the NIC hardware clock’s timestamps to PTP version 2 traffic running over UDP (using the standard UDP ports defined for PTP, for example 319 and 320).

* Use the NIC hardware’s clock as a free running clock. The ability to query the network hardware’s clock and establish a relation between the network hardware clock and a system clock makes this possible.

The target of the NDIS packet timestamping interface is Ethernet hardware. The interface works with both NICs that specifically support hardware timestamp generation for PTP version 2 traffic as well as NICs that can generate hardware timestamps for all traffic, as these NICs work with PTP traffic as well.

The following sections describe the NDIS packet timestamping interface:

[Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md)

[Attaching timestamps to packets](attaching-timestamps-to-packets.md)

[Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md)

[Querying timestamping capabilities and configuration](querying-timestamping-capabilities-and-configuration.md)

