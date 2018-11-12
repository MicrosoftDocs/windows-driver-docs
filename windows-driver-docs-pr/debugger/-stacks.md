---
title: stacks
description: The stacks extension displays information about the kernel stacks.
ms.assetid: f0777609-4785-4a6b-a6f5-9efaeb608df7
keywords: ["stacks Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- stacks
api_type:
- NA
ms.localizationpriority: medium
---

# !stacks


The **!stacks** extension displays information about the kernel stacks.

Syntax

```dbgcmd
!stacks [Detail [FilterString]] 
```

## <span id="ddk__stacks_dbg"></span><span id="DDK__STACKS_DBG"></span>Parameters


<span id="_______Detail______"></span><span id="_______detail______"></span><span id="_______DETAIL______"></span> *Detail*   
Specifies the level of detail to use in the display. The following table lists the valid values for *Detail*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>Displays a summary of the current kernel stacks. This is the default value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>Displays stacks that are currently paged out, as well as the current kernel stacks.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>Displays the full parameters for all stacks, as well as stacks that are currently paged out and the current kernel stacks.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______FilterString______"></span><span id="_______filterstring______"></span><span id="_______FILTERSTRING______"></span> *FilterString*   
Displays only threads that contain the specified substring in a symbol.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about kernel stacks, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

The **!stacks** extension gives a brief summary of the state of every thread. You can use this extension instead of the [**!process**](-process.md) extension to get a quick overview of the system, especially when debugging multithread issues such as resource conflicts or deadlocks.

The [**!findstack**](-findstack.md) user-mode extension also displays information about particular stacks.

Here is an example of the simplest **!stacks** display:

```dbgcmd
kd> !stacks 0
Proc.Thread  .Thread  ThreadState  Blocker
                                     [System]
   4.000050  827eea10  Blocked    +0xfe0343a5

                                     [smss.exe]

                                     [csrss.exe]
  b0.0000a8  82723b70  Blocked    ntoskrnl!_KiSystemService+0xc4
  b0.0000c8  82719620  Blocked    ntoskrnl!_KiSystemService+0xc4
  b0.0000d0  827d5d50  Blocked    ntoskrnl!_KiSystemService+0xc4
.....
```

The first column shows the process ID and the thread ID (separated by a period).

The second column is the current address of the thread's ETHREAD block.

The third column shows the state of the thread (initialized, ready, running, standby, terminated, transition, or blocked).

The fourth column shows the top address on the thread's stack.

Here are examples of more detailed **!stacks** output:

```dbgcmd
kd> !stacks 1
Proc.Thread  .Thread  ThreadState  Blocker
                                     [System]
   4.000008  827d0030  Blocked    ntoskrnl!MmZeroPageThread+0x66
   4.000010  827d0430  Blocked    ntoskrnl!ExpWorkerThread+0x189
   4.000014  827cf030  Blocked    Stack paged out
   4.000018  827cfda0  Blocked    Stack paged out
   4.00001c  827cfb10  Blocked    ntoskrnl!ExpWorkerThread+0x189
.....
                                     [smss.exe]
  9c.000098  82738310  Blocked    Stack paged out
  9c.0000a0  826a5190  Blocked    Stack paged out
  9c.0000a4  82739d30  Blocked    Stack paged out

                                     [csrss.exe]
  b0.0000bc  826d0030  Blocked    Stack paged out
  b0.0000b4  826c9030  Blocked    Stack paged out
  b0.0000a8  82723b70  Blocked    ntoskrnl!_KiSystemService+0xc4
.....

kd> !stacks 2
Proc.Thread  .Thread  ThreadState  Blocker
                                     [System]
   4.000008  827d0030  Blocked    ntoskrnl!KiSwapThread+0xc5
                                  ntoskrnl!KeWaitForMultipleObjects+0x2b4
                                  ntoskrnl!MmZeroPageThread+0x66
                                  ntoskrnl!Phase1Initialization+0xd82
                                  ntoskrnl!PspSystemThreadStartup+0x4d
                                  ntoskrnl!CreateSystemRootLink+0x3d8
                                  +0x3f3f3f3f
   4.000010  827d0430  Blocked    ntoskrnl!KiSwapThread+0xc5
                                  ntoskrnl!KeRemoveQueue+0x191
.....
```

 

 





