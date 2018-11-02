---
title: thread
description: The thread extension displays summary information about a thread on the target system, including the ETHREAD block. This command can be used only during kernel-mode debugging.
ms.assetid: 5d3cf2f7-02bf-4a94-b542-826ad2b66a6f
keywords: ["thread Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- thread
api_type:
- NA
ms.localizationpriority: medium
---

# !thread


The **!thread** extension displays summary information about a thread on the target system, including the ETHREAD block. This command can be used only during kernel-mode debugging.

This extension command is not the same as the [**.thread (Set Register Context)**](-thread--set-register-context-.md) command.

Syntax

```dbgcmd
!thread [-p] [-t] [Address [Flags]]
```

## <span id="ddk__thread_dbg"></span><span id="DDK__THREAD_DBG"></span>Parameters


<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Displays summary information about the process that owns the thread.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
When this option is included, *Address* is the thread ID, not the thread address.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the thread on the target computer. If *Address* is -1 or omitted, it indicates the current thread.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail to display. *Flags* can be any combination of the following bits. If *Flags* is 0, only a minimal amount of information is displayed. The default is 0x6:

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays the thread's wait states.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
If this bit is used without Bit 1 (0x2), it has no effect. If this bit is used with Bit 1, the thread is displayed with a stack trace.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Adds the return address, the stack pointer, and (on Itanium systems) the **bsp** register value to the information displayed for each function and suppresses the display of function arguments.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Sets the process context equal to the process that owns the specified thread for the duration of this command. This results in more accurate display of thread stacks.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about threads in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

Here is an example using Windows 10:

```dbgcmd
0: kd> !thread 0xffffcb088f0a4480            
THREAD ffffcb088f0a4480  Cid 0e34.3814  Teb: 0000001a27ca6000 Win32Thread: 0000000000000000 RUNNING on processor 0
Not impersonating
DeviceMap                 ffffb80842016c20
Owning Process            ffffcb08905397c0       Image:         MsMpEng.exe
Attached Process          N/A            Image:         N/A
Wait Start TickCount      182835891      Ticks: 0
Context Switch Count      5989           IdealProcessor: 3             
UserTime                  00:00:01.046
KernelTime                00:00:00.296
Win32 Start Address 0x00007ffb3b2fd1b0
Stack Init ffff95818476add0 Current ffff958184769d30
Base ffff95818476b000 Limit ffff958184765000 Call 0000000000000000
Priority 8 BasePriority 8 PriorityDecrement 0 IoPriority 2 PagePriority 5
Child-SP          RetAddr           : Args to Child                                                           : Call Site
fffff802`59858c68 fffff801`b56d24aa : ffffcb08`8fd68010 00000000`00000000 fffff802`58259600 00000000`00000008 : nt!DbgBreakPointWithStatus [d:\rs2\minkernel\ntos\rtl\amd64\debugstb.asm @ 130] 
fffff802`59858c70 ffffcb08`8fd68010 : 00000000`00000000 fffff802`58259600 00000000`00000008 ffffcb08`8f0a4400 : 0xfffff801`b56d24aa
fffff802`59858c78 00000000`00000000 : fffff802`58259600 00000000`00000008 ffffcb08`8f0a4400 00000000`00000019 : 0xffffcb08`8fd68010
```

Use commands like [**!process**](-process.md) to locate the address or thread ID of the thread you are interested in.

The useful information in the **!thread** display is explained in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Thread address</strong></p></td>
<td align="left"><p>The hexadecimal number after the word <em>THREAD</em> is the address of the ETHREAD block. In the preceding example, the thread address is 0xffffcb088f0a4480 .</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Thread ID</strong></p></td>
<td align="left"><p>The two hexadecimal numbers after the word <em>Cid</em> are the process ID and the thread ID: <em>process ID.thread ID</em>. In the preceding example, the process ID is 0x0e34, and the thread ID is 0x3814.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Thread Environment Block (TEB)</strong></p></td>
<td align="left"><p>The hexadecimal number after the word <em>Teb</em> is the address of the thread environment block (TEB).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>System Service Dispatch Table</strong></p></td>
<td align="left"><p>The hexadecimal number after the word <em>Win32Thread</em> is the address of the system service dispatch table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Thread State</strong></p></td>
<td align="left"><p>The thread state is displayed at the end of the line that begins with the word <em>RUNNING</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Owning Process</strong></p></td>
<td align="left"><p>The hexadecimal number after the words <em>Owning Process</em> is the address of the EPROCESS for the process that owns this thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Start Address</strong></p></td>
<td align="left"><p>The hexadecimal number after the words <em>Start Address</em> is the thread start address. This might appear in symbolic form.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>User Thread Function</strong></p></td>
<td align="left"><p>The hexadecimal number after the words <em>Win32 Start Address</em> is the address of the user thread function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Priority</strong></p></td>
<td align="left"><p>The priority information for the thread follows the word <em>Priority</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Stack trace</strong></p></td>
<td align="left"><p>A stack trace for the thread appears at the end of this display.</p></td>
</tr>
</tbody>
</table>

 

 

 





