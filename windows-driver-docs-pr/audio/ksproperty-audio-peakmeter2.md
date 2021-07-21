---
title: KSPROPERTY\_AUDIO\_PEAKMETER2
description: Windows 8 introduces the KSPROPERTY\_AUDIO\_PEAKMETER2 property that reports the maximum audio signal level that occurred at a peakmeter node (KSNODETYPE\_PEAKMETER) since the last time the peakmeter node was reset.
keywords: ["KSPROPERTY_AUDIO_PEAKMETER2 Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_PEAKMETER2
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 04/21/2020
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_PEAKMETER2

Windows 8 introduced the KSPROPERTY\_AUDIO\_PEAKMETER2 property that reports the maximum audio signal level that occurred at a peakmeter node (KSNODETYPE\_PEAKMETER) since the last time the peakmeter node was reset.

## <span id="ddk_ksproperty_audio_peakmeter2_ks"></span><span id="DDK_KSPROPERTY_AUDIO_PEAKMETER2_KS"></span>


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
<td align="left"><p>Node via Filter or Pin instance</p></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY_AUDIO_CHANNEL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty_audio_channel)"><strong>KSNODEPROPERTY_AUDIO_CHANNEL</strong></a></td>
<td align="left"><p>LONG</p></td>
</tr>
</tbody>
</table>


The property value (operation data) is of type LONG and specifies the peak sample value at the node. If the peak value is negative, its absolute value is used.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_PEAKMETER2 property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code. The following table shows a possible error status code.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_NOT_IMPLEMENTED</p></td>
<td align="left"><p>The KS filter cannot return the current value of the peakmeter.</p></td>
</tr>
</tbody>
</table>


## Remarks

The KSPROPERTY\_AUDIO\_PEAKMETER2 property is almost identical to the [**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md) property. The KSPROPERTY\_AUDIO\_PEAKMETER2 property was introduced with Windows 8 to provide improved hardware metering of a pin topology. The legacy KSPROPERTY\_AUDIO\_PEAKMETER property is deprecated and should no longer be used.

SignedMinimum must be set to LONG\_MIN (instead of 0x8000), and SignedMaximum must be set to LONG\_MAX (instead of 0x7fff). And also, note that peak meter values are relative to this scale and the scale is linear in amplitude.

So if, for example, you have a waveform with negative and positive peaks at -1 and +1 respectively (on a scale that goes from -1 to +1), then a peak meter value of LONG\_MAX accurately reports the maximum waveform value for a given time window. Conversely, a peak meter value of zero (0) should be used to report silence, where all the waveform’s values are zero. But in the case of a waveform whose peak values are *between* zero (0) and LONG\_MAX, the reported waveform values would be linearly reduced from the originals.

Therefore, in the case of the waveform that swings between -0.5 and +0.5 (on a scale that goes from -1 to +1), the peak meter value must be set to LONG\_MAX/2.

A KS audio filter handles this property request synchronously. If the request succeeds, it resets the peakmeter, which initializes the accumulated peak value to zero. If the request does not succeed, the peakmeter is not changed.

The system sends an IOCTL\_KS\_PROPERTY request for the KSPROPERTY\_AUDIO\_PEAKMETER2 property at IRQL PASSIVE\_LEVEL.

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

[**KSNODETYPE\_PEAKMETER**](ksnodetype-peakmeter.md)

[**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md)
