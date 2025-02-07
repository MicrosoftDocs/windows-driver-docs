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


The KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property registers a user-mode event for DMA-driven event notification. Events must be registered after successfully calling [**KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER_WITH_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md).

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property" data-raw-source="[&lt;strong&gt;KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property)"><strong>KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY</strong></a></p></td>
<td align="left"><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

        &KSPROPSETID_MidiLoopedStreaming,
        KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT,
        ACX_PROPERTY_ITEM_FLAG_SET,
        EvtMidiSetLoopedStreamingNotificationEventCallback,
        0,
        0, 

The property descriptor (instance data) consists of a KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY structure that contains a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure along with a user-mode event handle.

The property value (operation data) for this property is **NULL** because no operation data is returned.

### Return Value

A KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

|Status code|Meaning|
|---------- |------ |
|STATUS_UNSUCCESSFUL|A cyclic buffer with the specified combination of buffer attributes cannot be allocated.|
|STATUS_INSUFFICIENT_RESOURCES|Memory for the buffer cannot be allocated.|
|STATUS_DEVICE_NOT_READY|The device is not ready|


## Remarks

This property is used to register user-mode events for DMA-driven event notification.

When the pin is placed into the *run* state (KSSTATE_RUN) the registered events are signaled once or twice per cycle of the cyclic audio buffer, depending on the notification count requested when KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER_WITH_NOTIFICATION was called. For more information about KSSTATERUN, see the [State Transitions](../stream/state-transitions.md) topic.

After you stop the pin, and prior to the time when you close it, each registered event is unregistered via a call to [**KSPROPERTY_RTAUDIO_UNREGISTER_NOTIFICATION_EVENT**](ksproperty-rtaudio-unregister-notification-event.md).

## Requirements

## Requirements

|Item   | Description|
|------ |----------- |
|Version|Available in Windows 27788 (TDB) and later Windows operating systems.|
|Header |Ksmedia.h|

## See also

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_BUFFER**](ksproperty-midiloopedstreaming-buffer.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

[State Transitions](../stream/state-transitions.md)
