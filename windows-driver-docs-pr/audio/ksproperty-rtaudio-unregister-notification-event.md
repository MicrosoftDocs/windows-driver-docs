---
title: KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT
description: The KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT property unregisters a user-mode event from DMA-driven event notification.The following table summarizes the features of this property.
keywords: ["KSPROPERTY_RTAUDIO_UNREGISTER_NOTIFICATION_EVENT Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_RTAUDIO_UNREGISTER_NOTIFICATION_EVENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT


The KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT property unregisters a user-mode event from DMA-driven event notification.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property" data-raw-source="[&lt;strong&gt;KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property)"><strong>KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY</strong></a></p></td>
<td align="left"><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSRTAUDIO\_NOTIFICATION\_EVENT\_PROPERTY structure that contains a [**KSPROPERTY**](../stream/ksproperty-structure.md) structure along with a user-mode event handle.

The property value (operation data) for this property is **NULL** because no operation data is returned.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_ RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

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
<td align="left"><p>STATUS_NOT_SUPPORTED</p></td>
<td align="left"><p>Event notifications are not supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td align="left"><p>Memory for the buffer cannot be allocated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_NOT_READY</p></td>
<td align="left"><p>The device is not ready.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This property is used to unregister user-mode events from DMA-driven event notification.

When the pin is placed into the run state (KSSTATE\_RUN) the registered events are signaled once or twice per cycle of the cyclic audio buffer, depending on the notification count requested when [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md) was called. For more information about KSSTATE\_RUN, see the [State Transitions](../stream/state-transitions.md) topic.

After you stop the pin and prior to the step where you close it, each registered event must be unregistered via a call to KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT.

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](../stream/ksproperty-structure.md)

[**KSRTAUDIO\_NOTIFICATION\_EVENT\_PROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksrtaudio_notification_event_property)

[**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md)

[**KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT**](ksproperty-rtaudio-register-notification-event.md)
