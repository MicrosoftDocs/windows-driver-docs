---
title: KSPROPERTY\_AUDIO\_TREBLE
description: The KSPROPERTY\_AUDIO\_TREBLE property specifies the treble level for a channel in a tone node (KSNODETYPE\_TONE).
keywords: ["KSPROPERTY_AUDIO_TREBLE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIO_TREBLE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_AUDIO\_TREBLE


The KSPROPERTY\_AUDIO\_TREBLE property specifies the treble level for a channel in a tone node ([**KSNODETYPE\_TONE**](ksnodetype-tone.md)).

## <span id="ddk_ksproperty_audio_treble_ks"></span><span id="DDK_KSPROPERTY_AUDIO_TREBLE_KS"></span>


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
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type LONG and specifies the treble-level setting for the channel. Treble-level values use the following scale:

-2147483648 is -Infinity decibels (attenuation),

-2147483647 is -32767.99998474 decibels (attenuation), and

+2147483647 is +32767.99998474 decibels (gain).

A decibel range represented by integer values -2147483648 to +2147483647, where

This scale has a resolution of 1/65536 decibel.

The filter will succeed a set-property request that specifies a value that is beyond the range of the filter but will clamp the value to the supported range. In a subsequent request to get this property, however, it will return the actual value used.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_TREBLE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

A tone node can support properties for controlling treble level, mid-frequency level, bass level, and bass boost. For more information, see [**KSNODETYPE\_TONE**](ksnodetype-tone.md).

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


[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel)

[**KSNODETYPE\_TONE**](ksnodetype-tone.md)

