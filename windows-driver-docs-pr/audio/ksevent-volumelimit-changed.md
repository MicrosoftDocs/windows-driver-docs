---
title: KSEVENT\_VOLUMELIMIT\_CHANGED
description: The KSEVENT\_VOLUMELIMIT\_CHANGED event indicates to the audio stack that the audio volume level limit for the audio device has changed.
ms.assetid: CC6A6027-03CA-4D2C-8AA2-155E1617E19B
keywords: ["KSEVENT_VOLUMELIMIT_CHANGED Audio Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VOLUMELIMIT_CHANGED
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_VOLUMELIMIT\_CHANGED


The KSEVENT\_VOLUMELIMIT\_CHANGED event indicates to the audio stack that the audio volume level limit for the audio device has changed.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561744" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561744)"><strong>KSEVENT</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

Remarks
-------

For information about how to implement support for the KSEVENT\_PINCAPS\_VOLUMELIMITCHANGE event, see the **Remarks** section of [**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md).

Note that while KSEVENT\_PINCAPS\_FORMATCHANGE is implemented on the Wave filter (for miniport drivers that are linked to Portcls), the KSEVENT\_VOLUMELIMIT\_CHANGED event is implemented on the Topology filter.

## <span id="see_also"></span>See also


[**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744)

[**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

 

 






