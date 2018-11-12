---
title: .cxr (Display Context Record)
description: The .cxr command displays the context record saved at the specified address. It also sets the register context.
ms.assetid: 0e882639-6029-4512-8d46-050228e95cb6
keywords: ["Display Context Record (.cxr) command", "context record", ".cxr (Display Context Record) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .cxr (Display Context Record)
api_type:
- NA
ms.localizationpriority: medium
---

# .cxr (Display Context Record)


The **.cxr** command displays the context record saved at the specified address. It also sets the register context.

```dbgsyntax
.cxr [Options] [Address]  
```

## <span id="ddk_meta_display_context_record_dbg"></span><span id="DDK_META_DISPLAY_CONTEXT_RECORD_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any combination of the following options:

<span id="_f_Size"></span><span id="_f_size"></span><span id="_F_SIZE"></span>**/f** **** *Size*  
Forces the context size to equal the value of *Size*, in bytes. This can be useful when the context does not match the actual target -- for example, when using an x86 context on a 64-bit target during [*WOW64*](https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-wow64) debugging. If an invalid or inconsistent size is specified, the error "Unable to convert context to canonical form" will be displayed.

<span id="_w"></span><span id="_W"></span>**/w**  
Writes the current context to memory, and displays the address of the location where it was written.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Address of the system context record.

Omitting the address does not display any context record information, but it does reset the register context.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

The information from a context record can be used to assist in debugging a system halt where an unhandled exception has occurred and an exact stack trace is not available. The **.cxr** command displays the important registers for the specified context record.

This command also instructs the debugger to use the specified context record as the register context. After this command is executed, the debugger will have access to the most important registers and the stack trace for this thread. This register context persists until you allow the target to execute or use another register context command ([**.thread**](-thread--set-register-context-.md), [**.ecxr**](-ecxr--display-exception-context-record-.md), [**.trap**](-trap--display-trap-frame-.md) , or **.cxr** again). In user mode, it will also be reset if you change the current process or thread. See [Register Context](changing-contexts.md#register-context) for details.

The **.cxr** command is often used to debug bug check 0x1E. For more information and an example, see [**Bug Check 0x1E**](bug-check-0x1e--kmode-exception-not-handled.md) (KMODE\_EXCEPTION\_NOT\_HANDLED).

The **.cxr /w** command writes the context to memory and displays the address where it has been stored. This address can be passed to [**.apply\_dbp (Apply Data Breakpoint to Context)**](-apply-dbp--apply-data-breakpoint-to-context-.md) if you need to apply data breakpoints to this context.

 

 





