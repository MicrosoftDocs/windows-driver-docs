---
title: KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS
description: The KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS property is used to retrieve pointers to the read and write positions that are mapped to the caller's process space. 
ms.date: 12/16/2025
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
---

# KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS

The **KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** property is used to retrieve pointers to the read and write positions that are mapped to the caller's process space.

The following table summarizes the features of this property.

### Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | KSPROPERTY | KSMIDILOOPED_REGISTERS |

Property descriptor type is **KSPROPERTY**. Property value type is a **[KSMIDILOOPED_REGISTERS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_registers)** structure.

### Return Value

A **KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** property request returns STATUS_SUCCESS to indicate successful completion. Otherwise, the request returns an error code that indicates a failure.

| Status code | Meaning |
|--|--|
| STATUS_SUCCESS | Indicates successful completion. |
| STATUS_ALREADY_INITIALIZED | Returned if the registers are already allocated or if KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER was called by a different process. Meaning that the looped memory buffer is already allocated and mapped to a different process than the one requesting the registers. |
| STATUS_INSUFFICIENT_RESOURCES | Returned if there's insufficient memory to allocate the registers. |

## Remarks

**KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** is called with no input data. A **[KSMIDILOOPED_REGISTERS](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_registers)**  structure is returned, containing pointers to the read and write positions that are mapped to the caller's process space.

### Sample Code

```cpp
    HRESULT
    LoopedRegisterCall(
        _In_ PULONG& ReadPosition,
        _In_ PULONG& WritePosition
    )
    {
        KSPROPERTY property {0};
        KSMIDILOOPED_REGISTERS registers {0};
        ULONG propertySize {sizeof(property)};

        property.Set    = KSPROPSETID_MidiLoopedStreaming; 
        property.Id     = KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS;       
        property.Flags  = KSPROPERTY_TYPE_GET;

        RETURN_IF_FAILED(SyncIoctl(
            m_Pin.get(),
            IOCTL_KS_PROPERTY,
            &property,
            propertySize,
            &registers,
            sizeof(registers),
            nullptr));

        ReadPosition = (PULONG) registers.ReadPosition;
        WritePosition = (PULONG) registers.WritePosition;

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
- **[KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT](ksproperty-midiloopedstreaming-notification-event.md)**
- **[KSPROPERTY](../stream/ksproperty-structure.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming)**
- **[KSMIDILOOPED_BUFFER_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property)**
- **[KSMIDILOOPED_BUFFER](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING enum](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming)**
