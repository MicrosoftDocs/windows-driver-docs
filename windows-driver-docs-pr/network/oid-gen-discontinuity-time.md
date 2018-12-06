---
title: OID_GEN_DISCONTINUITY_TIME
description: As a query, use the OID_GEN_DISCONTINUITY_TIME OID to determine the discontinuity time of a network interface (ifCounterDiscontinuityTime from RFC 2863).
ms.assetid: 3eac6818-c346-47f6-b812-f98b808dc36a
ms.date: 08/08/2017
keywords: 
 -OID_GEN_DISCONTINUITY_TIME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_DISCONTINUITY\_TIME


As a query, use the OID\_GEN\_DISCONTINUITY\_TIME OID to determine the discontinuity time of a network interface (*ifCounterDiscontinuityTime* from [RFC 2863](http://go.microsoft.com/fwlink/p/?linkid=84054)).

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

Remarks
-------

Only [NDIS network interface](https://msdn.microsoft.com/library/windows/hardware/ff566527) providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

This OID returns the time, starting from the last computer restart, when the interface had a discontinuity in maintaining the statistics counters. For example, there was a discontinuity because the interface was disabled or the associated adapter was removed from the computer. For more information about the statistics counters, see [OID\_GEN\_STATISTICS](oid-gen-statistics.md). To get the current time, an interface provider can call the [**NdisGetSystemUpTimeEx**](https://msdn.microsoft.com/library/windows/hardware/ff562675) function.

If no such discontinuity occurred since the last re-initialization of the interface this value should be zero. If the interface provider does not track discontinuity time, this value should be zero.

If the interface provider returns NDIS\_STATUS\_SUCCESS, the result of the query is a ULONG64 value that specifies the discontinuity time, in milliseconds, since the last computer restart.

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

 

 




