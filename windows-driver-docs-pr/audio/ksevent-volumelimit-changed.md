---
title: KSEVENT\_VOLUMELIMIT\_CHANGED
description: The KSEVENT\_VOLUMELIMIT\_CHANGED event indicates to the audio stack that the audio volume level limit for the audio device has changed.
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
<td align="left"><p><a href="/previous-versions/ff561744(v=vs.85)" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](/previous-versions/ff561744(v=vs.85))"><strong>KSEVENT</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The event value type (operation data) is a **KSEVENTDATA** structure that specifies the notification method to use for this event.

## Remarks

For information about how to implement support for the KSEVENT\_PINCAPS\_VOLUMELIMITCHANGE event, see the **Remarks** section of [**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md).

Note that while KSEVENT\_PINCAPS\_FORMATCHANGE is implemented on the Wave filter (for miniport drivers that are linked to Portcls), the KSEVENT\_VOLUMELIMIT\_CHANGED event is implemented on the Topology filter.

## <span id="see_also"></span>See also


[**KSEVENT**](/previous-versions/ff561744(v=vs.85))

[**KSEVENT\_PINCAPS\_FORMATCHANGE**](ksevent-pincaps-formatchange.md)

[**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)

