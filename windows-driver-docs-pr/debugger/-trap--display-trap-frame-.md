---
title: .trap (Display Trap Frame)
description: The .trap command displays the trap frame register state and also sets the register context.
ms.assetid: c53177ad-243c-4276-8602-2edc14b44251
keywords: ["Display Trap Frame (.trap) command", "trap frame", ".trap (Display Trap Frame) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .trap (Display Trap Frame)
api_type:
- NA
ms.localizationpriority: medium
---

# .trap (Display Trap Frame)


The **.trap** command displays the trap frame register state and also sets the register context.

```dbgcmd
.trap [Address]
```

## <span id="ddk_meta_display_trap_frame_dbg"></span><span id="DDK_META_DISPLAY_TRAP_FRAME_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Hexadecimal address of the trap frame on the target system. Omitting the address does not display any trap frame information, but it does reset the register context.

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
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

The **.trap** command displays the important registers for the specified trap frame.

This command also instructs the kernel debugger to use the specified context record as the register context. After this command is executed, the debugger will have access to the most important registers and the stack trace for this thread. This register context persists until you allow the target to execute or use another register context command ([**.thread**](-thread--set-register-context-.md), [**.cxr**](-cxr--display-context-record-.md), or **.trap**). See [Register Context](changing-contexts.md#register-context) for full details.

This extension is commonly used when debugging bug check 0xA and 0x7F. For details and an example, see [**Bug Check 0xA**](bug-check-0xa--irql-not-less-or-equal.md) (IRQL\_NOT\_LESS\_OR\_EQUAL).

 

 





