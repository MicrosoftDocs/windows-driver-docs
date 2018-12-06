---
title: KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS
description: The KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS property is used to retrieve the number of frequency bands in the equalization table. This is a get-only property of a channel in an EQ node (KSNODETYPE\_EQUALIZER).
ms.assetid: b7bb9f05-0b27-4b41-aa38-efb87fc1beee
keywords: ["KSPROPERTY_AUDIO_NUM_EQ_BANDS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_NUM_EQ_BANDS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS


The KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS property is used to retrieve the number of frequency bands in the equalization table. This is a get-only property of a channel in an EQ node ([**KSNODETYPE\_EQUALIZER**](ksnodetype-equalizer.md)).

## <span id="ddk_ksproperty_audio_num_eq_bands_ks"></span><span id="DDK_KSPROPERTY_AUDIO_NUM_EQ_BANDS_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537145" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537145)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies the number of frequency bands in the node's equalization table.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_NUM\_EQ\_BANDS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is used in conjunction with the [**KSPROPERTY\_AUDIO\_EQ\_BANDS**](ksproperty-audio-eq-bands.md) and [**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md) properties to determine the lengths of the arrays that contain the values for those properties.

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


[**KSNODEPROPERTY\_AUDIO\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff537145)

[**KSNODETYPE\_EQUALIZER**](ksnodetype-equalizer.md)

[**KSPROPERTY\_AUDIO\_EQ\_BANDS**](ksproperty-audio-eq-bands.md)

[**KSPROPERTY\_AUDIO\_EQ\_LEVEL**](ksproperty-audio-eq-level.md)

 

 






