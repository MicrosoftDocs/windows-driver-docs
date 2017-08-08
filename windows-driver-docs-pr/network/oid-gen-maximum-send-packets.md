---
title: OID\_GEN\_MAXIMUM\_SEND\_PACKETS
author: windows-driver-content
description: As a query, the OID\_GEN\_MAXIMUM\_SEND\_PACKETS OID specifies the maximum number of send packet descriptors that a miniport driver's MiniportSendPackets function can accept.
ms.assetid: 7e87285f-26c5-4b7d-99a8-bc0f30c643dc
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_MAXIMUM_SEND_PACKETS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_MAXIMUM\_SEND\_PACKETS


As a query, the OID\_GEN\_MAXIMUM\_SEND\_PACKETS OID specifies the maximum number of send packet descriptors that a miniport driver's [*MiniportSendPackets*](https://msdn.microsoft.com/library/windows/hardware/ff550524) function can accept.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS ignores any value returned by a deserialized driver in response to a query of OID\_GEN\_MAXIMUM\_SEND\_PACKETS. NDIS does not adjust the size of the array of packet descriptors that it supplies to a deserialized miniport driver's *MiniportSendPackets* function.

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


[*MiniportSendPackets*](https://msdn.microsoft.com/library/windows/hardware/ff550524)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MAXIMUM_SEND_PACKETS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


