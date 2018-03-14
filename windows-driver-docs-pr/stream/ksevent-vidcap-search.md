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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>KSEVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561744)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Clients might register for this event when searching for a particular track, for instance, in order to be notified when the search completes.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 





