---
title: OID_GEN_MEDIA_IN_USE
description: As a query, the OID_GEN_MEDIA_IN_USE OID specifies a complete list of the media types that the NIC currently uses.
ms.assetid: 3b8db63d-07e0-4a5c-9848-57e594e3dd54
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MEDIA_IN_USE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MEDIA\_IN\_USE


As a query, the OID\_GEN\_MEDIA\_IN\_USE OID specifies a complete list of the media types that the NIC currently uses.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

This OID provides the same information as the [OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md) OID.

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


[OID\_GEN\_MEDIA\_SUPPORTED](oid-gen-media-supported.md)

 

 




