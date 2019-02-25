---
title: OID_GEN_MAXIMUM_TOTAL_SIZE
description: As a query, the OID_GEN_MAXIMUM_TOTAL_SIZE OID specifies the maximum total packet length, in bytes, the NIC supports.
ms.assetid: 4973b4bd-58a5-4242-b33f-1ff8c3a7ec4b
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAXIMUM_TOTAL_SIZE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MAXIMUM\_TOTAL\_SIZE


As a query, the OID\_GEN\_MAXIMUM\_TOTAL\_SIZE OID specifies the maximum total packet length, in bytes, the NIC supports. This specification includes the header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The returned length specifies the largest packet size for the underlying medium. Thus, the returned length depends on the particular medium. A protocol driver might use this returned length as a gauge to determine the maximum size packet that a miniport driver could forward to the protocol driver. If the protocol driver preallocates buffers, it allocates buffers accordingly. The returned length also specifies the largest packet that a protocol driver can pass to the [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) function.

If the miniport driver for a NIC enables [802.1p packet priority](https://msdn.microsoft.com/library/windows/hardware/ff562331)(that is, the miniport driver specifies the NDIS\_MAC\_OPTION\_8021P\_PRIORITY bit in the [OID\_GEN\_MAC\_OPTIONS](oid-gen-mac-options.md) OID bitmask), then the miniport driver must specify its maximum total packet length as 4 bytes less than the maximum size of packets received or sent over the network. For example, if a NIC that has 802.1p packet priority enabled receives and sends packets on the wire that are 1514 bytes in length, the miniport driver for the NIC must report its maximum total packet length as 1510 bytes. The miniport driver must never indicate up to the bound protocol driver packets received over the network that are longer than the packet size specified by OID\_GEN\_MAXIMUM\_TOTAL\_SIZE. That is, even if the miniport driver receives packets over the network that are not marked with priority values but are still the maximum size that the underlying medium supports, the miniport driver can only indicate up packets that are no longer than the size specified by OID\_GEN\_MAXIMUM\_TOTAL\_SIZE.

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


[**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535)

[OID\_GEN\_MAC\_OPTIONS](oid-gen-mac-options.md)

 

 




