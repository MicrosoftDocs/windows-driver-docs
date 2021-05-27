---
title: KSEVENT\_PINCAPS\_FORMATCHANGE
description: The KSEVENT\_PINCAPS\_FORMATCHANGE event indicates to the audio stack that the audio data format for the audio device has changed.
keywords: ["KSEVENT_PINCAPS_FORMATCHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_PINCAPS_FORMATCHANGE
api_location:
- Ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="/previous-versions/ff561744(v=vs.85)" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](/previous-versions/ff561744(v=vs.85))"><strong>KSEVENT</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

## Remarks

When an audio port driver calls the [**EventHandler**](/windows-hardware/drivers/ddi/portcls/nc-portcls-pcpfnevent_handler) routine for its miniport driver, it passes a [**PCEVENT\_REQUEST**](/windows-hardware/drivers/ddi/portcls/ns-portcls-_pcevent_request) structure. This structure contains a pointer to a [**PCEVENT\_ITEM**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcevent_item) structure that is used to describe an event that is supported by a filter, pin, or node.

So, for example, a driver that supports the `KSEVENT_PINCAPS_FORMATCHANGE` event must populate a **PCEVENT\_ITEM** structure as follows:

```cpp
static PCEVENT_ITEM FormatChangePinEvent[] = {
  {
    &KSEVENTSETID_PinCapsChange,
    KSEVENT_PINCAPS_FORMATCHANGE,
    KSEVENT_TYPE_ENABLE | KSEVENT_TYPE_BASICSUPPORT,
    MyEventHandler
  }
};
```

In the preceding code example, the MyEventHandler custom event handler must monitor the `KSEVENT_PINCAPS_FORMATCHANGE` event and register it with Portcls when KSEVENT\_PINCAPS\_FORMATCHANGE is triggered. The miniport driver must call the [**IPortEvents::AddEventToEventList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportevents-addeventtoeventlist) method to register the event.

To obtain a description of the pins, nodes, connections and properties supported by the miniport driver, the port driver calls the [**IMiniport::GetDescription**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-getdescription) method. This method call returns a [**PCFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcfilter_descriptor) structure that points to an automation table ([**PCAUTOMATION\_TABLE**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcautomation_table)). The **PCAUTOMATION\_TABLE** structure has an **Events** member. This member points to an array of the events that are associated with the filter that the miniport driver supports. So you must set the **Events** member to point to the event array that contains the **PCEVENT\_ITEM** structure for the `KSEVENT_PINCAPS_FORMATCHANGE` event.

When the miniport driver detects a dynamic format change, it must call the [**IPortEvents::GenerateEventList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportevents-generateeventlist) method to signal the `KSEVENT_PINCAPS_FORMATCHANGE` event.

## Requirements

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


[**EventHandler**](/windows-hardware/drivers/ddi/portcls/nc-portcls-pcpfnevent_handler)

[**IMiniport::GetDescription**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiport-getdescription)

[**IPortEvents::AddEventToEventList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportevents-addeventtoeventlist)

[**IPortEvents::GenerateEventList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportevents-generateeventlist)

[**KSEVENT**](/previous-versions/ff561744(v=vs.85))

[**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)

[**PCAUTOMATION\_TABLE**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcautomation_table)

[**PCEVENT\_ITEM**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcevent_item)

[**PCEVENT\_REQUEST**](/windows-hardware/drivers/ddi/portcls/ns-portcls-_pcevent_request)

[**PCFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcfilter_descriptor)

