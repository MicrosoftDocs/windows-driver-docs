---
title: pa (Step to Address)
description: The pa command executes the program until the specified address is reached, displaying each step.
ms.assetid: 497261a9-69fb-4df2-b342-cd62bda8a51f
keywords: ["pa (Step to Address) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- pa (Step to Address)
api_type:
- NA
---

# pa (Step to Address)


The **pa** command executes the program until the specified address is reached, displaying each step.

User-Mode

```
[~Thread] pa [r] [= StartAddress] StopAddress ["Command"]
```

Kernel-Mode

```
    pa [r] [= StartAddress] StopAddress ["Command"]
```

## <span id="ddk_cmd_step_to_address_dbg"></span><span id="DDK_CMD_STEP_TO_ADDRESS_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies threads to continue executing. All other threads are frozen. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______r______"></span><span id="_______R______"></span> **r**   
Turns on and off the display of registers and flags. By default, the registers and flags are displayed. You can disable register display by using the **par**, [**pr**](p--step-.md), [**tr**](t--trace-.md), or .prompt\_allow -reg commands. All of these commands control the same setting and you can use any of them to override any previous use of these commands.

You can also disable register display by using the l-os command. This setting is separate from the other three commands. To control which registers and flags are displayed, use the [**rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the address where the debugger begins execution. Otherwise, the debugger begins at the instruction that the instruction pointer points to. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______StopAddress______"></span><span id="_______stopaddress______"></span><span id="_______STOPADDRESS______"></span> *StopAddress*   
Specifies the address where execution will stop. This address must match the exact address of an instruction.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies a debugger command to execute after the step is performed. This command is executed before the standard **pa** results are displayed. If you also use *StopAddress*, the specified command is executed after *StopAddress* is reached (but before the results from the final step are displayed).

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

The **pa** command causes the target to begin executing. This execution continues until the specified instruction is reached or a breakpoint is encountered.

**Note**   If you use this command in kernel mode, execution stops when an instruction is encountered at the specified virtual address in any virtual address space.

 

During this execution, all steps are displayed explicitly. Called functions are treated as a single unit. Therefore, the display of this command is similar to what you see if you execute [**p (Step)**](p--step-.md) repeatedly until the program counter reaches the specified address.

For example, the following command explicitly steps through the target code until the return address of the current function is reached.

```
0:000> pa @$ra 
```

The following example demonstrates using the **pa** command along with the **kb** command to display the stack trace:

```
0:000> pa 70b5d2f1 "kb"
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20pa%20%28Step%20to%20Address%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




