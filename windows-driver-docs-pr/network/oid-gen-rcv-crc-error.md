---
title: OID_GEN_RCV_CRC_ERROR
description: As a query, the OID_GEN_RCV_CRC_ERROR OID specifies the number of frames that are received with checksum errors.
ms.assetid: dfa5e568-2b0a-4b26-8100-06ea8b0f1a71
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RCV_CRC_ERROR Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RCV\_CRC\_ERROR


As a query, the OID\_GEN\_RCV\_CRC\_ERROR OID specifies the number of frames that are received with checksum errors.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Not requested.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

Remarks
-------

The value for the [OID\_GEN\_RCV\_DISCARDS](oid-gen-rcv-discards.md) OID includes CRC errors. For general information about statistics OIDs, see [General Statistics](https://msdn.microsoft.com/library/windows/hardware/ff552485).

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


[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 




