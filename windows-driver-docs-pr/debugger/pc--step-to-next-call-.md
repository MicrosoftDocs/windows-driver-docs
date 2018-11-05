---
title: pc (Step to Next Call)
description: The pc command executes the program until a call instruction is reached.
ms.assetid: 4b9b786c-2ecc-44a6-a82b-0641d7991abc
keywords: ["pc (Step to Next Call) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pc (Step to Next Call)
api_type:
- NA
ms.localizationpriority: medium
---

# pc (Step to Next Call)


The **pc** command executes the program until a call instruction is reached.

User-Mode

```dbgcmd
[~Thread] pc [r] [= StartAddress] [Count] 
```

Kernel-Mode

```dbgcmd
pc [r] [= StartAddress] [Count] 
```

## <span id="ddk_cmd_step_to_next_call_dbg"></span><span id="DDK_CMD_STEP_TO_NEXT_CALL_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to continue executing. All other threads are frozen. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the **pcr**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. Otherwise, the debugger begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of **call** instructions that the debugger must encounter for this command to stop. The default value is one.

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

The **pc** command causes the target to begin executing. This execution continues until a **call** instruction is reached or a breakpoint is encountered.

If the program counter is already on a **call** instruction, the entire call is executed. After this call is returned, execution continues until another **call** is reached. This execution, rather than tracing, of the call is the only difference between **pc** and [**tc (Trace to Next Call)**](tc--trace-to-next-call-.md).

In source mode, you can associate one source line with multiple assembly instructions. The **pc** command does not stop at a **call** instruction that is associated with the current source line.

 

 





