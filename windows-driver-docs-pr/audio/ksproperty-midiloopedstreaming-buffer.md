---
title: KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER
description: The KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property specifies a driver-allocated cyclic buffer for audio data.The following table summarizes the features of this property.
keywords: ["KSPROPERTY_RTAUDIO_BUFFER Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_BUFFER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 02/07/2025
---

# KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER

The KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property specifies a driver-allocated cyclic buffer for audio data.

The following table summarizes the features of this property.

### Usage Summary Table

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
<td align="left"><p><a href="ksrtaudio-buffer-property.md" data-raw-source="[&lt;strong&gt;KSRTAUDIO_BUFFER_PROPERTY&lt;/strong&gt;](ksrtaudio-buffer-property.md)"><strong>KSRTAUDIO_BUFFER_PROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_buffer" data-raw-source="[&lt;strong&gt;KSRTAUDIO_BUFFER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_buffer)"><strong>KSRTAUDIO_BUFFER</strong></a></p></td>
</tr>
</tbody>
</table>

```cpp

        &KSPROPSETID_MidiLoopedStreaming,
        KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER,
        ACX_PROPERTY_ITEM_FLAG_GET,
        EvtMidiGetLoopedStreamingBufferCallback,
        0,
        sizeof(ULONG),
        sizeof(KSMIDILOOPED_BUFFER),
```

### Return Value

A KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

|Status code|Meaning|
|--- |--- |
|STATUS_UNSUCCESSFUL|A cyclic buffer with the specified combination of buffer attributes cannot be allocated.|
|STATUS_INSUFFICIENT_RESOURCES|Memory for the buffer cannot be allocated.|
|STATUS_DEVICE_NOT_READY|The device is not ready|

## Remarks


## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)
