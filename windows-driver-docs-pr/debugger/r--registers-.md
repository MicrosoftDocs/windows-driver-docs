---
title: r (Registers)
description: The r command displays or modifies registers, floating-point registers, flags, pseudo-registers, and fixed-name aliases.
ms.assetid: c0d0af2f-1852-47a4-8f01-95f6ec198112
keywords: ["r (Registers) Windows Debugging"]
ms.author: domars
ms.date: 07/11/2018
topic_type:
- apiref
api_name:
- r (Registers)
api_type:
- NA
ms.localizationpriority: medium
---

# r (Registers)


The **r** command displays or modifies registers, floating-point registers, flags, pseudo-registers, and fixed-name aliases.

User-Mode

```dbgcmd
[~Thread] r[M Mask|F|X|?] [ Register[:[Num]Type] [= [Value]] ] 
r.
```

Kernel-Mode

```dbgcmd
[Processor] r[M Mask|F|X|Y|YI|?] [ Register[:[Num]Type] [= [Value]] ] 
r.
```

## <span id="ddk_cmd_registers_dbg"></span><span id="DDK_CMD_REGISTERS_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor that the registers are read from. The default value is zero. If you specify *Processor*, you cannot include the *Register* parameter--all registers are displayed. For more information about the syntax, see [Multiprocessor Syntax](multiprocessor-syntax.md). You can specify processors only in kernel mode.

<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread that the registers are read from. If you do not specify a thread, the current thread is used. For more information about the syntax, see [Thread Syntax](thread-syntax.md). You can specify threads only in user mode.

<span id="_______M_______Mask______"></span><span id="_______m_______mask______"></span><span id="_______M_______MASK______"></span> **M** *Mask*   
Specifies the mask to use when the debugger displays the registers. The "M" must be an uppercase letter. *Mask* is a sum of bits that indicate something about the register display. The meaning of the bits depends on the processor and the mode (see the tables in the following Remarks section for more information). If you omit **M**, the default mask is used. You can set or display the default mask by using the [**Rm (Register Mask)**](rm--register-mask-.md) command.

<span id="_______F______"></span><span id="_______f______"></span> **F**   
Displays the floating-point registers. The "F" must be an uppercase letter. This option is equivalent to **M 0x4**.

<span id="_______X______"></span><span id="_______x______"></span> **X**   
Displays the SSE XMM registers. This option is equivalent to **M 0x40**.

<span id="_______Y______"></span><span id="_______y______"></span> **Y**   
Displays the AVX YMM registers. This option is equivalent to **M 0x200**.

<span id="_______YI______"></span><span id="_______yi______"></span> **YI**   
Displays the AVX YMM integer registers. This option is equivalent to **M 0x400**.

<span id="_______YI______"></span><span id="_______yi______"></span> **Z**   
Displays the AVX-512 YMM registers (zmm0-zmm31) in floating point format. 

<span id="_______YI______"></span><span id="_______yi______"></span> **ZI**   
Displays the AVX-512 YMM registers (zmm0-zmm31) in integer format. 

<span id="_______YI______"></span><span id="_______yi______"></span> **K**   
Display the AVX-512 Opmask predicate registers (K0-K7).

<span id="______________"></span> **?**   
(Pseudo-register assignment only) Causes the pseudo-register to acquire typed information. Any type is permitted. For more information about the **r?** syntax, see [Debugger Command Program Examples](debugger-command-program-examples.md).

<span id="_______Register______"></span><span id="_______register______"></span><span id="_______REGISTER______"></span> *Register*   
Specifies the register, flag, pseudo-register, or fixed-name alias to display or modify. You must not precede this parameter with at (**@**) sign. For more information about the syntax, see [Register Syntax](register-syntax.md).

<span id="_______Num______"></span><span id="_______num______"></span><span id="_______NUM______"></span> *Num*   
Specifies the number of elements to display. If you omit this parameter but you include *Type*, the full register length is displayed.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the data format to display each register element in. You can use *Type* only with 64-bit and 128-bit vector registers. You can specify multiple types.

You can specify one or more of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"><em>Type</em></th>
<th align="left">Display format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ib</strong></p></td>
<td align="left"><p>Signed byte</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ub</strong></p></td>
<td align="left"><p>Unsigned byte</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>iw</strong></p></td>
<td align="left"><p>Signed word</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>uw</strong></p></td>
<td align="left"><p>Unsigned word</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>id</strong></p></td>
<td align="left"><p>Signed DWORD</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ud</strong></p></td>
<td align="left"><p>Unsigned DWORD</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>iq</strong></p></td>
<td align="left"><p>Signed quad-word</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>uq</strong></p></td>
<td align="left"><p>Unsigned quad-word</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>f</strong></p></td>
<td align="left"><p>32-bit floating-point</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>d</strong></p></td>
<td align="left"><p>64-bit floating-point</p></td>
</tr>
</tbody>
</table>

 

