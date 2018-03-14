---
title: NDIS_NBL_GET_MEDIA_SPECIFIC_INFO macro
author: windows-driver-content
description: The NDIS_NBL_GET_MEDIA_SPECIFIC_INFO macro gets a media-specific information data structure from a linked list of such structures that are associated with a NET_BUFFER_LIST structure.
ms.assetid: 44054921-4ddc-4102-9840-bb069b59d2ae
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_NBL_GET_MEDIA_SPECIFIC_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO macro


The NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO macro gets a media-specific information data structure from a linked list of such structures that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_NBL_GET_MEDIA_SPECIFIC_INFO(
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
A unique pre-assigned value that identifies the type of the media-specific information. This member is reserved for system use.

New tags can be assigned in future system releases for new media types that require additional OOB data specific to a particular media type.

*\_MediaSpecificInfo*   
A pointer to an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515) structure.

Return value
------------

None.

Remarks
-------

Any NDIS driver can use NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO to get media-specific information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. When this macro returns, the *\_MediaSpecificInfo* parameter contains a pointer to the first [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515) structure in the media-specific information list that has a **Tag** member matching the value specified in the *\_Tag* parameter.

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use [<strong>NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX</strong>](ndis-nbl-get-media-specific-info-ex.md).</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NBL\_GET\_MEDIA\_SPECIFIC\_INFO\_EX**](ndis-nbl-get-media-specific-info-ex.md)

[**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




