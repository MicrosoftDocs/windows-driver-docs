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
ms.date: 02/10/2025
---

# KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER

The **KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER** property specifies a driver-allocated cyclic buffer for audio data.

The following table summarizes the features of this property.

### Usage Summary Table


|Get |Set|Target|Property descriptor type    |Property value type|
|--- |--- |--- |---------------------------- |------------------ |
|Yes |No  |Pin |KSRTAUDIO_BUFFER_PROPERTYTBD ????|KSRTAUDIO_BUFFER  TBD ???|


Code snip notes:

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

A **KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER** property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

|Status code|Meaning|
|--- |--- |
|STATUS_UNSUCCESSFUL|A cyclic buffer with the specified combination of buffer attributes cannot be allocated.|
|STATUS_INSUFFICIENT_RESOURCES|Memory for the buffer cannot be allocated.|
|STATUS_DEVICE_NOT_READY|The device is not ready|

## Remarks

**KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER**, is called with a `[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)`, containing the requested buffer size. A `[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md)` is returned, containing the allocated buffer, mapped to the caller process space, along with the actual buffer size. 

The buffer is double mapped (the physical memory is mapped to the virtual address space twice, back to back) to simplify the read and write operations. This enables a read or write of up to one buffer size past the end of the primary buffer to loop back to the same physical memory that is mapped to the start of the primary buffer, without the need to perform address calculations. 

MIDI messages are read or written to the buffer one at a time, so the maximum single message size, enforced, is a UMP128, which is 16 bytes. This means that the maximum read or write past the end of the primary buffer, into the double mapped buffer, is 16 bytes, which is well less than the size of the mapping. 

This same buffer transfer mechanism is also used for moving messages between the MIDI service and client applications, using a shared library implementation of the reader and writer. 

TBD - OK to have the next text here, or perhaps move to KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS?

[KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS](ksproperty-midiloopedstreaming-registers.md) is called with no input data. A `[KSMIDILOOPED_REGISTERS struct](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_registers.md)` is returned, containing pointers to the read and write positions that are mapped to the caller’s process space. 

Only one pin handle is permitted be opened at a time, which is the same requirement that the MIDI version 1 driver and many other KS/ACX drivers have. Only the process which holds the open pin may allocate the shared memory buffer. 

The shared memory buffer is allocated and controlled by the audio driver, and the allocations are performed at page boundaries to prevent unintentional kernel memory exposure. If the pin handle is closed, or the calling process exits, the worker threads are shut down and the allocated buffers freed by the driver. 

### Sample Code

TBD - Better code sample to show here? Update code comment on property.RequestedBufferSize?

```cpp
_Use_decl_annotations_
HRESULT
KSMidiDevice::ConfigureLoopedBuffer(ULONG& bufferSize
)
{
    KSMIDILOOPED_BUFFER_PROPERTY property {0};
    KSMIDILOOPED_BUFFER buffer{0};
    ULONG propertySize {sizeof(property)};

    property.Property.Set           = KSPROPSETID_MidiLoopedStreaming; 
    property.Property.Id            = KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER;       
    property.Property.Flags         = KSPROPERTY_TYPE_GET;

    // Seems to be a reasonable balance for now,
    // TBD make this configurable via api or registry.
    property.RequestedBufferSize    = bufferSize;

    RETURN_IF_FAILED(SyncIoctl(
        m_Pin.get(),
        IOCTL_KS_PROPERTY,
        &property,
        propertySize,
        &buffer,
        sizeof(buffer),
        nullptr));

    m_MidiPipe->Data.BufferAddress = (PBYTE) buffer.BufferAddress;
    bufferSize = m_MidiPipe->Data.BufferSize = buffer.ActualBufferSize;

    return S_OK;
}
```


## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

TBD Future links:

`[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)`

`[**KSMIDILOOPED_BUFFER_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)`

`[**KSMIDILOOPED_BUFFER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md)` 

`[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)`