---
title: Security Guidelines for Offload-Capable Miniport Drivers
description: Security Guidelines for Offload-Capable Miniport Drivers
ms.assetid: 178be416-3936-4e17-b055-134897b3e2eb
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security Guidelines for Offload-Capable Miniport Drivers





To increase its performance, the Microsoft TCP/IP transport can offload tasks or connections to a network interface card (NIC) that has the appropriate TCP/IP-offload capabilities. Offloaded TCP/IP network communication tasks are handled in the NIC hardware. Miniport drivers advertise the various offload capabilities of the NIC hardware to the operating system and confugure the NIC hardware. The NIC hardware performs the advertised offload tasks on outgoing and incoming packets in the send and receive dispatch handlers. The hardware performs operations such as computing IP header checksum and so on.

To ensure a secure environment, the miniport driver should advertise only those offload capabilities that the NIC hardware can provide and no others. The miniport driver should configure the hardware to offload the advertised tasks on the packets that meet the advertised criteria. On the send path, the operating system does not require a driver to offload a task that the miniport driver did not advertise. On the receive path, the miniport driver and NIC should not perform any tasks that are not included in the capabilities of the NIC hardware that the miniport driver advertised.

If a miniport driver or NIC cannot perform an offload task on a received packet, the miniport driver should indicate such a packet up the driver stack without taking any action. In this case, the overlying drivers handle the packet as a normal packet.

The miniport driver should never advertise capabilities that the NIC hardware does not support. The miniport driver should never use the send or receive dispatch handlers to perform software emulation of the offload operations that the hardware cannot provide. If the miniport driver provides such software emulation, the driver must inspect the packet data in software. If the driver inspects the packet data in software, the computer might be exposed to security attacks.

The following topics provide more information about security attacks and how to avoid security problems in NDIS drivers:

[Vulnerability to Security Attacks in NDIS Drivers](vulnerability-to-security-attacks-in-ndis-drivers.md)

[Performance Degradation and Denial of Service Attacks in NDIS Drivers](performance-degradation-and-denial-of-service-attacks-in-ndis-drivers.md)

[Added Costs for Testing Vulnerable NDIS Drivers](added-costs-for-testing-vulnerable-ndis-drivers.md)

[Security Checklist for NDIS Drivers](security-checklist-for-ndis-drivers.md)

 

 





