---
title: KSEVENT\_VIDEODECODER\_CHANGED
description: The KSEVENT\_VIDEODECODER\_CHANGED event propagates an action, such as the selection of a new physical input connector, from the kernel-mode video capture minidriver to DirectShow in user-mode.
keywords: ["KSEVENT_VIDEODECODER_CHANGED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDEODECODER_CHANGED
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_VIDEODECODER\_CHANGED


The KSEVENT\_VIDEODECODER\_CHANGED event propagates an action, such as the selection of a new physical input connector, from the kernel-mode video capture minidriver to DirectShow in user-mode.

## <span id="ddk_ksevent_videodecoder_changed_ks"></span><span id="DDK_KSEVENT_VIDEODECODER_CHANGED_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kse_node" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)"><strong>KSE_NODE</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).

