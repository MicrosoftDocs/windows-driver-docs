---
title: .fiber (Set Fiber Context)
description: The .fiber command specifies which fiber is used for the fiber context.
ms.assetid: 37473c90-018c-417f-a2b2-3723b9d03ca7
keywords: ["Set Fiber Context (.fiber) command", "context, Set Fiber Context (.fiber) command", "fibers", ".fiber (Set Fiber Context) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .fiber (Set Fiber Context)
api_type:
- NA
ms.localizationpriority: medium
---

# .fiber (Set Fiber Context)


The **.fiber** command specifies which fiber is used for the fiber context.

```dbgcmd
.fiber [Address]
```

## <span id="ddk_meta_set_fiber_context_dbg"></span><span id="DDK_META_SET_FIBER_CONTEXT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the fiber. If you omit this parameter or specify zero, the fiber context is reset to the current fiber.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the process context, the register context, and the local context, see [Changing Contexts](changing-contexts.md).

 

 





