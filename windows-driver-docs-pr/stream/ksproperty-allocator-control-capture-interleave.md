---
title: KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE
description: The KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE property informs the Overlay Mixer if interleaved capture is possible.
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE


The KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE property informs the Overlay Mixer if interleaved capture is possible.

## <span id="ddk_ksproperty_allocator_control_capture_interleave_ks"></span><span id="DDK_KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s)"><strong>KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG the specifies whether interleaved capture is possible.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_allocator_control_capture_interleave_s)

