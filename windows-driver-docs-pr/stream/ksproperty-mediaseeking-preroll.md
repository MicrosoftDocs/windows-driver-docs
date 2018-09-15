---
title: KSPROPERTY\_MEDIASEEKING\_PREROLL
description: The KSPROPERTY\_MEDIASEEKING\_PREROLL property retrieves the amount of preroll in 100-nanosecond units required on a filter.
ms.assetid: 3b9a5458-b26a-452b-b7aa-7bbb30c3d631
keywords: ["KSPROPERTY_MEDIASEEKING_PREROLL Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_PREROLL
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

# KSPROPERTY\_MEDIASEEKING\_PREROLL


The KSPROPERTY\_MEDIASEEKING\_PREROLL property retrieves the amount of preroll in 100-nanosecond units required on a filter.

## <span id="ddk_ksproperty_mediaseeking_preroll_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_PREROLL_KS"></span>


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
<td><p>LONGLONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns the number of 100-nanosecond units of preroll as a value of type LONGLONG.

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

 

 






