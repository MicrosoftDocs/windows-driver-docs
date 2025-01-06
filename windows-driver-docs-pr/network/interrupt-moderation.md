---
title: Interrupt Moderation
description: Learn how to use interrupt moderation to reduce the number of hardware interruptions.
keywords:
- interrupt moderation WDK networking
- interrupts WDK networking , reducing number of
- OID_GEN_INTERRUPT_MODERATION
- NDIS_INTERRUPT_MODERATION_PARAMETERS
- interrupts WDK networking , moderation
ms.date: 12/17/2024
---

# Interrupt moderation

To reduce the number of interrupts, many network interface cards (NICs) use *interrupt moderation*. With interrupt moderation, the NIC hardware doesn't generate an interrupt immediately after it receives a packet. Instead, the hardware waits for more packets to arrive, or for a time-out to expire, before generating an interrupt. The hardware vendor specifies the maximum number of packets, time-out interval, or other interrupt moderation algorithm.

The roundtrip time for a packet is one of the most commonly used measures to determine the network bandwidth between two endpoints. However, when interrupt moderation is enabled, receiving a packet doesn't generate an immediate interrupt and therefore the perceived roundtrip time for a particular packet becomes larger than the average time. To allow accurate measurement of roundtrip time for a packet, NDIS provides the ability to disable and enable interrupt moderation on demand.

All NDIS 6.0 and later miniport drivers must support the [OID\_GEN\_INTERRUPT\_MODERATION](./oid-gen-interrupt-moderation.md) OID. If a miniport driver doesn't support interrupt moderation, the driver must specify `NdisInterruptModerationNotSupported` in the `InterruptModeration` member of the [NDIS\_INTERRUPT\_MODERATION\_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_interrupt_moderation_parameters) structure.

NDIS 6.0 and later miniport drivers must support both the [OID\_GEN\_INTERRUPT\_MODERATION](./oid-gen-interrupt-moderation.md) OID set and query requests. The set request directs the miniport driver to enable or disable interrupt moderation and the query request reports the current state of interrupt moderation.

A miniport driver that supports interrupt moderation should turn on this capability by default unless the `InterruptModeration` standard keyword in the registry disables it. For more information about the standard keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

