---
title: KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG
description: The KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property specifies the actual spatial placement of channels in the audio stream that a node outputs.
ms.assetid: 5ce9bf4a-c84e-4d7e-8e75-896c88ec1a72
keywords: ["KSPROPERTY_AUDIO_CHANNEL_CONFIG Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_CHANNEL_CONFIG
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG


The KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property specifies the actual spatial placement of channels in the audio stream that a node outputs.

## <span id="ddk_ksproperty_audio_channel_config_ks"></span><span id="DDK_KSPROPERTY_AUDIO_CHANNEL_CONFIG_KS"></span>


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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter/Pin</p></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537083" data-raw-source="[&lt;strong&gt;KSAUDIO_CHANNEL_CONFIG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537083)"><strong>KSAUDIO_CHANNEL_CONFIG</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSAUDIO\_CHANNEL\_CONFIG. This structure specifies the channels that are contained in the output stream and the assignment of those channels to speakers.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

When used as a property of a DAC node ([**KSNODETYPE\_DAC**](ksnodetype-dac.md)) or 3D node ([**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)), the KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property specifies the DirectSound speaker configuration. For stereo speaker configurations, this property is used in conjunction with the [**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](ksproperty-audio-stereo-speaker-geometry.md) property, which distinguishes between headphones and several stereo speaker configurations. For more information about speaker configurations, see [DirectSound Speaker-Configuration Settings](https://msdn.microsoft.com/library/windows/hardware/ff536332).

DirectSound also uses the KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG property to query a "pan" node for its channel configuration. A pan node is the second volume node ([**KSNODETYPE\_VOLUME**](ksnodetype-volume.md)) on a mixer pin that meets the [DirectSound node-ordering requirements](https://msdn.microsoft.com/library/windows/hardware/ff536331). DirectSound implementation of the **IDirectSoundBuffer::SetPan** method (described in the Microsoft Windows SDK documentation) uses the pan node's [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md) property to control panning.

DirectSound treats KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG as a filter property on a DAC node, and as a pin property on volume and 3D nodes.

Clients also use this property to select the format of the stream that a [**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md) node outputs.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSAUDIO\_CHANNEL\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff537083)

[**KSNODETYPE\_DAC**](ksnodetype-dac.md)

[**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)

[**KSNODETYPE\_VOLUME**](ksnodetype-volume.md)

[**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md)

[**KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY**](ksproperty-audio-stereo-speaker-geometry.md)

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

 

 






