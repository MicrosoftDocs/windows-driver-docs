---
title: Pseudo-Register Syntax
description: Pseudo-Register Syntax
ms.assetid: f7dc52ea-e97e-4251-a517-c115cbc7d056
keywords: ["pseudo-registers", "pseudo-registers, automatic", "pseudo-registers, user defined", "registers, pseudo-registers", "loop variables", "return address", "$to to $t19 pseudo-registers", "$bp ID pseudo-register", "$ea"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Pseudo-Register Syntax


## <span id="ddk_pseudo_register_syntax_dbg"></span><span id="DDK_PSEUDO_REGISTER_SYNTAX_DBG"></span>


The debugger supports several pseudo-registers that hold certain values.

The debugger sets *automatic pseudo-registers* to certain useful values. *User-defined pseudo-registers* are integer variables that you can write to or read.

All pseudo-registers begin with a dollar sign (**$**). If you are using MASM syntax, you can add an at sign ( **@** ) before the dollar sign. This at sign tells the debugger that the following token is a register or pseudo-register, not a symbol. If you omit the at sign, the debugger responds more slowly, because it has to search the whole symbol table.

For example, the following two commands produce the same output, but the second command is faster.

```dbgcmd
0:000> ? $exp
Evaluate expression: 143 = 0000008f
0:000> ? @$exp
Evaluate expression: 143 = 0000008f
```

If a symbol exists with the same name as the pseudo-register, you must add the at sign.

If you are using C++ expression syntax, the at sign ( **@** ) is always required.

The [**r (Registers)**](r--registers-.md) command is an exception to this rule. The debugger always interprets its first argument as a register or pseudo-register. (An at sign is not required or permitted.) If there is a second argument for the **r** command, it is interpreted according to the default expression syntax. If the default expression syntax is C++, you must use the following command to copy the **$t2** pseudo-register to the **$t1** pseudo-register.

```dbgcmd
0:000> r $t1 = @$t2
```

### <span id="automatic_pseudo_registers"></span><span id="AUTOMATIC_PSEUDO_REGISTERS"></span>Automatic Pseudo-Registers

The debugger automatically sets the following pseudo-registers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Pseudo-register</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>$ea</strong></p></td>
<td align="left"><p>The effective address of the last instruction that was executed. If this instruction does not have an effective address, the debugger displays &quot;Bad register error&quot;. If this instruction has two effective addresses, the debugger displays the first address.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$ea2</strong></p></td>
<td align="left"><p>The second effective address of the last instruction that was executed. If this instruction does not have two effective addresses, the debugger displays &quot;Bad register error&quot;.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exp</strong></p></td>
<td align="left"><p>The last expression that was evaluated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$ra</strong></p></td>
<td align="left"><p>The return address that is currently on the stack.</p>
<p>This address is especially useful in execution commands. For example, <strong>g @$ra</strong> continues until the return address is found (although <strong><a href="gu--go-up-.md" data-raw-source="[gu (Go Up)](gu--go-up-.md)">gu (Go Up)</a></strong> is a more precise effective way of &quot;stepping out&quot; of the current function).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$ip</strong></p></td>
<td align="left"><p>The instruction pointer register.</p>
<p></p>
<strong>x86-based processors:</strong> The same as <strong>eip</strong>.
<strong>Itanium-based processors:</strong> Related to <strong>iip</strong>. (For more information, see the note following this table.)
<strong>x64-based processors:</strong> The same as <strong>rip</strong>.</td>
</tr>
<tr class="even">
<td align="left"><p><strong>$eventip</strong></p></td>
<td align="left"><p>The instruction pointer at the time of the current event. This pointer typically matches <strong>$ip</strong>, unless you switched threads or manually changed the value of the instruction pointer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$previp</strong></p></td>
<td align="left"><p>The instruction pointer at the time of the previous event. (Breaking into the debugger counts as an event.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$relip</strong></p></td>
<td align="left"><p>An instruction pointer that is related to the current event. When you are branch tracing, this pointer is the pointer to the branch source.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$scopeip</strong></p></td>
<td align="left"><p>The instruction pointer for the current <a href="changing-contexts.md#local-context" data-raw-source="[local context](changing-contexts.md#local-context)">local context</a> (also known as the <em>scope</em>).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exentry</strong></p></td>
<td align="left"><p>The address of the entry point of the first executable of the current process.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$retreg</strong></p></td>
<td align="left"><p>The primary return value register.</p>
<p></p>
<strong>x86-based processors:</strong> The same as <strong>eax</strong>.
<strong>Itanium-based processors:</strong> The same as <strong>ret0</strong>.
<strong>x64-based processors:</strong> The same as <strong>rax</strong>.</td>
</tr>
<tr class="even">
<td align="left"><p><strong>$retreg64</strong></p></td>
<td align="left"><p>The primary return value register, in 64-bit format.</p>
<p><strong>x86 processor:</strong> The same as the <strong>edx:eax</strong> pair.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$csp</strong></p></td>
<td align="left"><p>The current call stack pointer. This pointer is the register that is most representative of call stack depth.</p>
<p></p>
<strong>x86-based processors:</strong> The same as <strong>esp</strong>.
<strong>Itanium-based processors:</strong> The same as <strong>bsp</strong>.
<strong>x64-based processors:</strong> The same as <strong>rsp</strong>.</td>
</tr>
<tr class="even">
<td align="left"><p><strong>$p</strong></p></td>
<td align="left"><p>The value that the last <strong><a href="d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md" data-raw-source="[d* (Display Memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md)">d* (Display Memory)</a></strong> command printed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$proc</strong></p></td>
<td align="left"><p>The address of the current process (that is, the address of the EPROCESS block).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$thread</strong></p></td>
<td align="left"><p>The address of the current thread. In kernel-mode debugging, this address is the address of the ETHREAD block. In user-mode debugging, this address is the address of the thread environment block (TEB).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$peb</strong></p></td>
<td align="left"><p>The address of the process environment block (PEB) of the current process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$teb</strong></p></td>
<td align="left"><p>The address of the thread environment block (TEB) of the current thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$tpid</strong></p></td>
<td align="left"><p>The process ID (PID) for the process that owns the current thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$tid</strong></p></td>
<td align="left"><p>The thread ID for the current thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$dtid</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$dpid</strong></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$dsid</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$bp</strong><em>Number</em></p></td>
<td align="left"><p>The address of the corresponding breakpoint. For example, <strong>$bp3</strong> (or <strong>$bp03</strong>) refers to the breakpoint whose breakpoint ID is 3. <em>Number</em> is always a decimal number. If no breakpoint has an ID of <em>Number</em>, <strong>$bp</strong><em>Number</em> evaluates to zero. For more information about breakpoints, see <a href="using-breakpoints.md" data-raw-source="[Using Breakpoints](using-breakpoints.md)">Using Breakpoints</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$frame</strong></p></td>
<td align="left"><p>The current frame index. This index is the same frame number that the <strong><a href="-frame--set-local-context-.md" data-raw-source="[.frame (Set Local Context)](-frame--set-local-context-.md)">.frame (Set Local Context)</a></strong> command uses.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$dbgtime</strong></p></td>
<td align="left"><p>The current time, according to the computer that the debugger is running on.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$callret</strong></p></td>
<td align="left"><p>The return value of the last function that <strong><a href="-call--call-function-.md" data-raw-source="[.call (Call Function)](-call--call-function-.md)">.call (Call Function)</a></strong> called or that is used in an <strong><a href="-fnret--display-function-return-value-.md" data-raw-source="[.fnret /s](-fnret--display-function-return-value-.md)">.fnret /s</a></strong> command. The data type of <strong>$callret</strong> is the data type of this return value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$extret</strong></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$extin</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$clrex</strong></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$lastclrex</strong></p></td>
<td align="left"><p><strong>Managed debugging only:</strong> The address of the last-encountered common language runtime (CLR) exception object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$ptrsize</strong></p></td>
<td align="left"><p>The size of a pointer. In kernel mode, this size is the pointer size on the target computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pagesize</strong></p></td>
<td align="left"><p>The number of bytes in one page of memory. In kernel mode, this size is the page size on the target computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$pcr</strong></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$pcrb</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$argreg</strong></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_chance</strong></p></td>
<td align="left"><p>The chance of the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_code</strong></p></td>
<td align="left"><p>The exception code for the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_numparams</strong></p></td>
<td align="left"><p>The number of parameters in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param0</strong></p></td>
<td align="left"><p>The value of Parameter 0 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param1</strong></p></td>
<td align="left"><p>The value of Parameter 1 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param2</strong></p></td>
<td align="left"><p>The value of Parameter 2 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param3</strong></p></td>
<td align="left"><p>The value of Parameter 3 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param4</strong></p></td>
<td align="left"><p>The value of Parameter 4 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param5</strong></p></td>
<td align="left"><p>The value of Parameter 5 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param6</strong></p></td>
<td align="left"><p>The value of Parameter 6 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param7</strong></p></td>
<td align="left"><p>The value of Parameter 7 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param8</strong></p></td>
<td align="left"><p>The value of Parameter 8 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param9</strong></p></td>
<td align="left"><p>The value of Parameter 9 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param10</strong></p></td>
<td align="left"><p>The value of Parameter 10 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param11</strong></p></td>
<td align="left"><p>The value of Parameter 11 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param12</strong></p></td>
<td align="left"><p>The value of Parameter 12 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$exr_param13</strong></p></td>
<td align="left"><p>The value of Parameter 13 in the current exception record.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$exr_param14</strong></p></td>
<td align="left"><p>The value of Parameter 14 in the current exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$bug_code</strong></p></td>
<td align="left"><p>If a bug check has occurred, this is the bug code. Applies to live kernel-mode debugging and kernel crash dumps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$bug_param1</strong></p></td>
<td align="left"><p>If a bug check has occurred, this is the value of Parameter 1. Applies to live kernel-mode debugging and kernel crash dumps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$bug_param2</strong></p></td>
<td align="left"><p>If a bug check has occurred, this is the value of Parameter 2. Applies to live kernel-mode debugging and kernel crash dumps.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$bug_param3</strong></p></td>
<td align="left"><p>If a bug check has occurred, this is the value of Parameter 3. Applies to live kernel-mode debugging and kernel crash dumps.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$bug_param4</strong></p></td>
<td align="left"><p>If a bug check has occurred, this is the value of Parameter 4. Applies to live kernel-mode debugging and kernel crash dumps.</p></td>
</tr>
</tbody>
</table>

 

Some of these pseudo-registers might not be available in certain debugging scenarios. For example, you cannot use **$peb**, **$tid**, and **$tpid** when you are debugging a user-mode minidump or certain kernel-mode dump files. There will be situations where you can learn thread information from [**~ (Thread Status)**](---thread-status-.md) but not from **$tid**. You cannot use the **$previp** pseudo-register on the first debugger event. You cannot use the **$relip** pseudo-register unless you are branch tracing. If you use an unavailable pseudo-register, a syntax error occurs.

A pseudo-register that holds the address of a structure -- such as **$thread**, **$proc**, **$teb**, **$peb**, and **$lastclrex** -- will be evaluated according to the proper data type in the C++ expression evaluator, but not in the MASM expression evaluator. For example, the command **? $teb** displays the address of the TEB, while the command **?? @$teb** displays the entire TEB structure. For more information, see [Evaluating Expressions](evaluating-expressions.md).

On an Itanium-based processor, the **iip** register is *bundle-aligned*, which means that it points to slot 0 in the bundle containing the current instruction, even if a different slot is being executed. So **iip** is not the full instruction pointer. The **$ip** pseudo-register is the actual instruction pointer, including the bundle and the slot. The other pseudo-registers that hold address pointers (**$ra**, **$retreg**, **$eventip**, **$previp**, **$relip**, and **$exentry**) have the same structure as **$ip** on all processors.

You can use the **r** command to change the value of **$ip**. This change also automatically changes the corresponding register. When execution resumes, it resumes at the new instruction pointer address. This register is the only automatic pseudo-register that you can change manually.

**Note**   In MASM syntax, you can indicate the **$ip** pseudo-register with a period ( **.** ). You do not add an at sign (@) before this period, and do not use the period as the first parameter of the **r** command. This syntax is not permitted within a C++ expression.

 

Automatic pseudo-registers are similar to [automatic aliases](using-aliases.md). But you can use automatic aliases together with alias-related tokens (such as **${ }**), and you cannot use pseudo-registers with such tokens.

### <span id="user_defined_pseudo_registers"></span><span id="USER_DEFINED_PSEUDO_REGISTERS"></span>User-Defined Pseudo-Registers

There are 20 user-defined pseudo-registers (**$t0**, **$t1**, ..., **$t19**). These pseudo-register are variables that you can read and write through the debugger. You can store any integer value in these pseudo-registers. They can be especially useful as loop variables.

To write to one of these pseudo-registers, use the [**r (Registers)**](r--registers-.md) command, as the following example shows.

```dbgcmd
0:000> r $t0 = 7
0:000> r $t1 = 128*poi(MyVar)
```

Like all pseudo-registers, you can use the user-defined pseudo-register in any expression, as the following example shows.

```dbgcmd
0:000> bp $t3 
0:000> bp @$t4 
0:000> ?? @$t1 + 4*@$t2 
```

A pseudo-register is always typed as an integer, unless you use the **?** switch together with the **r** command. If you use this switch, the pseudo-register acquires the type of whatever is assigned to it. For example, the following command assigns the UNICODE\_STRING\*\* type and the 0x0012FFBC value to **$t15**.

```dbgcmd
0:000> r? $t15 = * (UNICODE_STRING*) 0x12ffbc
```

User-defined pseudo-registers use zero as the default value when the debugger is started.

**Note**  The aliases **$u0**, **$u1**, ..., **$u9** are not pseudo-registers, despite their similar appearance. For more information about these aliases, see [Using Aliases](using-aliases.md).

 

### <span id="example1"></span><span id="EXAMPLE1"></span>Example

The following example sets a breakpoint that is hit every time that the current thread calls **NtOpenFile**. But this breakpoint is not hit when other threads call **NtOpenFile**.

```dbgcmd
kd> bp /t @$thread nt!ntopenfile
```

### <span id="example2"></span><span id="EXAMPLE2"></span>Example

The following example executes a command until the register holds a specified value. First, put the following code for conditional stepping in a script file named "eaxstep".

```dbgcmd
.if (@eax == 1234) { .echo 1234 } .else { t "$<eaxstep" }
```

Next, issue the following command.

```dbgcmd
t "$<eaxstep"
```

The debugger performs a step and then runs your command. In this case, the debugger runs the script, which either displays **1234** or repeats the process.

 

 





