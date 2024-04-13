---
title: KSPROPERTY\_AUDIO\_SURROUND\_ENCODE
description: The KSPROPERTY\_AUDIO\_SURROUND\_ENCODE property specifies whether the filter's surround encoder is enabled or disabled. A surround-encoder node (KSNODETYPE\_PROLOGIC\_ENCODER) performs Dolby Surround Pro Logic encoding.
keywords: ["KSPROPERTY_AUDIO_SURROUND_ENCODE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIO_SURROUND_ENCODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_AUDIO\_SURROUND\_ENCODE


The KSPROPERTY\_AUDIO\_SURROUND\_ENCODE property specifies whether the filter's surround encoder is enabled or disabled. A surround-encoder node ([**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md)) performs Dolby Surround Pro Logic encoding.

## <span id="ddk_ksproperty_audio_surround_encode_ks"></span><span id="DDK_KSPROPERTY_AUDIO_SURROUND_ENCODE_KS"></span>


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
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type BOOL and indicates whether the surround-encoder node is enabled or not. A value of **TRUE** indicates that the surround-encoder node is enabled. **FALSE** indicates that it is disabled.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_SURROUND\_ENCODE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

In Microsoft Windows XP and later, the [KMixer system driver](./kernel-mode-wdm-audio-components.md#kmixer-system-driver) supports the KSPROPERTY\_AUDIO\_SURROUND\_ENCODE property.

If enabled, the surround-encoder node encodes the four-channel input stream (with channels for left, right, center, and back speakers) to a surround-encoded stereo output stream. This output stream can be decoded by a [**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md) node, for example. It can also be played through the audio device's analog stereo outputs, which can be connected to an external surround decoder that directly drives left, right, center, and back speakers.

## Requirements

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


[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)

[**KSNODETYPE\_PROLOGIC\_ENCODER**](ksnodetype-prologic-encoder.md)

[**KSNODETYPE\_PROLOGIC\_DECODER**](ksnodetype-prologic-decoder.md)

