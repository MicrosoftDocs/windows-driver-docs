---
title: .tss (Display Task State Segment)
description: The .tss command displays a formatted view of the saved Task State Segment (TSS) information for the current processor.
ms.assetid: 3f73b7cf-56a8-434a-bc4d-2e8ab3af9f94
keywords: ["Display Task State Segment (.tss) command", "task state segment (TSS)", "TSS (task state segment)", ".tss (Display Task State Segment) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .tss (Display Task State Segment)
api_type:
- NA
ms.localizationpriority: medium
---

# .tss (Display Task State Segment)


The **.tss** command displays a formatted view of the saved Task State Segment (TSS) information for the current processor.

```dbgcmd
.tss [Address]
```

## <span id="ddk_meta_display_task_state_segment_dbg"></span><span id="DDK_META_DISPLAY_TASK_STATE_SEGMENT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Address of the TSS.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86 only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The address of the TSS can be found by examining the output of the [**!pcr**](-pcr.md) extension.

 

 





