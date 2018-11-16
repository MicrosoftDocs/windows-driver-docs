---
title: OID_GEN_XMIT_LINK_SPEED
description: As a query, use the OID_GEN_XMIT_LINK_SPEED OID to determine the transmit link speed of a network interface. Version Information Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.assetid: 0a390456-8974-4668-b624-55259c2f9e20
ms.date: 08/08/2017
keywords: 
 -OID_GEN_XMIT_LINK_SPEED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_XMIT\_LINK\_SPEED


As a query, use the OID\_GEN\_XMIT\_LINK\_SPEED OID to determine the transmit link speed of a network interface.

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that indicates the transmit link speed of the interface, in bits per second.

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


[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 




