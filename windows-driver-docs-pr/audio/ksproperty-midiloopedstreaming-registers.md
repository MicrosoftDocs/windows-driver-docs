---
title: *KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS
description: The KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS property .
keywords: ["KSPROPERTY_RTAUDIO_CLOCKREGISTER Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_CLOCKREGISTER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# *KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS


The *KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS property .

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwregister_property" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER_PROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwregister_property)"><strong>KSRTAUDIO_HWREGISTER_PROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwregister" data-raw-source="[&lt;strong&gt;KSRTAUDIO_HWREGISTER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_hwregister)"><strong>KSRTAUDIO_HWREGISTER</strong></a></p></td>
</tr>
</tbody>
</table>

 
   &KSPROPSETID_MidiLoopedStreaming,
        KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS,
        ACX_PROPERTY_ITEM_FLAG_GET,
        EvtMidiGetLoopedStreamingRegistersCallback,
        0,
        0,
        sizeof(KSMIDILOOPED_REGISTERS)

The property descriptor (instance data) consists of a KSRTAUDIO_HWREGISTER_PROPERTY structure that contains a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure. Before sending the request, the client loads the KSRTAUDIO_HWREGISTER_PROPERTY structure with values that indicate the preferred base address for the clock register.

The property value (operation data) is a pointer to a KSRTAUDIO_HWREGISTER structure into which the property handler writes the register address and the register-update frequency. This register address is the user-mode or kernel-mode virtual address into which the hardware register is mapped. The client can directly read the register from this address.

### Return Value

A *KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an error code that indicates a failure.

## Remarks

Some audio devices contain clock registers. A clock register is a wall clock counter that starts running when the hardware powers up and stops when the hardware powers down. Software uses clock registers to synchronize between two or more controller devices by measuring the relative drift between the hardware clocks of the device.

If successful, the property request maps the clock register to a virtual memory address that is accessible from either user-mode or kernel-mode, as specified by the client. Thereafter, the client reads from this address to obtain the current value of the clock register.

The property request fails if the audio hardware does not support a clock register that can be mapped to virtual memory.

The mapping of the clock register is destroyed when the pin closes. The client can map the register only once in the lifetime of a pin instance, and any subsequent call to map the clock register again for that instance fails.

It is typically faster to read a clock register than it is to send a [**KSPROPERTY_CLOCK_TIME**](../stream/ksproperty-clock-time.md) request, which requires transitions between user-mode and kernel-mode for user-mode clients.

## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_BUFFER**](ksproperty-midiloopedstreaming-buffer.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

