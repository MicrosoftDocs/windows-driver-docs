---
title: OID_GEN_XMIT_DISCARDS
description: As a query, NDIS and overlying drivers use the OID_GEN_XMIT_DISCARDS OID to determine the number of transmit discards on a miniport adapter.
ms.assetid: f6265262-c485-441c-bb89-fa1d302608d2
ms.date: 08/08/2017
keywords: 
 -OID_GEN_XMIT_DISCARDS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_XMIT\_DISCARDS


As a query, NDIS and overlying drivers use the OID\_GEN\_XMIT\_DISCARDS OID to determine the number of transmit discards on a miniport adapter.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

Remarks
-------

NDIS handles this OID for miniport drivers. See the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID for more information about statistics.

The count that this OID returns is the number of packets that is discarded by the interface.

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

 

 




