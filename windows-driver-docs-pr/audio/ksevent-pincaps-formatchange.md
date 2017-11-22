---
title: KSEVENT\_PINCAPS\_FORMATCHANGE
description: The KSEVENT\_PINCAPS\_FORMATCHANGE event indicates to the audio stack that the audio data format for the audio device has changed.
ms.assetid: ca9ee246-7fca-42df-89e0-7ace6b1f808a
keywords: ["KSEVENT_PINCAPS_FORMATCHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_PINCAPS_FORMATCHANGE
api_location:
- Ks.h
api_type:
- HeaderDef
---

# KSEVENT\_PINCAPS\_FORMATCHANGE


The `KSEVENT_PINCAPS_FORMATCHANGE` event indicates to the audio stack that the audio data format for the audio device has changed.

### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span> Usage Summary Table

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target</th>
<th align="left">Event descriptor type</th>
<th align="left">Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pin</p></td>
<td align="left"><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td align="left"><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

Remarks
-------

When an audio port driver calls the [**EventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff536374) routine for its miniport driver, it passes a [**PCEVENT\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537693) structure. This structure contains a pointer to a [**PCEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537692) structure that is used to describe an event that is supported by a filter, pin, or node.

So, for example, a driver that supports the `KSEVENT_PINCAPS_FORMATCHANGE` event must populate a **PCEVENT\_ITEM** structure as follows:

```
static PCEVENT_ITEM FormatChangePinEvent[] = {
  {
    &amp;KSEVENTSETID_PinCapsChange,
    KSEVENT_PINCAPS_FORMATCHANGE,
    KSEVENT_TYPE_ENABLE | KSEVENT_TYPE_BASICSUPPORT,
    MyEventHandler
  }
};
```

In the preceding code example, the MyEventHandler custom event handler must monitor the `KSEVENT_PINCAPS_FORMATCHANGE` event and register it with Portcls when KSEVENT\_PINCAPS\_FORMATCHANGE is triggered. The miniport driver must call the [**IPortEvents::AddEventToEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536886) method to register the event.

To obtain a description of the pins, nodes, connections and properties supported by the miniport driver, the port driver calls the [**IMiniport::GetDescription**](https://msdn.microsoft.com/library/windows/hardware/ff536765) method. This method call returns a [**PCFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537694) structure that points to an automation table ([**PCAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff537685)). The **PCAUTOMATION\_TABLE** structure has an **Events** member. This member points to an array of the events that are associated with the filter that the miniport driver supports. So you must set the **Events** member to point to the event array that contains the **PCEVENT\_ITEM** structure for the `KSEVENT_PINCAPS_FORMATCHANGE` event.

When the miniport driver detects a dynamic format change, it must call the [**IPortEvents::GenerateEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536889) method to signal the `KSEVENT_PINCAPS_FORMATCHANGE` event.

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
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**EventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff536374)

[**IMiniport::GetDescription**](https://msdn.microsoft.com/library/windows/hardware/ff536765)

[**IPortEvents::AddEventToEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536886)

[**IPortEvents::GenerateEventList**](https://msdn.microsoft.com/library/windows/hardware/ff536889)

[**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

[**PCAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff537685)

[**PCEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537692)

[**PCEVENT\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537693)

[**PCFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537694)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENT_PINCAPS_FORMATCHANGE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





