---
title: OID_GEN_OPERATIONAL_STATUS
description: As a query, use the OID_GEN_OPERATIONAL_STATUS OID to determine the current operational status of a network interface (ifOperStatus from RFC 2863).
ms.assetid: fa00d449-6ec0-4e72-8d9c-a453a0b1f3e9
ms.date: 08/08/2017
keywords: 
 -OID_GEN_OPERATIONAL_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_OPERATIONAL\_STATUS


As a query, use the OID\_GEN\_OPERATIONAL\_STATUS OID to determine the current operational status of a network interface (*ifOperStatus* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

NDIS handles this OID for miniport adapters and filter modules, and only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers receive this OID query.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568746) enumeration.

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


[**NET\_IF\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568746)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 




