---
title: Overview of NDIS packet timestamping
description: NDIS packet timestamping supports NICs' hardware timestamping capabilities
ms.date: 01/31/2021
ms.localizationpriority: medium
---

# Overview of NDIS packet timestamping

The NDIS packet timestamping interface supports the hardware timestamping capability of a network interface card (NIC) for the Precision Time Protocol (PTP) version 2. 

Many NICs can generate timestamps in their hardware when a packet is received or transmitted using their own hardware clock. Starting with NDIS 6.82, NDIS packet timestamping allows you to add hardware timestamping support to your NIC driver.

You may want to enable timestamping support to improve the accuracy of clock synchronization applications. The miniport driver should disable all types of timestamping support by default. 

Specifically, NDIS packet timestamping makes hardware timestamps available to the operating system so that applications implementing the PTP protocol can use them. The PTP is a protocol that utilizes hardware timestamps to achieve more accurate time synchronization between systems. It does this by accounting for delays that occur when a packet traverses a network. The PTP uses timestamps to compute the time a packet spends within the network stack of the machine before being sent from or received by the wire. The PTP can then use these calculations to improve time synchronization accuracy. 

The closer timestamp generation is to when a packet is sent or received by the network adapter hardware, the more accurate the synchronization application. Previously, applications on Windows could only report timestamps generated at the application layer. NDIS packet timestamping improves time synchronization accuracy by enabling applications to report timestamps generated in the NIC hardware.  

NDIS packet timestamping enables PTP version 2 applications (as defined by IEEE) operating in the two-step mode to use the NIC’s hardware timestamping capabilities. In two-step mode, timestamps in PTP packets are retrieved from the hardware and conveyed as separate messages rather than being generated on the fly in the hardware.

NDIS packet timestamping provides the ability to:

* Discover the NIC hardware’s timestamping capabilities.

* Associate the NIC hardware clock’s timestamps to PTP version 2 traffic running over UDP (using the standard UDP ports defined for PTP, for example 319 and 320).

* Use the NIC hardware’s clock as a free running clock. The ability to query the network hardware’s clock and establish a relation between the network hardware clock and a system clock makes this possible.

* Generate software timestamps.

The target of the NDIS packet timestamping interface is Ethernet hardware. The interface works with both NICs that specifically support hardware timestamp generation for PTP version 2 traffic as well as NICs that can generate hardware timestamps for all traffic, as these NICs work with PTP traffic as well.

## In this section

[Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md)

[Attaching timestamps to packets](attaching-timestamps-to-packets.md)

[Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md)

[Querying timestamping capabilities and configuration](querying-timestamping-capabilities-and-configuration.md)

