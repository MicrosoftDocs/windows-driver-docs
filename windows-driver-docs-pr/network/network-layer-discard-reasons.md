---
title: Network layer discard reasons
author: windows-driver-content
description: This section describes Network layer discard reasons for Windows Filtering Platform callout drivers. |
ms.assetid: 30066077-53ac-43bb-8c8b-67af210f747e
keywords:
- Network layer discard reasons network drivers
ms.author: windowsdriverdev
ms.date: 11/09/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")