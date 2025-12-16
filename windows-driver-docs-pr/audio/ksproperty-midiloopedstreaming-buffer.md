---
title: KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER
description: The KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER property specifies a driver-allocated cyclic buffer for audio data.
ms.date: 12/16/2025
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
---

# KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER

The **KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER** property is used to allocate the cross process looped memory buffer, which is used for transferring the MIDI data.

The following table summarizes the features of this property.

### Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | KSMIDILOOPED_BUFFER_PROPERTY | KSMIDILOOPED_BUFFER |

The property descriptor consists of a **[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property)**, which includes a **KSPROPERTY** and a requested buffer size. The property value type is **[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer)**, which returns the looped (cyclic) buffer mapped to the callers process space and the actual size allocated.

### Return Value

A **KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER** property request returns STATUS_SUCCESS to indicate successful completion. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

| Status code | Meaning |
|--|--|
| STATUS_ALREADY_INITIALIZED | Returned if the registers are already allocated or if KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER was called by a different process, meaning that the looped memory buffer is already allocated and mapped to a different process than the one requesting the registers. |
| STATUS_DEVICE_NOT_READY | The device isn't ready |
| STATUS_INSUFFICIENT_RESOURCES | Returned if there's insufficient memory to allocate the registers. |
| STATUS_INVALID_PARAMETER | If the KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER or provided KSMIDILOOPED_BUFFER are invalid or an invalid buffer size is requested. |
| STATUS_SUCCESS | Indicates successful completion. |
| STATUS_UNSUCCESSFUL | A cyclic buffer with the specified combination of buffer attributes can't be allocated. |

## Remarks

**KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER** is called with a **[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property)**, containing the requested buffer size. A **[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer)** is returned, containing the allocated buffer, mapped to the caller process space, along with the actual buffer size.

The buffer is double mapped to simplify read and write operations. The physical memory is mapped to the virtual address space twice, back to back. The double mapping allows reads or writes up to one buffer size past the end of the primary buffer. These operations automatically loop back to the same physical memory that is mapped to the start of the primary buffer. This eliminates the need to perform address calculations.

MIDI messages are read or written to the buffer one at a time, so the maximum single message size, enforced, is a UMP128, which is 16 bytes. The maximum read or write past the end of the primary buffer, into the double mapped buffer, is 16 bytes, which is less than the size of the mapping.

The buffer transfer mechanism is also used for moving messages between the MIDI service and client applications, using a shared library implementation of the reader and writer.

Only one pin handle can be opened at a time, which is the same requirement that the MIDI version 1 driver and many other KS/ACX drivers have. Only the process that holds the open pin can allocate the shared memory buffer.

The audio driver allocates and controls the shared memory buffer. The allocations are performed at page boundaries to prevent unintentional kernel memory exposure. If the pin handle is closed, or the calling process exits, the worker threads are shut down and the allocated buffers freed by the driver.

### Sample Code

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

| Item | Description |
|--|--|
| Version | Available in Windows 11 version 25H2 and later. |
| Header | Ksmedia.h |

## See also

- **[KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS](ksproperty-midiloopedstreaming-registers.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT](ksproperty-midiloopedstreaming-notification-event.md)**
- **[KSPROPERTY](../stream/ksproperty-structure.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming)**
- **[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property)**
- **[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming)**
