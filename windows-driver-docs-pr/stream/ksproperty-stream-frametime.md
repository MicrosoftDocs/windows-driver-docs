---
title: KSPROPERTY\_STREAM\_FRAMETIME
description: The KSPROPERTY\_STREAM\_FRAMETIME property allows a client to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.
ms.assetid: 0cc218eb-1f21-4b45-ac48-b3e308bddfaf
keywords: ["KSPROPERTY_STREAM_FRAMETIME Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_FRAMETIME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_STREAM\_FRAMETIME


The KSPROPERTY\_STREAM\_FRAMETIME property allows a client to determine the duration of the next frame based on the particular media stream, and use that information to step-frame a sequence.

## <span id="ddk_ksproperty_stream_frametime_ks"></span><span id="DDK_KSPROPERTY_STREAM_FRAMETIME_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff562558" data-raw-source="[&lt;strong&gt;KSFRAMETIME&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562558)"><strong>KSFRAMETIME</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

KSPROPERTY\_STREAM\_FRAMETIME is an optional property that should be implemented if a pin recognizes the specifics of the media type it is transporting.

The property is supported by rendering pins and is used to return the duration of the next frame of data and any flags associated with that frame. A frame is generally the smallest usable unit into which the data can be split. For a video stream, this might be a video frame or a field. For audio, this would be a sample for each channel in the stream. For MIDI, this would be the next MIDI event.

The duration is measured in terms of the presentation time units provided by the pin. This is dependent on the interface and the numerator/denominator pair used in the presentation time. This does not apply to streams that are not oriented toward any specific media type, such as generic file readers.

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


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSFRAMETIME**](https://msdn.microsoft.com/library/windows/hardware/ff562558)

 

 






