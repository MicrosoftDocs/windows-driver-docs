---
title: NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX macro
description: The NDIS\_NBL\_REMOVE\_MEDIA\_SPECIFIC\_INFO\_EX macro removes a media-specific information data structure from a linked list of such structures that are associated with a NET\_BUFFER\_LIST structure.
MS-HAID:
- 'ndis\_netbuf\_macros\_media\_specific\_53a0a936-8ca8-42c4-95c9-86c1d86c40ef.xml'
- 'netvista.ndis\_nbl\_remove\_media\_specific\_info\_ex'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e03f2322-e40b-46ea-b9d4-e58c1e44a564
keywords: ["NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX
api_location:
- Ndis.h
api_type:
- HeaderDef
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





