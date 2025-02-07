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
ms.date: 02/06/2025
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

        &KSPROPSETID_MidiLoopedStreaming,
        KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER,
        ACX_PROPERTY_ITEM_FLAG_GET,
        EvtMidiGetLoopedStreamingBufferCallback,
        0,
        sizeof(ULONG),
        sizeof(KSMIDILOOPED_BUFFER),



The property descriptor (instance data) consists of a KSRTAUDIO\_BUFFER\_PROPERTY structure that contains a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure along with other members. The client writes its requested buffer size into the structure. If the client does not have to work with a specific base address, it must specify the base address as **NULL**.

The property value (operation data) is a structure of type KSRTAUDIO\_BUFFER. The driver fills this structure with the actual buffer size, base address, and memory barrier flag for the cyclic buffer that it has allocated.

### Return Value

A KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_UNSUCCESSFUL</p></td>
<td align="left"><p>A cyclic buffer with the specified combination of buffer attributes cannot be allocated.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td align="left"><p>Memory for the buffer cannot be allocated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_NOT_READY</p></td>
<td align="left"><p>The device is not ready</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The base address is the virtual memory address at the start of the cyclic buffer. The client can directly access the buffer at this address. The buffer is contiguous in virtual memory. The decision whether to make the buffer contiguous in physical memory is left up to the driver.

The client should set the base address in the property descriptor to **NULL**. The driver sets the base address in the property value to the virtual address of the allocated audio buffer.

Typically, audio hardware requires the audio buffer either to begin and end on sample boundaries or meet other types of hardware-dependent alignment constraints. If sufficient memory is available, the actual size of the buffer is the requested size rounded (up or down) to the nearest sample or other hardware-constrained boundary. The actual size must be at least the requested size; otherwise, the Audio Session API (WASAPI) audio engine won't use the buffer, and stream creation will fail.

If a KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property request is successful, the property value, which is a structure of type KSRTAUDIO\_BUFFER, contains the address and size of the driver-allocated buffer.

Closing the pin automatically frees the buffer that was allocated through this property.

If you want event notifications, you must call [**KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md) instead of KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER.

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

## See also

[**KSRTAUDIO\_BUFFER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_buffer)

[**KSRTAUDIO\_BUFFER\_PROPERTY**](ksrtaudio-buffer-property.md)

[**KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md)
