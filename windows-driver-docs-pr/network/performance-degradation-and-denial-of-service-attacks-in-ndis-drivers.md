---
title: Performance degradation and DoS attacks in NDIS drivers
description: Performance Degradation and Denial of Service Attacks in NDIS Drivers
ms.assetid: 0e80c6e2-3e6d-4189-b2df-bdd9a4a40dd6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performance Degradation and Denial of Service Attacks in NDIS Drivers




If an NDIS driver interrupt handler parses received packets, the interrupt handler implementation might lead to performance degradation and denial of service attacks. For example, a malicious user can target the computer by sending many packets so that the miniport driver is busy computing the checksum on bad packets in the interrupt handler.

Even if you are careful in how your driver handles received packets, the driver would perform receive operations at dispatch IRQL. Instead, you should let the driver stack handle the received packets. In this case, the overlying driver stack might copy the packet and operate on it later at passive IRQL.

 

 





