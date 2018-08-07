---
title: KSEVENT\_TUNER\_CHANGED
description: The KSEVENT\_TUNER\_CHANGED event propagates an action, such as a channel change, from the kernel-mode video capture minidriver to DirectShow in user-mode.
ms.assetid: 7286e36c-a433-40a0-9281-7eac4ab64cbf
keywords: ["KSEVENT_TUNER_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_TUNER_CHANGED
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSEVENT\_TUNER\_CHANGED


The KSEVENT\_TUNER\_CHANGED event propagates an action, such as a channel change, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## <span id="ddk_ksevent_tuner_changed_ks"></span><span id="DDK_KSEVENT_TUNER_CHANGED_KS"></span>


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

 

 





