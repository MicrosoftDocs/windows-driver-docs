---
title: KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE
description: The KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE property controls the three-state output of video decoders that reside on a shared video port bus. This property is optional.
ms.assetid: 33c9a3d2-ffc0-4460-abc4-56bc83c64b55
keywords: ["KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEODECODER_OUTPUT_ENABLE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566052" data-raw-source="[&lt;strong&gt;KSPROPERTY_VIDEODECODER_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566052)"><strong>KSPROPERTY_VIDEODECODER_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the three-state output enable setting. A value of zero indicates three-state output. A nonzero value indicates that the device is actively driving the video port bus.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEODECODER\_S structure specifies the three-output enable setting.

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

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_VIDEODECODER\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566052)

 

 






