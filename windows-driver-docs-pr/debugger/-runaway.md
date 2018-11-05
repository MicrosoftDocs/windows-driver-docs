---
title: runaway
description: The runaway extension displays information about the time consumed by each thread.
ms.assetid: ea318d5b-60c6-4d1c-80c7-6bc418ad01ab
keywords: ["runaway Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- runaway
api_type:
- NA
ms.localizationpriority: medium
---

# !runaway


The **!runaway** extension displays information about the time consumed by each thread.

```dbgcmd
!runaway [Flags]
```

## <span id="ddk__runaway_dbg"></span><span id="DDK__RUNAWAY_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the kind of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x1.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the debugger to show the amount of user time consumed by each thread.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the debugger to show the amount of kernel time consumed by each thread.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the debugger to show the amount of time that has elapsed since each thread was created.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Uext.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p></p>
Uext.dll
Ntsdexts.dll</td>
</tr>
</tbody>
</table>

 

The **!runaway** extension can only be used during live debugging or when debugging crash dump files created by [**.dump /mt**](-dump--create-dump-file-.md) or **.dump /ma**.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about threads in user mode, see [Controlling Processes and Threads](controlling-processes-and-threads.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

This extension is a quick way to find out which threads are spinning out of control or consuming too much CPU time.

The display identifies each thread by the debugger's internal thread numbering and by the thread ID in hexadecimal. The debugger IDs are also shown.

Here is an example:

```dbgcmd
0:001> !runaway 7

 User Mode Time
 Thread       Time
 0:55c        0:00:00.0093
 1:1a4        0:00:00.0000

 Kernel Mode Time
 Thread       Time
 0:55c        0:00:00.0140
 1:1a4        0:00:00.0000

 Elapsed Time
 Thread       Time
 0:55c        0:00:43.0533
 1:1a4        0:00:25.0876
```

 

 





