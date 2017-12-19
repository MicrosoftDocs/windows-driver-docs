---
title: KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT
description: The KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT property registers a user-mode event for DMA-driven event notification.
ms.assetid: 8fd5883a-ff86-4d27-af44-a82511c9e8eb
keywords: ["KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT


The KSPROPERTY\_RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT property registers a user-mode event for DMA-driven event notification. Events must be registered after successfully calling [**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md).

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
<td align="left"><p>[<strong>KSRTAUDIO_NOTIFICATION_EVENT_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537499)</p></td>
<td align="left"><p><strong>NULL</strong></p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) consists of a KSRTAUDIO\_NOTIFICATION\_EVENT\_PROPERTY structure that contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure along with a user-mode event handle.

The property value (operation data) for this property is **NULL** because no operation data is returned.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_ RTAUDIO\_REGISTER\_NOTIFICATION\_EVENT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate failure status code. The following table shows some of the possible failure status codes.

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

 

Remarks
-------

This property is used to register user-mode events for DMA-driven event notification.

When the pin is placed into the *run* state (KSSTATE\_RUN) the registered events are signaled once or twice per cycle of the cyclic audio buffer, depending on the notification count requested when KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION was called. For more information about KSSTATERUN, see the [State Transitions](https://msdn.microsoft.com/library/windows/hardware/ff568227) topic.

After you stop the pin, and prior to the time when you close it, each registered event is unregistered via a call to [**KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT**](ksproperty-rtaudio-unregister-notification-event.md).

Requirements
------------

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


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_RTAUDIO\_BUFFER\_WITH\_NOTIFICATION**](ksproperty-rtaudio-buffer-with-notification.md)

[**KSPROPERTY\_RTAUDIO\_UNREGISTER\_NOTIFICATION\_EVENT**](ksproperty-rtaudio-unregister-notification-event.md)

[State Transitions](https://msdn.microsoft.com/library/windows/hardware/ff568227)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_RTAUDIO_REGISTER_NOTIFICATION_EVENT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





