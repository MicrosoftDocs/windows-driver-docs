---
title: KSEVENT\_TVAUDIO\_CHANGED
description: The KSEVENT\_TVAUDIO\_CHANGED event propagates an action, such as a newly tuned-to channel supports stereo audio, from the kernel-mode video capture minidriver to DirectShow in user-mode.
ms.assetid: 98d77001-9844-4893-9a23-9c06f7d75841
keywords: ["KSEVENT_TVAUDIO_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_TVAUDIO_CHANGED
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_TVAUDIO\_CHANGED


The KSEVENT\_TVAUDIO\_CHANGED event propagates an action, such as a newly tuned-to channel supports stereo audio, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## <span id="ddk_ksevent_tvaudio_changed_ks"></span><span id="DDK_KSEVENT_TVAUDIO_CHANGED_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561937" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561937)"><strong>KSE_NODE</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 





