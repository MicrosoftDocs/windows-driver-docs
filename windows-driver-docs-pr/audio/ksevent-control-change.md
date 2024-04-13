---
title: KSEVENT\_CONTROL\_CHANGE
description: The KSEVENT\_CONTROL\_CHANGE event indicates that a change in control value has occurred at a node that represents a hardware volume-control knob, mute switch, or other type of manual control.Usage Summary TableTargetEvent Descriptor TypeEvent Value TypePinKSE\_NODEKSEVENTDATA The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.
keywords: ["KSEVENT_CONTROL_CHANGE Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSEVENT_CONTROL_CHANGE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---

# KSEVENT\_CONTROL\_CHANGE


The KSEVENT\_CONTROL\_CHANGE event indicates that a change in control value has occurred at a node that represents a hardware volume-control knob, mute switch, or other type of manual control.

**Usage Summary Table**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Target</th>
<th align="left">Event Descriptor Type</th>
<th align="left">Event Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kse_node" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)"><strong>KSE_NODE</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSE\_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)

[**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)

[**PCEVENT\_ITEM**](/windows-hardware/drivers/ddi/portcls/ns-portcls-pcevent_item)

[**PCEVENT\_REQUEST**](/windows-hardware/drivers/ddi/portcls/ns-portcls-_pcevent_request)

[IPortEvents](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportevents)

