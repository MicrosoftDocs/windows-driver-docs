---
title: KSPROPERTY\_AUDIO\_SAMPLING\_RATE
description: The KSPROPERTY\_AUDIO\_SAMPLING\_RATE property specifies the rate at which a node samples its input stream in order to produce its output stream.
ms.assetid: c5e48678-3b9a-4e5b-ae7b-16f9dcae7492
keywords: ["KSPROPERTY_AUDIO_SAMPLING_RATE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_SAMPLING_RATE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_SAMPLING\_RATE


The KSPROPERTY\_AUDIO\_SAMPLING\_RATE property specifies the rate at which a node samples its input stream in order to produce its output stream.

## <span id="ddk_ksproperty_audio_sampling_rate_ks"></span><span id="DDK_KSPROPERTY_AUDIO_SAMPLING_RATE_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and specifies sampling rate. This rate is expressed as the number of samples per second (the sampling frequency in Hz).

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_SAMPLING\_RATE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The miniport driver should return an error on a set-property request if the node does not support the specified sampling rate.

This property is used to control the sampling rate for the following node types:

-   ADC node ([**KSNODETYPE\_ADC**](ksnodetype-adc.md))

-   DAC node ([**KSNODETYPE\_DAC**](ksnodetype-dac.md))

-   SRC node ([**KSNODETYPE\_SRC**](ksnodetype-src.md))

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

[**KSNODETYPE\_ADC**](ksnodetype-adc.md)

[**KSNODETYPE\_DAC**](ksnodetype-dac.md)

[**KSNODETYPE\_SRC**](ksnodetype-src.md)

 

 






