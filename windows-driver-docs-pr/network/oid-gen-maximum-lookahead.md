---
title: OID_GEN_MAXIMUM_LOOKAHEAD
description: As a query, the OID_GEN_MAXIMUM_LOOKAHEAD OID specifies the maximum number of bytes that the NIC can provide as lookahead data.
ms.assetid: 086581f7-c0a5-4355-82fe-22f53201b540
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAXIMUM_LOOKAHEAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MAXIMUM\_LOOKAHEAD


As a query, the OID\_GEN\_MAXIMUM\_LOOKAHEAD OID specifies the maximum number of bytes that the NIC can provide as lookahead data. This specification does not include a header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

Upper-layer drivers examine lookahead data to determine whether a packet that is associated with the lookahead data is intended for one or more of their clients.

If the underlying driver supports multipacket receive indications, bound protocol drivers are given full net packets on every indication. Consequently, this value is identical to that returned for [OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md).

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


[OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md)

 

 




