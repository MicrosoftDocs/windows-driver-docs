---
title: tb (Trace to Next Branch)
description: The tb command executes the program until a branch instruction is reached.
ms.assetid: 28b736f9-69f5-405b-9684-48b4205e7633
keywords: ["tb (Trace to Next Branch) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- tb (Trace to Next Branch)
api_type:
- NA
---

# tb (Trace to Next Branch)


The **tb** command executes the program until a branch instruction is reached.

```
    tb [r] [= StartAddress] [Count] 
```

## <span id="ddk_cmd_trace_to_next_branch_dbg"></span><span id="DDK_CMD_TRACE_TO_NEXT_BRANCH_DBG"></span>Parameters


<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the **tbr**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other four commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger starts execution. If you do not use *StartAddress*, execution begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
Specifies the number of branches to allow. Every time that a branch is encountered, the instruction address and the instruction are displayed. If you omit *Count*, the default number is 1.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p></p>
<strong>x86-based:</strong> Kernel mode only
<strong>Itanium-based:</strong> User mode, kernel mode
<strong>x64-based:</strong> User mode, kernel mode</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86-based (GenuineIntel processor family 6 and later), Itanium-based, x64-based</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about related commands, see [Controlling the Target](controlling-the-target.md).

Remarks
-------

The **tb** command causes the target to begin executing. This execution continues until a branch command is reached.

Execution stops at any branch command that is to be taken. This stopping of execution is always based on the *disassembly* code, even when the debugger is in source mode.

Branch instructions include calls, returns, jumps, counted loops, and while loops. If the debugger encounters an unconditional branch, or a conditional branch for which the condition is true, execution stops. If the debugger encounters a conditional branch whose condition is false, execution continues.

When execution stops, the address of the branch instruction and any associated symbols are displayed. This information is followed by an arrow and then the address and instructions of the new program counter location.

The **tb** command works only on the current processor. If you use **tb** on a multiprocessor system, execution stops when a branch command is reached or when another processor's event occurs, whichever comes first.

Usually, branch tracing is enabled after the processor control block (PRCB) has been initialized. (The PRCB is initialized early in the boot process.) However, if you have to use the **tb** command before this point, you can use [**.force\_tb (Forcibly Allow Branch Tracing)**](-force-tb--forcibly-allow-branch-tracing-.md) to enable branch tracing earlier. Use the **.force\_tb** command cautiously, because it can corrupt your processor state.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20tb%20%28Trace%20to%20Next%20Branch%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




