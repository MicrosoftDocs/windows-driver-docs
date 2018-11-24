---
title: OID_GEN_BYTES_XMIT
description: As a query, NDIS and overlying drivers use the OID_GEN_BYTES_XMIT OID to determine the total bytes that a miniport adapter transmitted.
ms.assetid: 95b89a01-39e0-4e13-b960-32923e47a88d
ms.date: 08/08/2017
keywords: 
 -OID_GEN_BYTES_XMIT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_BYTES\_XMIT


As a query, NDIS and overlying drivers use the OID\_GEN\_BYTES\_XMIT OID to determine the total bytes that a miniport adapter transmitted.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

NDIS handles this OID for miniport drivers. See the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID for more information about statistics.

The total byte count is the sum of the transmit-directed byte count, transmit-multicast byte count and transmit-broadcast byte count. This value is the same as the sum of the values that are returned by the [OID\_GEN\_DIRECTED\_BYTES\_XMIT](oid-gen-directed-bytes-xmit.md), [OID\_GEN\_MULTICAST\_BYTES\_XMIT](oid-gen-multicast-bytes-xmit.md), and [OID\_GEN\_BROADCAST\_BYTES\_XMIT](oid-gen-broadcast-bytes-xmit.md) OIDs.

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


[OID\_GEN\_BROADCAST\_BYTES\_XMIT](oid-gen-broadcast-bytes-xmit.md)

[OID\_GEN\_DIRECTED\_BYTES\_XMIT](oid-gen-directed-bytes-xmit.md)

[OID\_GEN\_MULTICAST\_BYTES\_XMIT](oid-gen-multicast-bytes-xmit.md)

[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 




