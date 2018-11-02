---
title: .apply_dbp (Apply Data Breakpoint to Context)
description: The .apply_dbp command applies the current process' existing data breakpoints to the specified register context.
ms.assetid: c74fd4b3-3335-4e03-a57a-6a9aa883dd9f
keywords: [".apply_dbp (Apply Data Breakpoint to Context) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- .apply_dbp (Apply Data Breakpoint to Context)
api_type:
- NA
ms.localizationpriority: medium
---

# .apply\_dbp (Apply Data Breakpoint to Context)


The **.apply\_dbp** command applies the current process' existing data breakpoints to the specified register context.

```dbgcmd
    .apply_dbp [/m Context] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________m_______Context______"></span><span id="________m_______context______"></span><span id="________M_______CONTEXT______"></span> **/m** *Context*   
Specifies the address of a register context (CONTEXT structure) in memory to which to apply the current process' data breakpoints.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode and kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live target only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about breakpoints controlled by the processor, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md). For more information about the register context (thread context), see [Register Context](changing-contexts.md#register-context).

Remarks
-------

Breakpoints that are controlled by the processor are called *data breakpoints* or *processor breakpoints*. These breakpoints are created by the [**ba (Break on Access)**](ba--break-on-access-.md) command.

These breakpoints are associated with a memory location in the address space of a specific process. The **.apply\_dbp** command modifies the specified register context so that these data breakpoints will be active when this context is used.

If the **/m** *Address* parameter is not used, data breakpoints will be applied to the current register context.

This command can only be used if the target is in native machine mode. For example, if the target is running on a 64-bit machine emulating an x86 processor using [*WOW64*](https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-wow64), this command cannot be used.

One example of a time this command is useful is when you are in an exception filter. The **.apply\_dbp** command can update the exception filter's stored context. Data breakpoints will then be applied when the exception filter exits and the stored context is resumed. Without such a modification it is possible that data breakpoints would be lost.

 

 





