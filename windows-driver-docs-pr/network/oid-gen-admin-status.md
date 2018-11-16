---
title: OID_GEN_ADMIN_STATUS
description: As a query, use the OID_GEN_ADMIN_STATUS OID to determine the administrative status for an interface (ifAdminStatus from RFC 2863).
ms.assetid: e8f45521-7419-4c11-b84b-36d4d3306fc2
ms.date: 08/08/2017
keywords: 
 -OID_GEN_ADMIN_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_ADMIN\_STATUS


As a query, use the OID\_GEN\_ADMIN\_STATUS OID to determine the administrative status for an interface (*ifAdminStatus* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

The administrative status is the status that the system administrator requested.

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_ADMIN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568740) enumeration.

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


[**NET\_IF\_ADMIN\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568740)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 




