---
title: KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY
description: The KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY property is used in combination with KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG to implement the DirectSound speaker-configuration property for hardware-accelerated 3D audio.
ms.assetid: 4a870368-6a9b-41bc-80c3-da6ad1f2454b
keywords: ["KSPROPERTY_AUDIO_STEREO_SPEAKER_GEOMETRY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_STEREO_SPEAKER_GEOMETRY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY


The KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY property is used in combination with [**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md) to implement the DirectSound speaker-configuration property for hardware-accelerated 3D audio. This is an optional property of DAC nodes ([**KSNODETYPE\_DAC**](ksnodetype-dac.md)) and 3D nodes ([**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)).

## <span id="ddk_ksproperty_audio_stereo_speaker_geometry_ks"></span><span id="DDK_KSPROPERTY_AUDIO_STEREO_SPEAKER_GEOMETRY_KS"></span>


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
<td align="left"><p>Pin/Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type LONG and specifies the speaker geometry. This value can be set to one of the following constants, which are defined in header file Ksmedia.h:

-   KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_HEADPHONES

-   KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_MIN

-   KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_NARROW

-   KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_WIDE

-   KSAUDIO\_STEREO\_SPEAKER\_GEOMETRY\_MAX

The preceding parameters are equivalent in meaning (but not equal in value) to the following values, which are used by the **IDirectSound::GetSpeakerConfig** method (see the Microsoft Windows SDK documentation) and are defined in header file Dsound.h:

-   DSSPEAKER\_HEADPHONE

-   DSSPEAKER\_STEREO | DSSPEAKER\_GEOMETRY\_MIN

-   DSSPEAKER\_STEREO | DSSPEAKER\_GEOMETRY\_NARROW

-   DSSPEAKER\_STEREO | DSSPEAKER\_GEOMETRY\_WIDE

-   DSSPEAKER\_STEREO | DSSPEAKER\_GEOMETRY\_MAX

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

DirectSound treats KSPROPERTY\_AUDIO\_STEREO\_SPEAKER\_GEOMETRY as a filter property on a DAC node, and as a pin property on a 3D node.

For additional information, see [DirectSound Speaker-Configuration Settings](https://msdn.microsoft.com/library/windows/hardware/ff536332).

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


[**KSPROPERTY\_AUDIO\_CHANNEL\_CONFIG**](ksproperty-audio-channel-config.md)

[**KSNODETYPE\_DAC**](ksnodetype-dac.md)

[**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md)

[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

 

 






