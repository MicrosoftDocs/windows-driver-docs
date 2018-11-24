---
title: Network layer discard reasons
description: This section describes Network layer discard reasons for Windows Filtering Platform callout drivers. |
ms.assetid: 30066077-53ac-43bb-8c8b-67af210f747e
keywords:
- Network layer discard reasons network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# Network layer discard reasons

The identifiers for the possible reasons that data is discarded by one of the network layers are as follows. These identifiers are constant values in the IP_DISCARD_REASON enumeration that is defined in Fwpsk.h.

| Discard reason identifier | Discard reason description |
| --- | --- |
| IpDiscardBadSourceAddress | The outgoing packet's source address is a multicast address, a broadcast address, or an IPv6 address that contains an embedded IPv4 loopback or unspecified address. |
| IpDiscardNotLocallyDestined | The received packet's destination address does not exist on the system, and no appropriate forwarding interface exists. |
| IpDiscardProtocolUnreachable | There is either no transport protocol handler for the received packet or the transport protocol handler refused to process the packet. |
| IpDiscardPortUnreachable | There is no application that is receiving packets on the received packet's destination port. |
| IpDiscardBadLength | A length field specified within the received packet is inconsistent with the packet's length. |
| IpDiscardMalformedHeader | The received packet contains a recognized extension header or option whose contents are invalid. |
| IpDiscardNoRoute | The received packet cannot be forwarded to its destination address because the system's routing table does not contain a route to that destination. |
| IpDiscardBeyondScope | The received packet cannot be forwarded because the packet's incoming and outgoing network interfaces have different zone indexes for the packet's zone level. |
| IpDiscardInspectionDrop | Reserved for internal use by the network stack. |
| IpDiscardTooManyDecapsulations | The received packet cannot be forwarded to its destination address because there are too many decapsulations. |
| IpDiscardAdministrativelyProhibited | Reserved for internal use by the network stack. |
| IpDiscardHopLimitExceeded | The received packet's hop limit or time-to-live limit has been exceeded. |
| IpDiscardAddressUnreachable | The outgoing packet cannot be sent to the packet's destination address either because the destination does not exist or packets are not allowed to be sent to that destination. |
| IpDiscardRscPacket | The outgoing packet cannot be sent because it is a receive-side coalesced (RSC) packet. |
| IpDiscardArbitrationUnhandled | Reserved for internal use by the network stack. |
| IpDiscardInspectionAbsorb | The outgoing packet cannot be sent because WFP took ownership of the packet. |
| IpDiscardDontFragmentMtuExceeded | Reserved for internal use by the network stack. |
| IpDiscardBufferLengthExceeded | Reserved for internal use by the network stack. |
| IpDiscardAddressResolutionTimeout | Reserved for internal use by the network stack. |
| IpDiscardAddressResolutionFailure | Reserved for internal use by the network stack. |
| IpDiscardIpsecFailure | Reserved for internal use by the network stack. |
| IpDiscardExtensionHeadersFailure | Reserved for internal use by the network stack. |
| IpDiscardAllocationFailure | Reserved for internal use by the network stack. |

