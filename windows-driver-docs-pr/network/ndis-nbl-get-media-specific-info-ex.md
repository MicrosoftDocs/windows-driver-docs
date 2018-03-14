---
title: NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX macro
author: windows-driver-content
description: The NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX macro gets a media-specific information data structure from a linked list of such structures that are associated with a NET_BUFFER_LIST structure.
ms.assetid: 06dce06d-e7ce-466c-86d7-26fced4f5695
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX macro Network Drivers Starting with Windows Vista
---

# NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO\_EX macro


The **NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO\_EX** macro gets a media-specific information data structure from a linked list of such structures that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX(
   PNET_BUFFER_LIST                     _NBL,
   ULONG                                _Tag,
   PNDIS_NBL_MEDIA_SPECIFIC_INFORMATION _MediaSpecificInfo
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_Tag*   
A unique pre-assigned value that identifies the type of the media-specific information.

New tags can be assigned in future system releases for new media types that require additional OOB data specific to a particular media type.

*\_MediaSpecificInfo*   
A pointer to an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518) structure.

Return value
------------

None

Remarks
-------

Any NDIS 6.20 or later driver can use NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO\_EX to get media-specific information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. When this macro returns, the *\_MediaSpecificInfo* parameter contains a pointer to the first [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518) structure in the media-specific information list that has a **Tag** member matching the value specified in the *\_Tag* parameter.

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


[**NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO**](ndis-nbl-get-media-specific-info.md)

[**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff566518)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




