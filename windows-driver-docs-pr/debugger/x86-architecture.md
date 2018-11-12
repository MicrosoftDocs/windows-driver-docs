---
title: x86 Architecture
description: x86 Architecture
ms.assetid: 42c62647-7c9a-496e-839f-91283db73a29
keywords: ["x86 processor, architecture", "registers, on an x86 processor", "x86 processor, registers", "x86 processor, calling conventions", "x86 processor, data types"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# x86 Architecture


## <span id="ddk_x86_architecture_dbg"></span><span id="DDK_X86_ARCHITECTURE_DBG"></span>


The Intel x86 processor uses complex instruction set computer (CISC) architecture, which means there is a modest number of special-purpose registers instead of large quantities of general-purpose registers. It also means that complex special-purpose instructions will predominate.

The x86 processor traces its heritage at least as far back as the 8-bit Intel 8080 processor. Many peculiarities in the x86 instruction set are due to the backward compatibility with that processor (and with its Zilog Z-80 variant).

Microsoft Win32 uses the x86 processor in *32-bit flat mode*. This documentation will focus only on the flat mode.

### <span id="Registers"></span><span id="registers"></span><span id="REGISTERS"></span>Registers

The x86 architecture consists of the following unprivileged integer registers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>eax</strong></p></td>
<td align="left"><p>Accumulator</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ebx</strong></p></td>
<td align="left"><p>Base register</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ecx</strong></p></td>
<td align="left"><p>Counter register</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>edx</strong></p></td>
<td align="left"><p>Data register - can be used for I/O port access and arithmetic functions</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>esi</strong></p></td>
<td align="left"><p>Source index register</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>edi</strong></p></td>
<td align="left"><p>Destination index register</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ebp</strong></p></td>
<td align="left"><p>Base pointer register</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>esp</strong></p></td>
<td align="left"><p>Stack pointer</p></td>
</tr>
</tbody>
</table>

 

All integer registers are 32 bit. However, many of them have 16-bit or 8-bit subregisters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ax</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>eax</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bx</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>ebx</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>cx</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>ecx</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dx</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>edx</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>si</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>esi</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>di</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>edi</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bp</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>ebp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sp</strong></p></td>
<td align="left"><p>Low 16 bits of <strong>esp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>al</strong></p></td>
<td align="left"><p>Low 8 bits of <strong>eax</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ah</strong></p></td>
<td align="left"><p>High 8 bits of <strong>ax</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bl</strong></p></td>
<td align="left"><p>Low 8 bits of <strong>ebx</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bh</strong></p></td>
<td align="left"><p>High 8 bits of <strong>bx</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>cl</strong></p></td>
<td align="left"><p>Low 8 bits of <strong>ecx</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ch</strong></p></td>
<td align="left"><p>High 8 bits of <strong>cx</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dl</strong></p></td>
<td align="left"><p>Low 8 bits of <strong>edx</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dh</strong></p></td>
<td align="left"><p>High 8 bits of <strong>dx</strong></p></td>
</tr>
</tbody>
</table>

 

Operating on a subregister affects only the subregister and none of the parts outside the subregister. For example, storing to the **ax** register leaves the high 16 bits of the **eax** register unchanged.

When using the [**? (Evaluate Expression)**](---evaluate-expression-.md) command, registers should be prefixed with an "at" sign ( **@** ). For example, you should use <strong>? @ax</strong> rather than **? ax**. This ensures that the debugger recognizes **ax** as a register rather than a symbol.

However, the (@) is not required in the [**r (Registers)**](r--registers-.md) command. For instance, **r ax=5** will always be interpreted correctly.

Two other registers are important for the processor's current state.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>eip</strong></p></td>
<td align="left"><p>instruction pointer</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>flags</strong></p></td>
<td align="left"><p>flags</p></td>
</tr>
</tbody>
</table>

 

The instruction pointer is the address of the instruction being executed.

The flags register is a collection of single-bit flags. Many instructions alter the flags to describe the result of the instruction. These flags can then be tested by conditional jump instructions. See [x86 Flags](#x86-flags) for details.

### <span id="Calling_Conventions"></span><span id="calling_conventions"></span><span id="CALLING_CONVENTIONS"></span>Calling Conventions

The x86 architecture has several different calling conventions. Fortunately, they all follow the same register preservation and function return rules:

-   Functions must preserve all registers, except for **eax**, **ecx**, and **edx**, which can be changed across a function call, and **esp**, which must be updated according to the calling convention.

-   The **eax** register receives function return values if the result is 32 bits or smaller. If the result is 64 bits, then the result is stored in the **edx:eax** pair.

The following is a list of calling conventions used on the x86 architecture:

-   Win32 (**\_\_stdcall**)

    Function parameters are passed on the stack, pushed right to left, and the callee cleans the stack.

-   Native C++ method call (also known as thiscall)

    Function parameters are passed on the stack, pushed right to left, the "this" pointer is passed in the **ecx** register, and the callee cleans the stack.

-   COM (**\_\_stdcall** for C++ method calls)

    Function parameters are passed on the stack, pushed right to left, then the "this" pointer is pushed on the stack, and then the function is called. The callee cleans the stack.

-   **\_\_fastcall**

    The first two DWORD-or-smaller arguments are passed in the **ecx** and **edx** registers. The remaining parameters are passed on the stack, pushed right to left. The callee cleans the stack.

-   **\_\_cdecl**

    Function parameters are passed on the stack, pushed right to left, and the caller cleans the stack. The **\_\_cdecl** calling convention is used for all functions with variable-length parameters.

### <span id="Debugger_Display_of_Registers_and_Flags"></span><span id="debugger_display_of_registers_and_flags"></span><span id="DEBUGGER_DISPLAY_OF_REGISTERS_AND_FLAGS"></span>Debugger Display of Registers and Flags

Here is a sample debugger register display:

```dbgcmd
eax=00000000 ebx=008b6f00 ecx=01010101 edx=ffffffff esi=00000000 edi=00465000
eip=77f9d022 esp=05cffc48 ebp=05cffc54 iopl=0         nv up ei ng nz na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=0038  gs=0000             efl=00000286
```

In user-mode debugging, you can ignore the **iopl** and the entire last line of the debugger display.

### <span id="x86-flags"></span><span id="X86_FLAGS"></span>x86 Flags

In the preceding example, the two-letter codes at the end of the second line are *flags*. These are single-bit registers and have a variety of uses.

The following table lists the x86 flags:

Flag Code
Flag Name
Value
Flag Status
Status Description
**of**

Overflow Flag

0
1
**nvov**

No overflow
Overflow
**df**

Direction Flag

0
1
**updn**

Direction up
Direction down
**if**

Interrupt Flag

0
1
**diei**

Interrupts disabled
Interrupts enabled
**sf**

Sign Flag

0
1
**plng**

Positive (or zero)
Negative
**zf**

Zero Flag

0
1
**nzzr**

Nonzero
Zero
**af**

Auxiliary Carry Flag

0
1
**naac**

No auxiliary carry
Auxiliary carry
**pf**

Parity Flag

0
1
**pepo**

Parity even
Parity odd
**cf**

Carry Flag

0
1
**nccy**

No carry
Carry
**tf**

Trap Flag

If **tf** equals 1, the processor will raise a STATUS\_SINGLE\_STEP exception after the execution of one instruction. This flag is used by a debugger to implement single-step tracing. It should not be used by other applications.

**iopl**

I/O Privilege Level

This is a two-bit integer, with values between zero and 3. It is used by the operating system to control access to hardware. It should not be used by applications.

 

When registers are displayed as a result of some command in the Debugger Command window, it is the *flag status* that is displayed. However, if you want to change a flag using the [**r (Registers)**](r--registers-.md) command, you should refer to it by the *flag code*.

In the Registers window of WinDbg, the flag code is used to view or alter flags. The flag status is not supported.

Here is an example. In the preceding register display, the flag status **ng** appears. This means that the sign flag is currently set to 1. To change this, use the following command:

```dbgcmd
r sf=0
```

This sets the sign flag to zero. If you do another register display, the **ng** status code will not appear. Instead, the **pl** status code will be displayed.

The Sign Flag, Zero Flag, and Carry Flag are the most commonly-used flags.

### <span id="Conditions"></span><span id="conditions"></span><span id="CONDITIONS"></span>Conditions

A *condition* describes the state of one or more flags. All conditional operations on the x86 are expressed in terms of conditions.

The assembler uses a one or two letter abbreviation to represent a condition. A condition can be represented by multiple abbreviations. For example, AE ("above or equal") is the same condition as NB ("not below"). The following table lists some common conditions and their meaning.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Condition Name</th>
<th align="left">Flags</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Z</p></td>
<td align="left"><p>ZF=1</p></td>
<td align="left"><p>Result of last operation was zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NZ</p></td>
<td align="left"><p>ZF=0</p></td>
<td align="left"><p>Result of last operation was not zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>C</p></td>
<td align="left"><p>CF=1</p></td>
<td align="left"><p>Last operation required a carry or borrow. (For unsigned integers, this indicates overflow.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>NC</p></td>
<td align="left"><p>CF=0</p></td>
<td align="left"><p>Last operation did not require a carry or borrow. (For unsigned integers, this indicates overflow.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>S</p></td>
<td align="left"><p>SF=1</p></td>
<td align="left"><p>Result of last operation has its high bit set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NS</p></td>
<td align="left"><p>SF=0</p></td>
<td align="left"><p>Result of last operation has its high bit clear.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>O</p></td>
<td align="left"><p>OF=1</p></td>
<td align="left"><p>When treated as a signed integer operation, the last operation caused an overflow or underflow.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NO</p></td>
<td align="left"><p>OF=0</p></td>
<td align="left"><p>When treated as signed integer operation, the last operation did not cause an overflow or underflow.</p></td>
</tr>
</tbody>
</table>

 

Conditions can also be used to compare two values. The **cmp** instruction compares its two operands, and then sets flags as if subtracted one operand from the other. The following conditions can be used to check the result of **cmp** *value1*, *value2*.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Condition Name</th>
<th align="left">Flags</th>
<th align="left">Meaning after a CMP operation.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>E</p></td>
<td align="left"><p>ZF=1</p></td>
<td align="left"><p><em>value1</em> == <em>value2</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NE</p></td>
<td align="left"><p>ZF=0</p></td>
<td align="left"><p><em>value1</em> != <em>value2</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
GE
NL</td>
<td align="left"><p>SF=OF</p></td>
<td align="left"><p></p>
<em>value1</em> &gt;= <em>value2</em>.
Values are treated as signed integers.</td>
</tr>
<tr class="even">
<td align="left"><p></p>
LE
NG</td>
<td align="left"><p>ZF=1 or SF!=OF</p></td>
<td align="left"><p><em>value1</em> &lt;= <em>value2</em>. Values are treated as signed integers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
G
NLE</td>
<td align="left"><p>ZF=0 and SF=OF</p></td>
<td align="left"><p><em>value1</em> &gt; <em>value2</em>. Values are treated as signed integers.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
L
NGE</td>
<td align="left"><p>SF!=OF</p></td>
<td align="left"><p><em>value1</em> &lt; <em>value2</em>. Values are treated as signed integers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
AE
NB</td>
<td align="left"><p>CF=0</p></td>
<td align="left"><p><em>value1</em> &gt;= <em>value2</em>. Values are treated as unsigned integers.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
BE
NA</td>
<td align="left"><p>CF=1 or ZF=1</p></td>
<td align="left"><p><em>value1</em> &lt;= <em>value2</em>. Values are treated as unsigned integers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
A
NBE</td>
<td align="left"><p>CF=0 and ZF=0</p></td>
<td align="left"><p><em>value1</em> &gt; <em>value2</em>. Values are treated as unsigned integers.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
B
NAE</td>
<td align="left"><p>CF=1</p></td>
<td align="left"><p><em>value1</em> &lt; <em>value2</em>. Values are treated as unsigned integers.</p></td>
</tr>
</tbody>
</table>

 

Conditions are typically used to act on the result of a **cmp** or **test** instruction. For example,

```asm
cmp eax, 5
jz equal
```

compares the **eax** register against the number 5 by computing the expression (**eax** - 5) and setting flags according to the result. If the result of the subtraction is zero, then the **zr** flag will be set, and the **jz** condition will be true so the jump will be taken.

### <span id="Data_Types"></span><span id="data_types"></span><span id="DATA_TYPES"></span>Data Types

-   byte: 8 bits

-   word: 16 bits

-   dword: 32 bits

-   qword: 64 bits (includes floating-point doubles)

-   tword: 80 bits (includes floating-point extended doubles)

-   oword: 128 bits

### <span id="Notation"></span><span id="notation"></span><span id="NOTATION"></span>Notation

The following table indicates the notation used to describe assembly language instructions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Notation</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>r</strong>, <strong>r1</strong>, <strong>r2</strong>...</p></td>
<td align="left"><p>Registers</p></td>
</tr>
<tr class="even">
<td align="left"><p>m</p></td>
<td align="left"><p>Memory address (see the succeeding Addressing Modes section for more information.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>#n</p></td>
<td align="left"><p>Immediate constant</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r</strong>/m</p></td>
<td align="left"><p>Register or memory</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>r</strong>/#n</p></td>
<td align="left"><p>Register or immediate constant</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>r</strong>/m/#n</p></td>
<td align="left"><p>Register, memory, or immediate constant</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>cc</em></p></td>
<td align="left"><p>A condition code listed in the preceding Conditions section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>T</em></p></td>
<td align="left"><p>&quot;B&quot;, &quot;W&quot;, or &quot;D&quot; (byte, word or dword)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>acc<em>T</em></p></td>
<td align="left"><p>Size <em>T</em> accumulator: <strong>al</strong> if <em>T</em> = &quot;B&quot;, <strong>ax</strong> if <em>T</em> = &quot;W&quot;, or <strong>eax</strong> if <em>T</em> = &quot;D&quot;</p></td>
</tr>
</tbody>
</table>

 

### <span id="Addressing_Modes"></span><span id="addressing_modes"></span><span id="ADDRESSING_MODES"></span>Addressing Modes

There are several different addressing modes, but they all take the form **T ptr \[expr\]**, where **T** is some data type (see the preceding Data Types section) and **expr** is some expression involving constants and registers.

The notation for most modes can be deduced without much difficulty. For example, **BYTE PTR \[esi+edx\*8+3\]** means "take the value of the **esi** register, add to it eight times the value of the **edx** register, add three, then access the byte at the resulting address."

### <span id="Pipelining"></span><span id="pipelining"></span><span id="PIPELINING"></span>Pipelining

The Pentium is dual-issue, which means that it can perform up to two actions in one clock tick. However, the rules on when it is capable of doing two actions at once (known as *pairing*) are very complicated.

Because x86 is a CISC processor, you do not have to worry about jump delay slots.

### <span id="Synchronized_Memory_Access"></span><span id="synchronized_memory_access"></span><span id="SYNCHRONIZED_MEMORY_ACCESS"></span>Synchronized Memory Access

Load, modify, and store instructions can receive a **lock** prefix, which modifies the instruction as follows:

1.  Before issuing the instruction, the CPU will flush all pending memory operations to ensure coherency. All data prefetches are abandoned.

2.  While issuing the instruction, the CPU will have exclusive access to the bus. This ensures the atomicity of the load/modify/store operation.

The **xchg** instruction automatically obeys the previous rules whenever it exchanges a value with memory.

All other instructions default to nonlocking.

### <span id="Jump_Prediction"></span><span id="jump_prediction"></span><span id="JUMP_PREDICTION"></span>Jump Prediction

Unconditional jumps are predicted to be taken.

Conditional jumps are predicted to be taken or not taken, depending on whether they were taken the last time they were executed. The cache for recording jump history is limited in size.

If the CPU does not have a record of whether the conditional jump was taken or not taken the last time it was executed, it predicts backward conditional jumps as taken and forward conditional jumps as not taken.

### <span id="Alignment"></span><span id="alignment"></span><span id="ALIGNMENT"></span>Alignment

The x86 processor will automatically correct unaligned memory access, at a performance penalty. No exception is raised.

A memory access is considered aligned if the address is an integer multiple of the object size. For example, all BYTE accesses are aligned (everything is an integer multiple of 1), WORD accesses to even addresses are aligned, and DWORD addresses must be a multiple of 4 in order to be aligned.

The **lock** prefix should not be used for unaligned memory accesses.

 

 





