---
title: KSPROPERTY_VIDEODECODER_VCR_TIMING
description: The KSPROPERTY\_VIDEODECODER\_VCR\_TIMING property controls whether the VCR is expecting video from a tape source or a broadcast source. This property is optional.
keywords: ["KSPROPERTY_VIDEODECODER_VCR_TIMING Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEODECODER_VCR_TIMING
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEODECODER\_VCR\_TIMING


The KSPROPERTY\_VIDEODECODER\_VCR\_TIMING property controls whether the VCR is expecting video from a tape source or a broadcast source. This property is optional.

## <span id="ddk_ksproperty_videodecoder_vcr_timing_ks"></span><span id="DDK_KSPROPERTY_VIDEODECODER_VCR_TIMING_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videodecoder_s" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEODECODER_S&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videodecoder_s)"><strong>KSPROPERTY_VIDEODECODER_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies whether to use VCR timing or broadcast timing. A value of zero indicates a broadcast source. A nonzero value indicates a tape source.

## Remarks

The **Value** member of the KSPROPERTY\_VIDEODECODER\_S structure indicates whether to use VCR timing or broadcast timing.

The timing accuracy of synchronization pulses on tape sources typically is not as accurate as from broadcast sources.

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


[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY\_VIDEODECODER\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_videodecoder_s)

