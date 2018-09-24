---
title: KSPROPERTY\_MEDIASEEKING\_FORMATS
description: The KSPROPERTY\_MEDIASEEKING\_FORMATS property retrieves the media time formats supported by a filter. This information is returned as a multiple item property.
ms.assetid: 6d01737e-baef-4a65-90c7-3838cb19b4c9
keywords: ["KSPROPERTY_MEDIASEEKING_FORMATS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_FORMATS
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_MEDIASEEKING\_FORMATS


The KSPROPERTY\_MEDIASEEKING\_FORMATS property retrieves the media time formats supported by a filter. This information is returned as a multiple item property.

## <span id="ddk_ksproperty_mediaseeking_formats_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_FORMATS_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)</p></td>
<td><p>PVOID</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property can return a multiple item property. The requester is responsible for supplying a buffer of adequate size.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[KSPROPSETID\_MediaSeeking](kspropsetid-mediaseeking.md)

 

 






