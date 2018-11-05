---
title: RSS Hashing Types
description: RSS Hashing Types
ms.assetid: 21ea384c-5fe2-46c1-9e01-30513f505672
keywords:
- receive-side scaling WDK networking , hash
- RSS WDK networking , hash
- hash WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RSS Hashing Types

## Overview

The RSS hashing type specifies the portion of received network data that a NIC must use to calculate an RSS hash value.

Overlying drivers set the hash type, function, and indirection table. The hash type that the overlying driver sets can be a subset of the type that the miniport driver can support. For more information, see [RSS Configuration](rss-configuration.md).

The hash type is an OR of valid combinations of the following flags:

- NDIS_HASH_IPV4
- NDIS_HASH_TCP_IPV4
- NDIS_HASH_UDP_IPV4
- NDIS_HASH_IPV6
- NDIS_HASH_TCP_IPV6
- NDIS_HASH_UDP_IPV6
- NDIS_HASH_IPV6_EX
- NDIS_HASH_TCP_IPV6_EX
- NDIS_HASH_UDP_IPV6_EX

These are the sets of valid flag combinations:

- IPv4 (combinations of NDIS_HASH_IPV4, NDIS_HASH_TCP_IPV4, and NDIS_HASH_UDP_IPV4)
- IPv6 (combinations of NDIS_HASH_IPV6, NDIS_HASH_TCP_IPV6, and NDIS_HASH_UDP_IPV6)
- IPv6 with extension headers (combinations of NDIS_HASH_IPV6_EX, NDIS_HASH_TCP_IPV6_EX, and NDIS_HASH_UDP_IPV6_EX)

A NIC must support one of the combinations from the IPv4 set. The other sets and combinations are optional. A NIC can support more than one set at a time. In this case, the type of data received determines which hash type the NIC uses.

In general, if the NIC cannot interpret the received data correctly, it must not compute the hash value. For example, if the NIC only supports IPv4 and it receives an IPv6 packet, which it cannot interpret correctly, it must not compute the hash value. If the NIC receives a packet for a transport type that it does not support, it must not compute the hash value. For example, if the NIC receives a UDP packet when it is supposed to be calculating hash values for TCP packets, it must not compute the hash value. In this case, the packet is processed as in the non-RSS case. For more information about the non-RSS receive processing, see [Non-RSS Receive Processing](non-rss-receive-processing.md).

## IPv4 hash type combinations

The valid hash type combinations in the IPv4 set are:

