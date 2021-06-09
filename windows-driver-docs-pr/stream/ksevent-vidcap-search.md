---
title: KSEVENT\_VIDCAP\_SEARCH
description: The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a search has been completed.
keywords: ["KSEVENT_VIDCAP_SEARCH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAP_SEARCH
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_VIDCAP\_SEARCH


The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a search has been completed.

## <span id="ddk_ksevent_vidcap_search_ks"></span><span id="DDK_KSEVENT_VIDCAP_SEARCH_KS"></span>


### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p><a href="/previous-versions/ff561744(v=vs.85)" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](/previous-versions/ff561744(v=vs.85))"><strong>KSEVENT</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

Clients might register for this event when searching for a particular track, for instance, in order to be notified when the search completes.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).

