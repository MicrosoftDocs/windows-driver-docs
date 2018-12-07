---
title: OID_GEN_LAST_CHANGE
description: As a query, use the OID_GEN_LAST_CHANGE OID to determine the time of the last operational state change of a network interface (ifLastChange from RFC 2863).
ms.assetid: bd96d1ec-2fd0-491f-acb4-c1594ce6a084
ms.date: 08/08/2017
keywords: 
 -OID_GEN_LAST_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_LAST\_CHANGE


As a query, use the OID\_GEN\_LAST\_CHANGE OID to determine the time of the last operational state change of a network interface (*ifLastChange* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

This OID returns the time, starting from the last computer restart, when the interface entered its current operational state. For more information about the operational state, see [**NDIS\_STATUS\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567406) and [OID\_GEN\_OPERATIONAL\_STATUS](oid-gen-operational-status.md). To get the current time, an interface provider can call the [**NdisGetSystemUpTimeEx**](https://msdn.microsoft.com/library/windows/hardware/ff562675) function.

If the current operational state was entered before the last reinitialization of the interface, this value should be zero. . If the interface provider does not track operational state change time, the value should be zero.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that specifies the state change time, in milliseconds, since the last computer restart.

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


[OID\_GEN\_OPERATIONAL\_STATUS](oid-gen-operational-status.md)

[**NDIS\_STATUS\_OPER\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567406)

[**NdisGetSystemUpTimeEx**](https://msdn.microsoft.com/library/windows/hardware/ff562675)

[NDIS Network Interface OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566545)

 

 




