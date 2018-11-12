---
title: .excr (Display Exception Context Record)
description: The .excr command displays the context record that is associated with the current exception.
ms.assetid: 18FD32B9-93DE-4E23-A73C-18CC3665417A
keywords: [".excr (Display Exception Context Record) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .excr (Display Exception Context Record)
api_type:
- NA
ms.localizationpriority: medium
---

# .excr (Display Exception Context Record)


The **.excr** command displays the context record that is associated with the current exception.

```dbgcmd
.excr
```

## <span id="ddk_meta_display_exception_context_record_dbg"></span><span id="DDK_META_DISPLAY_EXCEPTION_CONTEXT_RECORD_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Crash dump only (minidumps only)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

The **.excr** command locates the current exception's context information and displays the important registers for the specified context record.

This command also instructs the debugger to use the context record that is associated with the current exception as the register context. After you run **.excr**, the debugger can access the most important registers and the stack trace for this thread. This register context persists until you enable the target to execute, change the current process or thread, or use another register context command ([**.cxr**](-cxr--display-context-record-.md) or **.excr**). For more information about register contexts, see [Register Context](changing-contexts.md#register-context).

The [**.ecxr**](-ecxr--display-exception-context-record-.md) command is a synonym command and has identical functionality.

## <span id="see_also"></span>See also


[**.ecxr**](-ecxr--display-exception-context-record-.md)

 

 






