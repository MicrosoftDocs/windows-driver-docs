---
title: NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO macro
author: windows-driver-content
description: The NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO macro removes a media-specific information data structure from a linked list of such structures that are associated with a NET\_BUFFER\_LIST structure.
ms.assetid: 70aeef03-208b-4d09-9e0a-dd3571367ae5
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO macro


The NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO macro removes a media-specific information data structure from a linked list of such structures that are associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO(
   PNET_BUFFER_LIST                     _NBL,
   PNDIS_NBL_MEDIA_SPECIFIC_INFORMATION _MediaSpecificInfo
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_MediaSpecificInfo*   
A pointer to an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515) structure that has a **Tag** member matching the **Tag** member of the information structure that should be removed.

Return value
------------

None.

Remarks
-------

Any NDIS driver can use NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO to remove an [**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515) structure from a list of media-specific information. To specify the type information to remove, specify an NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION structure with a matching **Tag** member in the *\_MediaSpecificInfo* parameter.

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
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use [<strong>NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX</strong>](ndis-nbl-remove-media-specific-info-ex.md).</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NBL\_MEDIA\_SPECIFIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff566515)

[**NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX**](ndis-nbl-remove-media-specific-info-ex.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


