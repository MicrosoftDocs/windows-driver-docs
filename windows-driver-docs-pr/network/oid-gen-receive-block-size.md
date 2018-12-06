---
title: OID_GEN_RECEIVE_BLOCK_SIZE
description: As a query.
ms.assetid: 92a7a388-4a41-41cf-96e5-a65b5559553d
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RECEIVE_BLOCK_SIZE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RECEIVE\_BLOCK\_SIZE


As a query. the OID\_GEN\_RECEIVE\_BLOCK\_SIZE OID specifies the amount of storage, in bytes, that a single packet occupies in the receive buffer space of the NIC.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The OID\_GEN\_RECEIVE\_BLOCK\_SIZE OID specifies the amount of storage, in bytes, that a single packet occupies in the receive buffer space of a NIC.

The same information can be obtained from the current and maximum *lookahead* size. However, one of these OIDs can be mandatory to verify each other. Also protocol drivers can determine if the underlying driver indicates full-packet receives by comparing the values that driver returns for the [OID\_GEN\_CURRENT\_LOOKAHEAD](oid-gen-current-lookahead.md) and OID\_GEN\_RECEIVE\_BLOCK\_SIZE OIDs.

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


[OID\_GEN\_CURRENT\_LOOKAHEAD](oid-gen-current-lookahead.md)

 

 




