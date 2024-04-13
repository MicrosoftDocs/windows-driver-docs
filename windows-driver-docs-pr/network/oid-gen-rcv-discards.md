---
title: OID_GEN_RCV_DISCARDS
ms.topic: reference
description: As a query, NDIS and overlying drivers use the OID_GEN_RCV_DISCARDS OID to determine the number of receive discards on a miniport adapter.
ms.date: 11/01/2019
keywords: 
 -OID_GEN_RCV_DISCARDS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_RCV\_DISCARDS


As a query, NDIS and overlying drivers use the OID\_GEN\_RCV\_DISCARDS OID to determine the number of receive discards on a miniport adapter.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

## Remarks

NDIS handles this OID for miniport drivers. See the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID for more information about statistics.

The count is identical to the *ifInDiscards* counter described in RFC 2863.

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


[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 




