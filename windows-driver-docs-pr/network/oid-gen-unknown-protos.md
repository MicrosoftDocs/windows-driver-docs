---
title: OID_GEN_UNKNOWN_PROTOS
description: As a query, use the OID_GEN_UNKNOWN_PROTOS OID to determine the unknown-protocol packet count of a network interface (ifInUnknownProtos from RFC 2863).
ms.assetid: a0bebd8d-c202-41f5-84be-a3056a2eeef9
ms.date: 08/08/2017
keywords: 
 -OID_GEN_UNKNOWN_PROTOS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_UNKNOWN\_PROTOS


As a query, use the OID\_GEN\_UNKNOWN\_PROTOS OID to determine the unknown-protocol packet count of a network interface (*ifInUnknownProtos* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

The unknown-protocol statistics counter specifies the number of packets that were received through the interface that were discarded because the associated protocol was unknown or unsupported.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that specifies the number of packets.

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

 

 




