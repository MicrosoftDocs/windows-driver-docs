---
title: NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO macro
description: The NDIS\_NBL\_ADD\_MEDIA\_SPECIFIC\_INFO macro adds a media-specific information data structure to the beginning of a linked list of such structures that are associated with a NET\_BUFFER\_LIST structure.
MS-HAID:
- 'ndis\_netbuf\_macros\_ref\_0b881a76-0fb6-4314-a20d-0fd36149adc5.xml'
- 'netvista.ndis\_nbl\_add\_media\_specific\_info'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fe6fd49f-90e6-49fd-a430-2cb2fb56c9c5
keywords: ["NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO
api_location:
- Ndis.h
api_type:
- HeaderDef
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