<span id="_______Value______"></span><span id="_______value______"></span><span id="_______VALUE______"></span> *Value*   
Specifies the value to assign to the register. For more information about the syntax, see [Numerical Expression Syntax](numerical-expression-syntax.md).

 **.**   
Displays the registers used in the current instruction. If no registers are used, no output is displayed.

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

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

If you do not specify *Register*, the **r** command displays all the non-floating-point registers, and the **rF** command displays all the floating-point registers. You can change this behavior by using the [**rm (Register Mask)**](rm--register-mask-.md) command.

If you specify *Register* but you omit the equal sign (=) and the *Value* parameter, the command displays the current value of the register.

If you specify *Register* and an equal sign (=) but you omit *Value*, the command displays the current value of the register and prompts for a new value.

If you specify *Register*, the equal sign (=), and *Value*, the command changes the register to contain the value. (If *quiet mode* is active, you can omit the equal sign. You can turn on quiet mode by using the [**sq (Set Quiet Mode)**](sq--set-quiet-mode-.md) command. In kernel mode, you can also turn on quiet mode by using the KDQUIET [environment variable](kernel-mode-environment-variables.md).)

You can specify multiple registers, separated by commas.

In user mode, the **r** command displays registers that are associated with the current thread. For more information about the threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

In kernel mode, the **r** command displays registers that are associated with the current *register context*. You can set the register context to match a specific thread, context record, or trap frame. Only the most important registers for the specified register context are actually displayed, and you cannot change their values. For more information about register context, see [Register Context](changing-contexts.md#register-context).

When you specify a floating-point register by name, the **F** option is not required. When you specify a single floating-point register, the raw hexadecimal value is displayed in addition to the decimal value.

The following *Mask* bits are supported for an x86-based processor or an x64-based processor.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
0
1</td>
<td align="left"><p></p>
0x1
0x2</td>
<td align="left"><p>Displays the basic integer registers. (Setting one or both of these bits has the same effect.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0x4</p></td>
<td align="left"><p>Displays the floating-point registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0x8</p></td>
<td align="left"><p>Displays the segment registers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0x10</p></td>
<td align="left"><p>Displays the MMX registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>0x20</p></td>
<td align="left"><p>Displays the debug registers. In kernel mode, setting this bit also displays the CR4 register.</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>0x40</p></td>
<td align="left"><p>Displays the SSE XMM registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>0x80</p></td>
<td align="left"><p>(Kernel mode only) Displays the control registers, for example CR0, CR2, CR3 and CR8.</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>0x100</p></td>
<td align="left"><p>(Kernel mode only) Displays the descriptor and task state registers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>9</p></td>
<td align="left"><p>0x200</p></td>
<td align="left"><p>Displays the AVX YMM registers in floating point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>10</p></td>
<td align="left"><p>0x400</p></td>
<td align="left"><p>Displays the AVX YMM registers in decimal integers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>11</p></td>
<td align="left"><p>0x800</p></td>
<td align="left"><p>Displays the AVX XMM registers in decimal integers.</p></td>
</tr>
</tbody>
</table>


 

The following code examples show **r** commands for an x86-based processor.

In kernel mode, the following command shows the registers for processor 2.

```dbgcmd
1: kd> 2r 
```

In user mode, the following command shows the registers for thread 2.

```dbgcmd
0:000> ~2 r 
```

In user mode, the following command displays all of the **eax** registers that are associated with all threads (in thread index order).

```dbgcmd
0:000> ~* r eax
```

The following command sets the **eax** register for the current thread to 0x000000FF.

```dbgcmd
0:000> r eax=0x000000FF
```

The following command sets the **st0** register to 1.234e+10 (the **F** is optional).

```dbgcmd
0:000> rF st0=1.234e+10
```

The following command displays the zero flag.

```dbgcmd
0:000> r zf 
```

The following command displays the **xmm0** register as 16 unsigned bytes and then displays the full contents of the **xmm1** register in double-precision floating-point format.

```dbgcmd
0:000> r xmm0:16ub, xmm1:d 
```

If the current syntax is C++, you must precede registers by an at sign (**@**). Therefore, you could use the following command to copy the **ebx** register to the **eax** register.

```dbgcmd
0:000> r eax = @ebx
```

The following command displays pseudo-registers in the same way that the **r** command displays registers.

```dbgcmd
0:000> r $teb
```

You can also use the **r** command to create *fixed-name aliases*. These aliases are not registers or pseudo-registers, even though they are associated with the **r** command. For more information about these aliases, see [Using Aliases](using-aliases.md).

Here is an example of the **r.** command on an x86-based processor. The last entry of the call stack precedes the command itself.

```dbgcmd
01004af3 8bec            mov     ebp,esp
0:000> r.
ebp=0006ffc0  esp=0006ff7c
```


 

 





