---
title: NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO macro
author: windows-driver-content
description: The NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO macro adds a media-specific information data structure to the beginning of a linked list of such structures that are associated with a NET_BUFFER_LIST structure.
ms.assetid: fe6fd49f-90e6-49fd-a430-2cb2fb56c9c5
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO macro


The **NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO** macro adds a media-specific information data structure to the beginning of a linked list of such structures that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO(
   PNET_BUFFER_LIST                     _NBL,
   PNDIS_NBL_MEDIA_SPECIFIC_INFORMATION _MediaSpecificInfo
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_MediaSpecificInfo*   
A pointer to an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515) structure to add to the linked list.

Return value
------------

None.

Remarks
-------

Any NDIS driver can use NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO to add media-specific information to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use [<strong>NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO_EX</strong>](ndis-nbl-add-media-specific-info-ex.md).</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO\_EX**](ndis-nbl-add-media-specific-info-ex.md)

[**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




