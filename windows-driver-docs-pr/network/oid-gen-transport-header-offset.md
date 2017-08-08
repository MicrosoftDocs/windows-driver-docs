---
title: OID\_GEN\_TRANSPORT\_HEADER\_OFFSET
author: windows-driver-content
description: As a set, the OID\_GEN\_TRANSPORT\_HEADER\_OFFSET OID indicates the size of additional headers for packets that a particular transport sends and receives.
ms.assetid: 00b00c5b-cdf3-4b87-8914-e87876c9ae23
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_TRANSPORT_HEADER_OFFSET Network Drivers Starting with Windows Vista
---

# OID\_GEN\_TRANSPORT\_HEADER\_OFFSET


As a set, the OID\_GEN\_TRANSPORT\_HEADER\_OFFSET OID indicates the size of additional headers for packets that a particular transport sends and receives.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Optional.

Remarks
-------

A transport informs miniport drivers and other layered drivers of this header size; these drivers can then use this information when processing packets. For example, a driver could use the sublayer header size obtained from the transport to locate the beginning of higher layer information in packets, such as the start of the IP header; the driver could then parse and adjust the fields of the IP protocol header as appropriate. Transports use a TRANSPORT\_HEADER\_OFFSET structure, defined as follows, to indicate this header size.

```
typedef struct _TRANSPORT_HEADER_OFFSET {
  USHORT  ProtocolType; 
  USHORT  HeaderOffset; 
} TRANSPORT_HEADER_OFFSET, *PTRANSPORT_HEADER_OFFSET;
```

The members of this structure contain the following information:

<a href="" id="protocoltype"></a>**ProtocolType**  
Specifies the protocol type that sends this OID and that subsequently sends and receives packets using the specified sublayer header size. The protocol is one of the following values:

<a href="" id="ndis-protocol-id-default"></a>NDIS\_PROTOCOL\_ID\_DEFAULT  
Default protocol

<a href="" id="ndis-protocol-id-tcp-ip"></a>NDIS\_PROTOCOL\_ID\_TCP\_IP  
TCP/IP protocol

<a href="" id="ndis-protocol-id-ipx"></a>NDIS\_PROTOCOL\_ID\_IPX  
NetWare IPX protocol

<a href="" id="ndis-protocol-id-nbf"></a>NDIS\_PROTOCOL\_ID\_NBF  
NetBIOS protocol

<a href="" id="headeroffset"></a>**HeaderOffset**  
Specifies the size, in bytes, of the sublayer header that precedes the protocol header for packets that the protocol subsequently sends to or receives from the miniport driver or other layered driver. For example, sizeof(Ethernet header) + sizeof(SNAP header).

Typically, transports calculate the header size of packets from information that is retrieved from miniport drivers. To request the maximum total packet size in bytes that a NIC supports, including the header, transports use the [OID\_GEN\_MAXIMUM\_TOTAL\_SIZE](oid-gen-maximum-total-size.md) OID. To request the maximum packet size in bytes that a NIC supports, not including a header, transports use the [OID\_GEN\_MAXIMUM\_FRAME\_SIZE](oid-gen-maximum-frame-size.md) OID. To calculate the maximum header size, transports subtract the maximum frame size from the maximum total size.

If a transport transmits packets that contain sublayer header information, the transport must know the sublayer header size of these packets and must inform underlying miniport drivers and other layered drivers about the size so that the drivers can process the packets. Sending and receiving particular sublayer header information within a packet may be an option that can be set in the registry for a particular protocol. Transports could then obtain information about sublayer headers from the registry and pass the header size down to miniport drivers or other layered drivers.

For example, if a transport handles packets from the Fiber Distributed Data Interface medium, the transport must send a set request to underlying miniport drivers and other layered drivers using OID\_GEN\_TRANSPORT\_HEADER\_OFFSET to inform those drivers about the size of the packets' sublayer header. (FDDI is not supported in Windows Vista and later versions of Windows.) These packets from FDDI could contain Logical Link Control (LLC) information. This LLC information could in turn include an LLC header and other headers such as Sub-Network Access Protocol (SNAP). The transport determines from the registry to use LLC/SNAP and passes the header size of the LLC/SNAP segments of packets to miniport drivers.

This OID is optional for miniport drivers and other layered drivers. Because this OID is optional, drivers are not required to respond to requests that transports make using this OID.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_GEN\_MAXIMUM\_FRAME\_SIZE](oid-gen-maximum-frame-size.md)

[OID\_GEN\_MAXIMUM\_TOTAL\_SIZE](oid-gen-maximum-total-size.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_TRANSPORT_HEADER_OFFSET%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


