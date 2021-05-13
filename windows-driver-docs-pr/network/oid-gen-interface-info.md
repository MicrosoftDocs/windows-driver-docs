---
title: OID_GEN_INTERFACE_INFO
description: As a query, use the OID_GEN_INTERFACE_INFO OID to obtain the current state and statistics information for a network interface.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_INTERFACE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_INTERFACE\_INFO


As a query, use the OID\_GEN\_INTERFACE\_INFO OID to obtain the current state and statistics information for a network interface.

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

## Remarks

Only [NDIS network interface](./ndis-network-interfaces2.md) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query is an [**NDIS\_INTERFACE\_INFORMATION**](/windows/win32/api/ifdef/ns-ifdef-ndis_interface_information) structure. This structure contains information that changes during the lifetime of the interface.

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


[**NDIS\_INTERFACE\_INFORMATION**](/windows/win32/api/ifdef/ns-ifdef-ndis_interface_information)

[NDIS Network Interface OIDs](./ndis-network-interface-oids.md)

 

