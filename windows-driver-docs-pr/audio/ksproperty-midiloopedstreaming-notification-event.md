---
title: KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT
description: The KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property registers a reference to the handle for the MIDILOOPED streaming event and stores it.
ms.date: 09/25/2025
keywords: ["KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT

The **KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT** is used to provide the read and write events for the looped buffer to the driver. The driver adds a reference to the handle for that event and stores it.

The following table summarizes the features of this property.

### Usage Summary Table

|Get |Set|Target|Property descriptor type    |Property value type|
|--- |--- |--- |---------------------------- |------------------ |
|Yes |Yes |Pin |KSPROPERTY| KSMIDILOOPED_EVENT2|

The property descriptor type is KSPROPERTY. The property value type is KSMIDILOOPED_EVENT2 (which replaces KSMIDILOOPED_EVENT) containing the read and write events.

### Return Value

A **KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT** property request returns STATUS_SUCCESS to indicate successful completion. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

| Status code | Meaning |
|--|--|
| STATUS_UNSUCCESSFUL | A cyclic buffer with the specified combination of buffer attributes cannot be allocated. |
| STATUS_INSUFFICIENT_RESOURCES | Memory for the buffer cannot be allocated. |
| STATUS_DEVICE_NOT_READY | The device is not ready |
| STATUS_ALREADY_INITIALIZED | The events have already been set. |
| STATUS_ALREADY_INITIALIZED | **[KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER](ksproperty-midiloopedstreaming-buffer.md)** was called by a different process than the one attempting to configure the notification events. |

## Remarks

**KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT** takes in a caller created event handle in a **[KSMIDILOOPED_EVENT](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_event.md)** structure. The driver adds a reference to the handle for that event and stores it.

### Sample Code

```cpp
    HRESULT
    LoopedEventCall(
        _In_ HANDLE WriteEvent,
        _In_ HANDLE ReadEvent
    )
    {
        KSPROPERTY property {0};
        ULONG propertySize {sizeof(property)};
        KSMIDILOOPED_EVENT2 LoopedEvent {0};

        LoopedEvent.WriteEvent = WriteEvent;
        LoopedEvent.ReadEvent = ReadEvent;

        property.Set    = KSPROPSETID_MidiLoopedStreaming; 
        property.Id     = KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT;       
        property.Flags  = KSPROPERTY_TYPE_SET;

        RETURN_IF_FAILED(SyncIoctl(
            m_Pin.get(),
            IOCTL_KS_PROPERTY,
            &property,
            propertySize,
            &LoopedEvent,
            sizeof(LoopedEvent),
            nullptr));

        return S_OK;
    }
```

## Requirements

| Item | Description |
|--|--|
| Version | Available in Windows version 25H2 and later. |
| Header | Ksmedia.h |

## See also

- **[KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER](ksproperty-midiloopedstreaming-buffer.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS](ksproperty-midiloopedstreaming-registers.md)**
- **[KSPROPERTY](../stream/ksproperty-structure.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)**
- **[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)**
- **[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)**
