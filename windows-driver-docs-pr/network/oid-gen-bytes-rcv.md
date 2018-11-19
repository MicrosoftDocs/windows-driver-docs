---
title: OID_GEN_BYTES_RCV
description: As a query, NDIS and overlying drivers use the OID_GEN_BYTES_RCV OID to determine the total number of bytes that a miniport adapter received.
ms.assetid: e613e155-e4ff-48e4-8087-20ecad3c4644
ms.date: 08/08/2017
keywords: 
 -OID_GEN_BYTES_RCV Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_BYTES\_RCV


As a query, NDIS and overlying drivers use the OID\_GEN\_BYTES\_RCV OID to determine the total number of bytes that a miniport adapter received.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

NDIS handles this OID for miniport drivers. See the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID for more information about statistics.

The total byte count is the sum of the receive-directed byte count, receive-multicast byte count and receive-broadcast byte count. This value is the same as the sum of the values that are returned by the [OID\_GEN\_DIRECTED\_BYTES\_RCV](oid-gen-directed-bytes-rcv.md), [OID\_GEN\_MULTICAST\_BYTES\_RCV](oid-gen-multicast-bytes-rcv.md), and [OID\_GEN\_BROADCAST\_BYTES\_RCV](oid-gen-broadcast-bytes-rcv.md) OIDs.

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


[OID\_GEN\_BROADCAST\_BYTES\_RCV](oid-gen-broadcast-bytes-rcv.md)

[OID\_GEN\_DIRECTED\_BYTES\_RCV](oid-gen-directed-bytes-rcv.md)

[OID\_GEN\_MULTICAST\_BYTES\_RCV](oid-gen-multicast-bytes-rcv.md)

[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 




