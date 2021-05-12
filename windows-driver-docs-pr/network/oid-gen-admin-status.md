---
title: OID_GEN_ADMIN_STATUS
description: As a query, use the OID_GEN_ADMIN_STATUS OID to determine the administrative status for an interface (ifAdminStatus from RFC 2863).
ms.date: 08/08/2017
keywords: 
 -OID_GEN_ADMIN_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_ADMIN\_STATUS


As a query, use the OID\_GEN\_ADMIN\_STATUS OID to determine the administrative status for an interface (*ifAdminStatus* from [RFC 2863](https://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

## Remarks

The administrative status is the status that the system administrator requested.

Only [NDIS network interface](./ndis-network-interfaces2.md) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_ADMIN\_STATUS**](/windows/win32/api/ifdef/ne-ifdef-net_if_admin_status) enumeration.

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


[**NET\_IF\_ADMIN\_STATUS**](/windows/win32/api/ifdef/ne-ifdef-net_if_admin_status)

[NDIS Network Interface OIDs](./ndis-network-interface-oids.md)

 

