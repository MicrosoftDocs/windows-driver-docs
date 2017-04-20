---
title: RSS Hashing Types
description: RSS Hashing Types
ms.assetid: 21ea384c-5fe2-46c1-9e01-30513f505672
keywords:
- receive-side scaling WDK networking , hash
- RSS WDK networking , hash
- hash WDK RSS
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# RSS Hashing Types


## <a href="" id="ddk-rss-hashing-types-ng"></a>


The RSS hashing type specifies the portion of received network data that a NIC must use to calculate an RSS hash value.

Overlying drivers set the hash type, function, and indirection table. The hash type that the overlying driver sets can be a subset of the type that the miniport driver can support. For more information, see [RSS Configuration](rss-configuration.md).

The hash type is an OR of valid combinations of the following flags:

NDIS\_HASH\_IPV4

NDIS\_HASH\_TCP\_IPV4

NDIS\_HASH\_IPV6

NDIS\_HASH\_TCP\_IPV6

NDIS\_HASH\_IPV6\_EX

NDIS\_HASH\_TCP\_IPV6\_EX

There are three sets of valid flag combinations.

IPv4 (combinations of NDIS\_HASH\_IPV4 and NDIS\_HASH\_TCP\_IPV4)

IPv6 (combinations of NDIS\_HASH\_IPV6 and NDIS\_HASH\_TCP\_IPV6)

IPv6 with extension headers (combinations of NDIS\_HASH\_IPV6\_EX and NDIS\_HASH\_TCP\_IPV6\_EX)

A NIC must support one of the combinations from the IPv4 set. The other sets and combinations are optional. A NIC can support more than one set at a time. In this case, the type of data received determines which hash type the NIC uses.

In general, if the NIC cannot interpret the received data correctly, it must not compute the hash value. For example, if the NIC only supports IPv4 and it receives anIPv6 packet, which it cannot interpret correctly, it must not compute the hash value. If the NIC receives a packet for a transport type that it does not support, it must not compute the hash value. For example, if the NIC receives a UDP packet when it is supposed to be calculating hash values for TCP packets, it must not compute the hash value. In this case, the packet is processed as in the non-RSS case. For more information about the non-RSS receive processing, see [Non-RSS Receive Processing](non-rss-receive-processing.md).

The three valid hash type combinations in the IPv4 set:

<a href="" id="ndis-hash-ipv4"></a>NDIS\_HASH\_IPV4  
If this flag alone is set, the NIC should compute the hash value over the following IPv4 header fields:

Source-IPv4-Address

Destination-IPv4-Address

Note that if a NIC receives a packet that has both IP and TCP headers, NDIS\_HASH\_TCP\_IPV4 should not always be used. In the case of a fragmented IP packet, NDIS\_HASH\_IPV4 must be used. This includes the first fragment which contains both IP and TCP headers.

<a href="" id="ndis-hash-tcp-ipv4"></a>NDIS\_HASH\_TCP\_IPV4
If this flag alone is set, the NIC should parse the received data to identify an IPv4 packet that contains a TCP segment.

The NIC must identify and skip over any IP options that are present. If the NIC cannot skip over any IP options, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

Source-IPv4-Address

Destination-IPv4-Address

Source TCP Port

Destination TCP Port

<a href="" id="ndis-hash-tcp-ipv4---ndis-hash-ipv4"></a>NDIS\_HASH\_TCP\_IPV4 | NDIS\_HASH\_IPV4
If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS\_HASH\_TCP\_IPV4 case.

However, if the packet does not contain a TCP header, the NIC should compute the hash value as specified in the NDIS\_HASH\_IPV4 case.

The three valid hash type combinations in the IPv6 set are:

<a href="" id="ndis-hash-ipv6"></a>NDIS\_HASH\_IPV6  
If this flag alone is set, the NIC should compute the hash over the following fields:

Source-IPv6-Address

Destination-IPv6-Address

<a href="" id="ndis-hash-tcp-ipv6"></a>NDIS\_HASH\_TCP\_IPV6
If this flag alone is set, the NIC should parse the received data to identify an IPv6 packet that contains a TCP segment.

The NIC must identify and skip over any IPv6 extension headers that are present in the packet. If the NIC cannot skip over any IPv6 extension headers, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

Source-IPv6 -Address

Destination-IPv6 -Address

Source TCP Port

Destination TCP Port

<a href="" id="ndis-hash-tcp-ipv6---ndis-hash-ipv6"></a>NDIS\_HASH\_TCP\_IPV6 | NDIS\_HASH\_IPV6
If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS\_HASH\_TCP\_IPV6 case.

However, if the packet does not contain a TCP header, the NIC should compute the hash as specified for the NDIS\_HASH\_IPV6 case:

The three valid combinations in the IPv6 with extension headers set are:

<a href="" id="ndis-hash-ipv6-ex"></a>NDIS\_HASH\_IPV6\_EX  
If this flag alone is set, the NIC should compute the hash over the following fields:

Home address from the home address option in the IPv6 destination options header. If the extension header is not present, use the Source IPv6 Address

IPv6 address that is contained in the Routing-Header-Type-2 from the associated extension header. If the extension header is not present, use the Destination IPv6 Address

<a href="" id="ndis-hash-tcp-ipv6-ex"></a>NDIS\_HASH\_TCP\_IPV6\_EX
If this flag alone is set, the NIC should compute the hash over the following fields:

Home address from the home address option in the IPv6 destination options header. If the extension header is not present, use the Source IPv6 Address

IPv6 address that is contained in the Routing-Header-Type-2 from the associated extension header. If the extension header is not present, use the Destination IPv6 Address

Source TCP Port

Destination TCP Port

<a href="" id="ndis-hash-tcp-ipv6-ex---ndis-hash-ipv6-ex"></a>NDIS\_HASH\_TCP\_IPV6\_EX | NDIS\_HASH\_IPV6\_EX
If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS\_HASH\_TCP\_IPV6\_EX case.

However, if the packet does not contain a TCP header, the NIC should compute the hash as specified for the NDIS\_HASH\_IPV6\_EX case:

**Note**  If a miniport driver reports NDIS\_RSS\_CAPS\_HASH\_TYPE\_TCP\_IPV6\_EX capability for a NIC, the NIC must calculate hash values (over fields in the IPv6 extension headers) in accordance with the IPv6 extension hash types that the protocol driver set. The NIC can store either the extension hash type or the regular hash type in the NET\_BUFFER\_LIST structure of the IPv6 packet for which a hash value is computed.

 

A miniport driver sets the hash type in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure before indicating the received data. For more information, see [Indicating RSS Receive Data](indicating-rss-receive-data.md).

 

 