- [NDIS_HASH_IPV4](#ndishashipv4)
- [NDIS_HASH_TCP_IPV4](#ndishashtcpipv4)
- [NDIS_HASH_UDP_IPV4](#ndishashudpipv4)
- [NDIS_HASH_TCP_IPV4 | NDIS_HASH_IPV4](#ndishashtcpipv4--ndishashipv4)
- [NDIS_HASH_UDP_IPV4 | NDIS_HASH_IPV4](#ndishashudpipv4--ndishashipv4)
- [NDIS_HASH_TCP_IPV4 | NDIS_HASH_UDP_IPV4 | NDIS_HASH_IPV4](#ndishashtcpipv4--ndishashudpipv4--ndishashipv4)

### NDIS_HASH_IPV4  

If this flag alone is set, the NIC should compute the hash value over the following IPv4 header fields:

- Source-IPv4-Address
- Destination-IPv4-Address

>[!NOTE]
> If a NIC receives a packet that has both IP and TCP headers, NDIS_HASH_TCP_IPV4 should not always be used. In the case of a fragmented IP packet, NDIS_HASH_IPV4 must be used. This includes the first fragment which contains both IP and TCP headers.

### NDIS_HASH_TCP_IPV4

If this flag alone is set, the NIC should parse the received data to identify an IPv4 packet that contains a TCP segment.

The NIC must identify and skip over any IP options that are present. If the NIC cannot skip over any IP options, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

- Source-IPv4-Address
- Destination-IPv4-Address
- Source TCP Port
- Destination TCP Port

### NDIS_HASH_UDP_IPV4

If this flag alone is set, the NIC should parse the received data to identify an IPv4 packet that contains a UDP datagram.

The NIC must identify and skip over any IP options that are present. If the NIC cannot skip over any IP options, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

- Source-IPv4-Address
- Destination-IPv4-Address
- Source UDP Port
- Destination UDP Port

### NDIS_HASH_TCP_IPV4 | NDIS_HASH_IPV4

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_TCP_IPV4 case. However, if the packet does not contain a TCP header, the NIC should compute the hash value as specified for the NDIS_HASH_IPV4 case.

### NDIS_HASH_UDP_IPV4 | NDIS_HASH_IPV4

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_UDP_IPV4 case. However, if the packet does not contain a UDP header, the NIC should compute the hash value as specified for the NDIS_HASH_IPV4 case.

### NDIS_HASH_TCP_IPV4 | NDIS_HASH_UDP_IPV4 | NDIS_HASH_IPV4

If this flag combination is set, the NIC should perform the hash calculation as specified by the transport in the packet. However, if the packet does not contain a TCP or UDP header, the NIC should compute the hash value as specified for the NDIS_HASH_IPV4 case.

## IPv6 hash type combinations

The valid hash type combinations in the IPv6 set are:

- [NDIS_HASH_IPV6](#ndishashipv6)
- [NDIS_HASH_TCP_IPV6](#ndishashtcpipv6)
- [NDIS_HASH_UDP_IPV6](#ndishashudpipv6)
- [NDIS_HASH_TCP_IPV6 | NDIS_HASH_IPV6](#ndishashtcpipv6--ndishashipv6)
- [NDIS_HASH_UDP_IPV6 | NDIS_HASH_IPV6](#ndishashudpipv6--ndishashipv6)
- [NDIS_HASH_TCP_IPV6 | NDIS_HASH_UDP_IPV6 | NDIS_HASH_IPV6](#ndishashtcpipv6--ndishashudpipv6--ndishashipv6)

### NDIS_HASH_IPV6

If this flag alone is set, the NIC should compute the hash over the following fields:

- Source-IPv6-Address
- Destination-IPv6-Address

### NDIS_HASH_TCP_IPV6

If this flag alone is set, the NIC should parse the received data to identify an IPv6 packet that contains a TCP segment. The NIC must identify and skip over any IPv6 extension headers that are present in the packet. If the NIC cannot skip over any IPv6 extension headers, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

- Source-IPv6 -Address
- Destination-IPv6 -Address
- Source TCP Port
- Destination TCP Port

### NDIS_HASH_UDP_IPV6

If this flag alone is set, the NIC should parse the received data to identify an IPv6 packet that contains a UDP datagram. The NIC must identify and skip over any IPv6 extension headers that are present in the packet. If the NIC cannot skip over any IPv6 extension headers, it should not calculate a hash value.

The NIC should compute the hash value over the following fields:

- Source-IPv6-Address
- Destination-IPv6-Address
- Source UDP Port
- Destination UDP Port

### NDIS_HASH_TCP_IPV6 | NDIS_HASH_IPV6

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_TCP_IPV6 case. However, if the packet does not contain a TCP header, the NIC should compute the hash as specified for the NDIS_HASH_IPV6 case.

### NDIS_HASH_UDP_IPV6 | NDIS_HASH_IPV6

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_UDP_IPV6 case. However, if the packet does not contain a UDP header, the NIC should compute the hash as specified for the NDIS_HASH_IPV6 case.

### NDIS_HASH_TCP_IPV6 | NDIS_HASH_UDP_IPV6 | NDIS_HASH_IPV6

If this flag combination is set, the NIC should perform the hash calculation as specified by the transport in the packet. However, if the packet does not contain a TCP or UDP header, the NIC should compute the hash value as specified in the NDIS_HASH_IPV6 case.

## IPv6 with extension headers hash type combinations

The valid combinations in the IPv6 with extension headers set are:

- [NDIS_HASH_IPV6_EX](#ndishashipv6ex)
- [NDIS_HASH_TCP_IPV6_EX](#ndishashtcpipv6ex)
- [NDIS_HASH_UDP_IPV6_EX](#ndishashudpipv6ex)
- [NDIS_HASH_TCP_IPV6_EX | NDIS_HASH_IPV6_EX](#ndishashtcpipv6ex--ndishashipv6ex)
- [NDIS_HASH_UDP_IPV6_EX | NDIS_HASH_IPV6_EX](#ndishashudpipv6ex--ndishashipv6ex)
- [NDIS_HASH_TCP_IPV6_EX | NDIS_HASH_UDP_IPV6_EX | NDIS_HASH_IPV6_EX](#ndishashtcpipv6ex--ndishashudpipv6ex--ndishashipv6ex)

### NDIS_HASH_IPV6_EX  

If this flag alone is set, the NIC should compute the hash over the following fields:

- Home address from the home address option in the IPv6 destination options header. If the extension header is not present, use the Source IPv6 Address.
- IPv6 address that is contained in the Routing-Header-Type-2 from the associated extension header. If the extension header is not present, use the Destination IPv6 Address.

### NDIS_HASH_TCP_IPV6_EX

If this flag alone is set, the NIC should compute the hash over the following fields:

- Home address from the home address option in the IPv6 destination options header. If the extension header is not present, use the Source IPv6 Address.
- IPv6 address that is contained in the Routing-Header-Type-2 from the associated extension header. If the extension header is not present, use the Destination IPv6 Address.
- Source TCP Port
- Destination TCP Port

### NDIS_HASH_UDP_IPV6_EX

If this flag alone is set, the NIC should compute the hash over the following fields:

- Home address from the home address option in the IPv6 destination options header. If the extension header is not present, use the Source IPv6 Address.
- IPv6 address that is contained in the Routing-Header-Type-2 from the associated extension header. If the extension header is not present, use the Destination IPv6 Address.
- Source UDP Port
- Destination UDP Port

### NDIS_HASH_TCP_IPV6_EX | NDIS_HASH_IPV6_EX

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_TCP_IPV6_EX case. However, if the packet does not contain a TCP header, the NIC should compute the hash as specified for the NDIS_HASH_IPV6_EX case.

### NDIS_HASH_UDP_IPV6_EX | NDIS_HASH_IPV6_EX

If this flag combination is set, the NIC should perform the hash calculations as specified for the NDIS_HASH_UDP_IPV6_EX case. However, if the packet does not contain a UDP header, the NIC should compute the hash as specified for the NDIS_HASH_IPV6_EX case.

### NDIS_HASH_TCP_IPV6_EX | NDIS_HASH_UDP_IPV6_EX | NDIS_HASH_IPV6_EX

If this flag combination is set, the NIC should perform the hash calculations as specified by the packet transport. However, if the packet does not contain a TCP or UDP header, the NIC should compute the hash as specified for the NDIS_HASH_IPV6_EX case.

> [!NOTE]
> If a miniport driver reports NDIS_RSS_CAPS_HASH_TYPE_TCP_IPV6_EX and/or NDIS_RSS_CAPS_HASH_TYPE_UDP_IPV6_EX capability for a NIC, the NIC must calculate hash values (over fields in the IPv6 extension headers) in accordance with the IPv6 extension hash types that the protocol driver set. The NIC can store either the extension hash type or the regular hash type in the NET_BUFFER_LIST structure of the IPv6 packet for which a hash value is computed. 

A miniport driver sets the hash type in a [**NET_BUFFER_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure before indicating the received data. For more information, see [Indicating RSS Receive Data](indicating-rss-receive-data.md).

 

 





