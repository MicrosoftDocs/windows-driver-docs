---
title: NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX macro
author: windows-driver-content
description: The NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX macro removes a media-specific information data structure from a linked list of such structures that are associated with a NET_BUFFER_LIST structure.
ms.assetid: e03f2322-e40b-46ea-b9d4-e58c1e44a564
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
- NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX macro Network Drivers Starting with Windows Vista
---

# NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX macro


The **NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX** macro removes a media-specific information data structure from a linked list of such structures that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX(
   PNET_BUFFER_LIST                     _NBL,
   PNDIS_NBL_MEDIA_SPECIFIC_INFORMATION _MediaSpecificInfo
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_MediaSpecificInfo*   
A pointer to an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518) structure that has a **Tag** member that matches the **Tag** member of the information structure that should be removed.

Return value
------------

None

Remarks
-------

Any NDIS 6.20 or later driver can use NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX to remove media-specific information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




