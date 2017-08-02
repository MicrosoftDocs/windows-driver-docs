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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


