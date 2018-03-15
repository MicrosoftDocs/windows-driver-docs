---
title: KSPROPERTY\_VIDEODECODER\_VCR\_TIMING
description: The KSPROPERTY\_VIDEODECODER\_VCR\_TIMING property controls whether the VCR is expecting video from a tape source or a broadcast source. This property is optional.
ms.assetid: 66d194e4-df9e-4f8a-9767-414311c205da
keywords: ["KSPROPERTY_VIDEODECODER_VCR_TIMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEODECODER_VCR_TIMING
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_VIDEODECODER\_VCR\_TIMING


The KSPROPERTY\_VIDEODECODER\_VCR\_TIMING property controls whether the VCR is expecting video from a tape source or a broadcast source. This property is optional.

## <span id="ddk_ksproperty_videodecoder_vcr_timing_ks"></span><span id="DDK_KSPROPERTY_VIDEODECODER_VCR_TIMING_KS"></span>


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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY_VIDEODECODER_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566052)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies whether to use VCR timing or broadcast timing. A value of zero indicates a broadcast source. A nonzero value indicates a tape source.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEODECODER\_S structure indicates whether to use VCR timing or broadcast timing.

The timing accuracy of synchronization pulses on tape sources typically is not as accurate as from broadcast sources.

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_VIDEODECODER\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566052)

 

 






