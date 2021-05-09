---
title: OID_GEN_XMIT_ERROR
description: As a query, the OID_GEN_XMIT_ERROR OID specifies the number of frames that a NIC fails to transmit.
ms.date: 11/01/2019
keywords: 
 -OID_GEN_XMIT_ERROR Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_XMIT\_ERROR


As a query, the OID\_GEN\_XMIT\_ERROR OID specifies the number of frames that a NIC fails to transmit.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Not requested. Use [OID\_GEN\_STATISTICS](oid-gen-statistics.md) instead.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

## Remarks

The count is identical to the *ifOutErrors* counter described in RFC 2863.

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

 

