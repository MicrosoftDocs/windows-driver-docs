---
title: OID_GEN_RCV_OK
ms.topic: reference
description: As a query, the OID_GEN_RCV_OK OID specifies the number of frames that the NIC receives without errors and indicates to bound protocols.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RCV_OK Network Drivers Starting with Windows Vista
---

# OID\_GEN\_RCV\_OK


As a query, the OID\_GEN\_RCV\_OK OID specifies the number of frames that the NIC receives without errors and indicates to bound protocols.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Mandatory.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

## Remarks

OID\_GEN\_RCV\_OK specifies the number of frames that are received without errors. However, the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) does not include this information.

NOTE: Statistics OIDs are mandatory for NDIS 6.0 and later miniport drivers unless NDIS handles them. For general information about statistics OIDs, see [General Statistics](./ndis-general-statistics-oids.md).

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

 

