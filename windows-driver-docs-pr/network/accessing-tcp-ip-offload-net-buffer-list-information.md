---
title: Accessing TCP/IP Offload NET_BUFFER_LIST Information
description: Accessing TCP/IP Offload NET_BUFFER_LIST Information
ms.assetid: 555c9533-ab3f-43f0-9139-b1de33a6b1a7
keywords:
- TCP/IP offload WDK networking , out-of-band data
- offload WDK TCP/IP transport , out-of-band data WDK TCP/IP offload
- OOB data WDK TCP/IP offload
- NET_BUFFER_LIST
- task offload WDK TCP/IP transport , out-of-band data
- connection offload WDK TCP/IP transport , out-of-band data
ms.date: 10/23/2018
ms.localizationpriority: medium
---

# Accessing TCP/IP Offload NET\_BUFFER\_LIST Information

NDIS versions 6.0 and later provide TCP/IP offload out-of-band (OOB) data in the **NetBufferListInfo** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, which specifies a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. The **NetBufferListInfo** member is an array of values that contain information that is common to all of the NET\_BUFFER structures in the list.

Use the following identifiers with the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro to set and get the TCP/IP offload OOB data in the **NetBufferListInfo** array:

<a href="" id="tcpipchecksumnetbufferlistinfo"></a>**TcpIpChecksumNetBufferListInfo**  
Specifies checksum information that is used in offloading checksum tasks from the TCP/IP protocol to a miniport driver. When you specify **TcpIpChecksumNetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_TCP\_IP\_CHECKSUM\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567877) structure (not a pointer to the structure). This structure contains a union that enables the checksum information to be accessed as a single PVOID value or as bit fields.

<a href="" id="ipsecoffloadv1netbufferlistinfo"></a>**IPsecOffloadV1NetBufferListInfo**  
Specifies Internet protocol security (IPsec) offload information that is used in offloading IPsec tasks from the TCP/IP protocol to a miniport driver. When you specify **IPsecOffloadV1NetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565801) structure.

<a href="" id="tcplargesendnetbufferlistinfo"></a>**TcpLargeSendNetBufferListInfo**  
Specifies information that is used in offloading the segmentation of a large TCP packet from the TCP/IP protocol to a miniport driver. When you specify **TcpLargeSendNetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns an [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) structure (not a pointer to the structure). This structure contains a union that enables the information to be accessed as a single PVOID value or as bit fields.

<a href="" id="ieee8021qnetbufferlistinfo"></a>**Ieee8021QNetBufferListInfo**  
Specifies 802.1Q information about a packet. When you specify **Ieee8021QNetBufferListInfo**, NET\_BUFFER\_LIST\_INFO returns the **Value** member of an [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure. This structure can specify 802.1p priority and virtual LAN (VLAN) identifier information. 802.1p priority information is used to establish packet priority in shared-media 802 networks.

If a miniport driver reports support for the NDIS\_ENCAPSULATION\_IEEE\_802\_3\_P\_AND\_Q\_IN\_OOB encapsulation, it must insert the **Ieee8021QNetBufferListInfo** data into large send offload version 1 (LSOV1) and large send offload version 2 (LSOV2) Ethernet packets.

<a href="" id="tcpoffloadbytestransferred"></a>**TcpOffloadBytesTransferred**  
Specifies the number of data bytes that were transferred in a TCP chimney offload send, receive, or disconnect operation.

<a href="" id="tcpreceivenopush"></a>**TcpReceiveNoPush**  
Specifies a Boolean value that represents the push mode of a TCP chimney offload receive request. If **TRUE**, the receive request is in non-push mode. Otherwise, the receive request is in push mode.

For LSOV1, LSOV2, checksum, and IPsec offload types, a miniport driver performs task offload based on the type of OOB data and the offload capabilities that it reported. For example, if a protocol driver requires LSOV1 services for an IPv4 packet, each send request that the protocol driver provides includes the information from the **LsoV1Transmit** member in the [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) OOB data. Note that the protocol driver must verify that the miniport driver supports IPv4, with the specified encapsulation type, before making the send request.

The NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO structure contains the maximum segment size (MSS). The **TcpHeaderOffset** member specifies the location of the TCP header so that the miniport driver does not have to parse IP headers, IP options, or IP extension headers.

An NDIS 6.0 and later miniport driver that supports LSOV2 and LSOV1 must check the **Type** member of [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567882) to determine whether the driver stack is using LSOV2 or LSOV1 and must perform the appropriate offload.

For LSOv1, before a miniport driver completes the send of a large TCP packet that it has segmented into smaller packets by using LSO, the driver writes the number of TCP payload bytes that it sent in the segmented packets in the **TcpPayload** member of NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_NET\_BUFFER\_LIST\_INFO.

If a miniport driver specifies the NDIS\_ENCAPSULATION\_IEEE\_802\_3\_P\_AND\_Q flag in its capabilities, the driver can perform task offload services for [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures that contain the VLAN header in the buffer data. In the case of received data, this flag indicates that the miniport driver will perform the receive checksum calculation and put the VLAN header in the Ethernet packet.

If a miniport driver specifies the NDIS\_ENCAPSULATION\_IEEE\_802\_3\_P\_AND\_Q\_IN\_OOB flag in its capabilities, the driver can perform offload on NET\_BUFFER\_LIST structures that contain the VLAN header in the **Ieee8021QnetBufferListInfo** OOB data. In the receive checksum offload case, the miniport inserts the VLAN header into the **Ieee8021QnetBufferListInfo** OOB data.

 

 





