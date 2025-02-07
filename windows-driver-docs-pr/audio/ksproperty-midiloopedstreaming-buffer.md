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


|Get |Set|Target|Property descriptor type    |Property value type|
|--- |--- |--- |---------------------------- |------------------ |
|Yes |No  |Pin |KSRTAUDIO_BUFFER_PROPERTYTBD ????|KSRTAUDIO_BUFFER  TBD ???|

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

*KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER*, a member of the [KSPROPERTY_MIDILOOPEDSTREAMING enum](ne-ksmedia-ksproperty_midiloopedstreaming.md) is called with a [KSMIDILOOPED_BUFFER_PROPERTY](ns-ksmedia-ksmidilooped_buffer_property.md), containing the requested buffer size. A [KSMIDILOOPED_BUFFER](ns-ksmedia-ksmidilooped_buffer.md) is returned, containing the allocated buffer, mapped to the caller process space, along with the actual buffer size. 

The buffer is double mapped (the physical memory is mapped to the virtual address space twice, back to back) to simplify the read and write operations. This enables a read or write of up to one buffer size past the end of the primary buffer to loop back to the same physical memory that is mapped to the start of the primary buffer, without the need to perform address calculations. 

MIDI messages are read or written to the buffer one at a time, so the maximum single message size, enforced, is a UMP128, which is 16 bytes. This means that the maximum read or write past the end of the primary buffer, into the double mapped buffer, is 16 bytes, which is well less than the size of the mapping. 

This same buffer transfer mechanism is also used for moving messages between the MIDI service and client applications, using a shared library implementation of the reader and writer. 

*KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS* a member of the [KSPROPERTY_MIDILOOPEDSTREAMING enum](ne-ksmedia-ksproperty_midiloopedstreaming.md) is called with no input data. A [KSMIDILOOPED_REGISTERS struct](ns-ksmedia-ksmidilooped_registers.md) is returned, containing pointers to the read and write positions that are mapped to the caller’s process space. 

*KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT*, a member of the [KSPROPERTY_MIDILOOPEDSTREAMING enum](ne-ksmedia-ksproperty_midiloopedstreaming.md) takes in a caller created event handle in a [KSMIDILOOPED_EVENT struct](ns-ksmedia-ksmidilooped_event.md). The driver adds a reference to the handle for that event and stores it. 

Only one pin handle is permitted be opened at a time, which is the same requirement that the MIDI version 1 driver and many other KS/ACX drivers have. Only the process which holds the open pin may allocate the shared memory buffer. 

The shared memory buffer is allocated and controlled by the audio driver, and the allocations are performed at page boundaries to prevent unintentional kernel memory exposure. If the pin handle is closed, or the calling process exits, the worker threads are shut down and the allocated buffers freed by the driver. 

## -see-also


## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)

[**KSMIDILOOPED_BUFFER_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)

[**KSMIDILOOPED_BUFFER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md) 

[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)