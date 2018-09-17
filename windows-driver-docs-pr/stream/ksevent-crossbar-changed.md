---
title: KSEVENT\_CROSSBAR\_CHANGED
description: The KSEVENT\_CROSSBAR\_CHANGED event propagates an action, such as a new routing configuration, from the kernel-mode video capture minidriver to DirectShow in user-mode.
ms.assetid: b67d95a3-7c30-49ae-a2df-eb88491c2e97
keywords: ["KSEVENT_CROSSBAR_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CROSSBAR_CHANGED
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSEVENT\_CROSSBAR\_CHANGED


The KSEVENT\_CROSSBAR\_CHANGED event propagates an action, such as a new routing configuration, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## <span id="ddk_ksevent_crossbar_changed_ks"></span><span id="DDK_KSEVENT_CROSSBAR_CHANGED_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSE_NODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561937)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 





