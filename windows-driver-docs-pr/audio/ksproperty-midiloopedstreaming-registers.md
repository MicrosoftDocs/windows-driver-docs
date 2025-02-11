---
title: KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS
description: The KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS property is used to retrieve pointers to the read and write positions that are mapped to the caller’s process space. 
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
ms.date: 02/10/2023
---

# KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS

The **KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** property is used to retrieve pointers to the read and write positions that are mapped to the caller’s process space. 

The following table summarizes the features of this property.

### Usage Summary Table

|Get |Set|Target|Property descriptor type    |Property value type|
|--- |--- |--- |---------------------------- |------------------ |
|Yes |No  |Pin |KSRTAUDIO_HWREGISTER_PROPERTY TBD ????|KSRTAUDIO_HWREGISTER  TBD ???|

Internal code snip notes:

ACX_PROPERTY_ITEM_FLAG_GET

EvtMidiGetLoopedStreamingRegistersCallback

### Return Value

A **KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an error code that indicates a failure.

## Remarks

**KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS** is called with no input data. A `[KSMIDILOOPED_REGISTERS struct](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_registers.md)` is returned, containing pointers to the read and write positions that are mapped to the caller’s process space. 

### Sample Code

TBD - Better code sample then this test code?

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

| Item   | Description|
|------- |----------- |
| Version| Available in Windows 27788 (TDB) and later Windows operating systems.|
| Header | Ksmedia.h  |

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_BUFFER**](ksproperty-midiloopedstreaming-buffer.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

TBD Future links:

`[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)`

`[**KSMIDILOOPED_BUFFER_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)`

`[**KSMIDILOOPED_BUFFER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md)` 

`[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)`
