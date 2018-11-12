---
title: .force_tb (Forcibly Allow Branch Tracing)
description: The .force_tb command forces the processor to trace branches early in the boot process.
ms.assetid: ac4aabfa-6d00-4478-9c13-213bf89f613a
keywords: [".force_tb (Forcibly Allow Branch Tracing) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .force_tb (Forcibly Allow Branch Tracing)
api_type:
- NA
ms.localizationpriority: medium
---

# .force\_tb (Forcibly Allow Branch Tracing)


The **.force\_tb** command forces the processor to trace branches early in the boot process.

```dbgcmd
.force_tb 
```

## <span id="ddk_meta_forcibly_allow_branch_tracing_dbg"></span><span id="DDK_META_FORCIBLY_ALLOW_BRANCH_TRACING_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Typically, branch tracing is enabled after the debugger initializes the processor control block (PRCB). This initialization occurs early in the boot process.

However, if you have to use the [**tb (Trace to Next Branch)**](tb--trace-to-next-branch-.md) command before this initialization, you can use the **.force\_tb** command to enable branch tracing earlier. Use this command carefully because it can corrupt your processor state.

 

 





