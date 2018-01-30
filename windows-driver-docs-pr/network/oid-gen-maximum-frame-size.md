---
title: OID_GEN_MAXIMUM_FRAME_SIZE
author: windows-driver-content
description: As a query, the OID_GEN_MAXIMUM_FRAME_SIZE OID specifies the maximum network packet size, in bytes, that the NIC supports.
ms.assetid: 4c81f3a6-6f66-466d-8d22-67841a5a8320
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_MAXIMUM_FRAME_SIZE Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MAXIMUM_FRAME_SIZE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


