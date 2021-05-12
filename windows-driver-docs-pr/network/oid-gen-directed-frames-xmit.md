---
title: OID_GEN_DIRECTED_FRAMES_XMIT
description: As a query, the OID_GEN_DIRECTED_FRAMES_XMIT OID specifies the number of directed packets that are transmitted without errors.
ms.date: 11/01/2019
keywords: 
 -OID_GEN_DIRECTED_FRAMES_XMIT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_DIRECTED\_FRAMES\_XMIT


As a query, the OID\_GEN\_DIRECTED\_FRAMES\_XMIT OID specifies the number of directed packets that are transmitted without errors.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Not requested. Use [OID\_GEN\_STATISTICS](oid-gen-statistics.md) instead.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

## Remarks

The count is identical to the *ifOutUcastPkts* counter described in RFC 2863.

For general information about statistics OIDs, see [General Statistics](./ndis-general-statistics-oids.md).

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

 

