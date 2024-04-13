---
title: KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION
description: KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION returns stream presentation information.
keywords: ["KSPROPERTY_RTAUDIO_PRESENTATION_POSITION Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_PRESENTATION_POSITION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 01/31/2019
---

# KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION


KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION returns stream presentation information.

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
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_presentation_position"><STRONG>KSAUDIO_PRESENTATION_POSITION</STRONG></a></p></td>
</tr>
</tbody>
</table>
 

The property descriptor (instance data) is a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure. Before sending the request, the client loads the structure with values that describe the current cursor position in audio data stream.

The property value is a [**KSAUDIO\_PRESENTATION\_POSITION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_presentation_position) structure that represents a recent presentation position in the audio data stream.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code.

## Remarks

The OS may periodically get this property from the driver to retrieve recent presentation position information from the driver in order to allow upper layers to synchronize video or other activity with the audio stream.

The value returned in the u64PositionInBlocks member of [**KSAUDIO\_PRESENTATION\_POSITION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_presentation_position) should be consistent with the packet count returned by KSPROPERTY\_RTAUDIO\_PACKETCOUNT and the driver’s interpretation of the packet number passed to SetWritePacket. In other words, the first sample of packet 0 is block 0.

This does not mean that KSPROPERTY\_RTAUDIO\_PACKETCOUNT and KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION, if called simultaneously, would return values that refer to the same sample. KSPROPERTY\_RTAUDIO\_PACKETCOUNT returns information about the samples transferred from the WaveRT buffer to the hardware, while KSPROPERTY\_RTAUDIO\_PRESENTATION\_POSITION returns information about samples presented at the output of the system. These are two different pieces of information.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 10 and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[KSPROPSETID\_RTAudio](kspropsetid-rtaudio.md)
