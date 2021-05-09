---
title: KSPROPERTY\_AUDIO\_LATENCY
description: The KSPROPERTY\_AUDIO\_LATENCY property is used to report the delay (or amount of audio buffering) that is associated with the stream.
keywords: ["KSPROPERTY_AUDIO_LATENCY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_LATENCY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_LATENCY


The KSPROPERTY\_AUDIO\_LATENCY property is used to report the delay (or amount of audio buffering) that is associated with the stream.

## <span id="ddk_ksproperty_audio_latency_ks"></span><span id="DDK_KSPROPERTY_AUDIO_LATENCY_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/previous-versions/ff564262(v=vs.85)" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/previous-versions/ff564262(v=vs.85))"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kstime" data-raw-source="[&lt;strong&gt;KSTIME&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kstime)"><strong>KSTIME</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSTIME that specifies the stream latency.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_LATENCY property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

This property is used to query the stream latency of a pin on an AEC filter. For more information, see [Exposing Hardware-Accelerated Capture Effects](./exposing-hardware-accelerated-capture-effects.md).

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


[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

[**KSTIME**](/windows-hardware/drivers/ddi/ks/ns-ks-kstime)

