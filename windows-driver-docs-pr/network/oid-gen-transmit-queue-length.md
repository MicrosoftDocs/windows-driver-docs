---
title: OID_GEN_TRANSMIT_QUEUE_LENGTH
description: As a query, the OID_GEN_TRANSMIT_QUEUE_LENGTH OID specifies the number of packets that are currently queued for transmission, whether on the NIC or in a driver-internal queue.
ms.assetid: 042a7df3-a204-45f8-b147-96def7438b4a
ms.date: 08/08/2017
keywords: 
 -OID_GEN_TRANSMIT_QUEUE_LENGTH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_TRANSMIT\_QUEUE\_LENGTH


As a query, the OID\_GEN\_TRANSMIT\_QUEUE\_LENGTH OID specifies the number of packets that are currently queued for transmission, whether on the NIC or in a driver-internal queue.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Optional.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Optional.

Remarks
-------

For queries, the number returned is always the total number of packets currently queued. This number can include unsubmitted send requests queued in the NDIS library.

For general information about statistics OIDs, see [General Statistics](https://msdn.microsoft.com/library/windows/hardware/ff552485).

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

 

 




