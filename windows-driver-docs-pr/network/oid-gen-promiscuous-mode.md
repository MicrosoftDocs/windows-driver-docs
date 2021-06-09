---
title: OID_GEN_PROMISCUOUS_MODE
description: As a query, use the OID_GEN_PROMISCUOUS_MODE OID to determine whether a network interface is promiscuous or not (ifPromiscuousMode from RFC 2863).
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PROMISCUOUS_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_PROMISCUOUS\_MODE


As a query, use the OID\_GEN\_PROMISCUOUS\_MODE OID to determine whether a network interface is promiscuous or not (*ifPromiscuousMode* from [RFC 2863](https://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

## Remarks

Only [NDIS network interface](./ndis-network-interfaces2.md) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the interface provider returns NDIS\_STATUS\_SUCCESS and if the interface accepts only packets that are addressed to that interface, the result value should be **FALSE**. This value should be **TRUE** if the interface accepts all network packets.

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

 

