---
title: OID_GEN_RCV_LINK_SPEED
ms.topic: reference
description: As a query, use the OID_GEN_RCV_LINK_SPEED OID to determine the receive link speed of a network interface. Version Information Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RCV_LINK_SPEED Network Drivers Starting with Windows Vista
---

# OID\_GEN\_RCV\_LINK\_SPEED


As a query, use the OID\_GEN\_RCV\_LINK\_SPEED OID to determine the receive link speed of a network interface.

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

## Remarks

Only [NDIS network interface](./ndis-network-interfaces2.md) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that indicates the receive link speed of the interface, in bits per second.

## Requirements

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


[NDIS Network Interface OIDs](./ndis-network-interface-oids.md)

 

