---
title: KSEVENT\_VIDCAP\_SEARCH
description: The KSEVENT\_VIDCAP\_AUTO\_UPDATE event is triggered when a search has been completed.
ms.assetid: 07c7ef26-4f88-40cf-84f2-14cc702f37d5
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561744" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561744)"><strong>KSEVENT</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Clients might register for this event when searching for a particular track, for instance, in order to be notified when the search completes.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 





