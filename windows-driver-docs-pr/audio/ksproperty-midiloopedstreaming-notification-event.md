---
title: KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT
description: The KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property registers a user-mode event for DMA-driven event notification.
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
ms.date: 02/07/2025
---


# KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT


The KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property registers a caller created event handle in a [KSMIDILOOPED_EVENT struct](/windows-hardware/drivers/ddi/ns-ksmedia-ksmidilooped_event.md). The driver adds a reference to the handle for that event and stores it.

The following table summarizes the features of this property.

### Usage Summary Table

|Get |Set|Target|Property descriptor type    |Property value type|
|--- |--- |--- |---------------------------- |------------------ |
|Yes |Yes |Pin |[KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property) TBD ????| NULL TBD ???|

Notes:

KSPROPSETID_MidiLoopedStreaming,

KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT,

ACX_PROPERTY_ITEM_FLAG_SET,

EvtMidiSetLoopedStreamingNotificationEventCallback,

The property value (operation data) for this property is **NULL** because no operation data is returned.

### Return Value

A KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

|Status code|Meaning|
|---------- |------ |
|STATUS_UNSUCCESSFUL|A cyclic buffer with the specified combination of buffer attributes cannot be allocated.|
|STATUS_INSUFFICIENT_RESOURCES|Memory for the buffer cannot be allocated.|
|STATUS_DEVICE_NOT_READY|The device is not ready|


## Remarks

TBD

*KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT*, a member of the [KSPROPERTY_MIDILOOPEDSTREAMING enum](ne-ksmedia-ksproperty_midiloopedstreaming.md) takes in a caller created event handle in a [KSMIDILOOPED_EVENT struct](ns-ksmedia-ksmidilooped_event.md). The driver adds a reference to the handle for that event and stores it. 

### Sample Code

```cpp
TBD
```

## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_BUFFER**](ksproperty-midiloopedstreaming-buffer.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)

[**KSMIDILOOPED_BUFFER_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer_property.md)

[**KSMIDILOOPED_BUFFER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksmidilooped_buffer.md) 

[**KSPROPERTY_MIDILOOPEDSTREAMING enum**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_midiloopedstreaming.md)
