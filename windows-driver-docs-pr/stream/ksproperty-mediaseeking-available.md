---
title: KSPROPERTY\_MEDIASEEKING\_AVAILABLE
description: The KSPROPERTY\_MEDIASEEKING\_AVAILABLE property retrieves the media time span that is currently available on a filter.
ms.assetid: df59f32e-2783-418d-85b9-f9285034c6fa
keywords: ["KSPROPERTY_MEDIASEEKING_AVAILABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MEDIASEEKING_AVAILABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_MEDIASEEKING\_AVAILABLE


The KSPROPERTY\_MEDIASEEKING\_AVAILABLE property retrieves the media time span that is currently available on a filter.

## <span id="ddk_ksproperty_mediaseeking_available_ks"></span><span id="DDK_KSPROPERTY_MEDIASEEKING_AVAILABLE_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSPROPERTY_MEDIAAVAILABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565178)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The media time span is the duration that within which a client can seek.

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

## <span id="see_also"></span>See also


[**KSPROPERTY\_MEDIAAVAILABLE**](https://msdn.microsoft.com/library/windows/hardware/ff565178)

[KSPROPSETID\_MediaSeeking](kspropsetid-mediaseeking.md)

 

 






