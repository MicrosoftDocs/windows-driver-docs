---
title: KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE
description: The KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE property controls the three-state output of video decoders that reside on a shared video port bus. This property is optional.
keywords: ["KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
---

# KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE


The KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE property controls the three-state output of video decoders that reside on a shared video port bus. This property is optional.

## <span id="ddk_ksproperty_videodecoder_output_enable_ks"></span><span id="DDK_KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE_KS"></span>


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

 

The property value (operation data) is a ULONG that specifies the three-state output enable setting. A value of zero indicates three-state output. A nonzero value indicates that the device is actively driving the video port bus.

## Remarks

The **Value** member of the KSPROPERTY\_VIDEODECODER\_S structure specifies the three-output enable setting.

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

