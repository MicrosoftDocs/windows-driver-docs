---
title: OID_GEN_MAXIMUM_FRAME_SIZE
description: As a query, the OID_GEN_MAXIMUM_FRAME_SIZE OID specifies the maximum network packet size, in bytes, that the NIC supports.
ms.assetid: 4c81f3a6-6f66-466d-8d22-67841a5a8320
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAXIMUM_FRAME_SIZE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MAXIMUM\_FRAME\_SIZE


As a query, the OID\_GEN\_MAXIMUM\_FRAME\_SIZE OID specifies the maximum network packet size, in bytes, that the NIC supports. This specification does not include a header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not Requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The miniport driver supplies the maximum frame size during initialization and during a restart. NDIS handles this OID query for NDIS 6.0 and later miniport drivers.

In response to this query from requesting transports, the miniport driver should indicate the maximum frame size that the transports can send, excluding the header. A miniport driver that emulates another medium type for binding to a transport must ensure that the maximum frame size for a protocol-supplied net packet does not exceed the size limitations for the true network medium. The same is true for a miniport driver that supports a NIC that requires inserting fields in frames. For example, to determine the maximum transfer unit (MTU), transports send this query to a NIC.

If the miniport driver supports 802.1p packet priority and 802.1Q virtual LAN (VLAN) tags, based on prior actions, if the miniport driver expects that frames must traverse old networks before priority values are removed, that miniport driver might indicate a smaller value in response to this query.

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

 

 




