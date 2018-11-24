---
title: OID_GEN_ALIAS
description: As a query, use the OID_GEN_ALIAS OID to obtain the alias string for an interface (ifAlias from RFC 2863). Version Information Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.assetid: ff5e6494-aa4e-4a0a-b773-64b612236c8c
ms.date: 08/08/2017
keywords: 
 -OID_GEN_ALIAS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_ALIAS


As a query, use the OID\_GEN\_ALIAS OID to obtain the alias string for an interface (*ifAlias* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

An [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) provider can assign unique alias strings for its interfaces. If the name should remain associated with the same interface, the provider can make the strings persistent after the computer restarts and reinitializations.

Only NDIS network interface providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is an alias string that is returned in an NDIS\_IF\_COUNTED\_STRING structure.

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

 

 




