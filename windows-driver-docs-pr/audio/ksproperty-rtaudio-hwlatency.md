---
title: KSPROPERTY\_RTAUDIO\_HWLATENCY
description: The KSPROPERTY\_RTAUDIO\_HWLATENCY property retrieves a description of the stream latency of the audio hardware and its associated data path. The following table summarizes the features of this property.
keywords: ["KSPROPERTY_RTAUDIO_HWLATENCY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_HWLATENCY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/07/2019
ms.localizationpriority: medium
---

# KSPROPERTY\_RTAUDIO\_HWLATENCY


The KSPROPERTY\_RTAUDIO\_HWLATENCY property retrieves a description of the stream latency of the audio hardware and its associated data path.

The following table summarizes the features of this property.

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwlatency"><strong>KSRTAUDIO_HWLATENCY</strong></a></p></td>
</tr>
</tbody>
</table>

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_HWLATENCY property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

## Remarks

After the [WaveRT miniport driver](./wavert-miniport-driver.md) has allocated the cyclic buffer (see [**KSPROPERTY\_RTAUDIO\_BUFFER**](ksproperty-rtaudio-buffer.md)) the client can send a KSPROPERTY\_RTAUDIO\_HWLATENCY property request to the driver for hardware-latency information.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also

[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

[**KSRTAUDIO\_HWLATENCY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwlatency)

[**KSPROPERTY\_RTAUDIO\_BUFFER**](ksproperty-rtaudio-buffer.md)

[**WaveRT miniport driver**](./wavert-miniport-driver.md)
