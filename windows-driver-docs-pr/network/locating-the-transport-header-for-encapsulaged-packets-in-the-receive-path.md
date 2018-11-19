---
title: Locating the Transport Header for Received Encapsulated Packets
description: Locating the Transport Header for Encapsulated Packets in the Receive Path
ms.assetid: D3BDE575-C9EB-49E3-9B61-FDB99B68ED8E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Locating the Transport Header for Encapsulated Packets in the Receive Path

On receiving a packet, a NIC that supports [Network Virtualization using Generic Routing Encapsulation (NVGRE)](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) must first determine whether the packet is encapsulated and, if so, the type of encapsulation.

**Note**  In the send path, a packet is encapsulated if [**NDIS\_TCP\_SEND\_OFFLOADS\_SUPPLEMENTAL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/jj991957).**IsEncapsulatedPacket** is **TRUE**.
 

In the receive path, the NIC must determine whether the packet is encapsulated by checking the protocol number in the **Protocol** field of the IPv4 tunnel (outer) header or the **NextHeader** field of the IPv6 tunnel (outer) header. The list of assigned protocol numbers can be found at <http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xml>.

Once a packet is determined to be an encapsulated packet, the NIC must determine the offset to the transport (inner) IP header by parsing the encapsulated packet's protocol.

For NDIS 6.30 (Windows Server 2012) and later, only GRE IP encapsulation is supported. So the NIC should be able to parse the following, depending on the advertised capabilities:

-   GRE ([RFC 2784: Generic Routing Encapsulation (GRE)](http://tools.ietf.org/html/rfc2784)) headers
-   [RFC 2890: Key and Sequence Number Extensions to GRE](http://tools.ietf.org/html/rfc2890)
-   IPv4 ([RFC 791: Internet Protocol](http://tools.ietf.org/html/rfc791)) headers
-   IPv6 ([RFC 2460: Internet Protocol, Version 6 (IPv6)](http://tools.ietf.org/html/rfc2460)) headers

If the NIC finds an unknown or unsupported encapsulation protocol, it must pass the packet unchanged to the host stack.

Thus, on the receive path, the miniport must parse the transport (inner) IP header to determine the IP version as well as to get to the TCP or UDP header. This is a new requirement for NDIS 6.30 (Windows Server 2012) and later.

 

 





