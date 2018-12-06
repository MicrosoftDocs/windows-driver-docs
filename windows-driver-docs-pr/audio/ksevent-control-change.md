---
title: KSEVENT\_CONTROL\_CHANGE
description: The KSEVENT\_CONTROL\_CHANGE event indicates that a change in control value has occurred at a node that represents a hardware volume-control knob, mute switch, or other type of manual control.Usage Summary TableTargetEvent Descriptor TypeEvent Value TypePinKSE\_NODEKSEVENTDATA The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.
ms.assetid: 32d8e14c-f21d-4bac-8d98-8aca40e30b60
keywords: ["KSEVENT_CONTROL_CHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CONTROL_CHANGE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561937" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561937)"><strong>KSE_NODE</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a KSEVENTDATA structure that specifies the type of notification to use for an event.

Requirements
------------

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


[**KSE\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff561937)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

[**PCEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537692)

[**PCEVENT\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537693)

[IPortEvents](https://msdn.microsoft.com/library/windows/hardware/ff536884)

 

 






