---
title: KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE
description: The KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE property is used to enable and disable dynamic tracking of a node's sampling rate.
keywords: ["KSPROPERTY_AUDIO_DYNAMIC_SAMPLING_RATE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIO_DYNAMIC_SAMPLING_RATE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE


The KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE property is used to enable and disable dynamic tracking of a node's sampling rate.

## <span id="ddk_ksproperty_audio_dynamic_sampling_rate_ks"></span><span id="DDK_KSPROPERTY_AUDIO_DYNAMIC_SAMPLING_RATE_KS"></span>


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

 

The property value (operation data) is of type BOOL and specifies whether dynamic tracking is enabled or disabled on the node. The value is **TRUE** when dynamic tracking of the sampling rate is enabled. In this mode, the input stream's sampling rate can be varied explicitly by setting the rate through [**KSPROPERTY\_AUDIO\_SAMPLING\_RATE**](ksproperty-audio-sampling-rate.md) or implicitly by setting the rate through the time stamps on the input stream.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_DYNAMIC\_SAMPLING\_RATE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

This property is used to control dynamic tracking in the following node types:

-   ADC node ([**KSNODETYPE\_ADC**](ksnodetype-adc.md))

-   DAC node ([**KSNODETYPE\_DAC**](ksnodetype-dac.md))

-   SRC node ([**KSNODETYPE\_SRC**](ksnodetype-src.md))

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

[**KSPROPERTY\_AUDIO\_SAMPLING\_RATE**](ksproperty-audio-sampling-rate.md)

[**KSNODETYPE\_ADC**](ksnodetype-adc.md)

[**KSNODETYPE\_DAC**](ksnodetype-dac.md)

[**KSNODETYPE\_SRC**](ksnodetype-src.md)

