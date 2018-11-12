---
title: running
description: The running extension displays a list of running threads on all processors of the target computer.
ms.assetid: 08fd9806-36e9-4589-bf92-87dc02efebac
keywords: ["running Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- running
api_type:
- NA
ms.localizationpriority: medium
---

# !running


The **!running** extension displays a list of running threads on all processors of the target computer.

```dbgcmd
!running [-i] [-t]
```

## <span id="ddk__running_dbg"></span><span id="DDK__RUNNING_DBG"></span>Parameters


<span id="_______-i______"></span><span id="_______-I______"></span> **-i**   
Causes the display to include idle processors as well.

<span id="_______-t______"></span><span id="_______-T______"></span> **-t**   
Causes a stack trace to be displayed for each processor.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about debugging multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

Remarks
-------

With no options, **!running** will display the affinity of all active processors and all idle processors. For all active processors, it will also display the current and next thread fields from the process control block (PRCB) and the state of the 16 built-in queued spin locks.

Here is an example from a multiprocessor Itanium system:

```dbgcmd
0: kd> !running
 
System Processors 3 (affinity mask)
 Idle Processors 0
 
     Prcb              Current           Next
  0  e0000000818f8000  e0000000818f9e50  e0000000866f12f0  ................
 1  e000000086f16010  e00000008620ebe0  e000000086eddbc0  .O..............
```

The 16 characters at the end of each line indicate the built-in queued spin locks (the LockQueue entries in the PRCB). A period ( . ) indicates that the lock is not in use, **O** means the lock is owned by this processor, and **W** means the processor is queued for the lock. To see more information about the spin lock queue, use [**!qlocks**](-qlocks.md).

Here is an example that shows active and idle processors, along with their stack traces:

```dbgcmd
0: kd> !running -it
 
System Processors f (affinity mask)
  Idle Processors f
All processors idle.
 
     Prcb      Current   Next
  0  ffdff120  805495a0            ................
 
ChildEBP RetAddr
8053e3f0 805329c2 nt!RtlpBreakWithStatusInstruction
8053e3f0 80533464 nt!_KeUpdateSystemTime+0x126
ffdff980 ffdff980 nt!KiIdleLoop+0x14
 
 1  f87e0120  f87e2e60            ................
 
ChildEBP RetAddr
f87e0980 f87e0980 nt!KiIdleLoop+0x14
 
 2  f87f0120  f87f2e60            ................
 
ChildEBP RetAddr
f87f0980 f87f0980 nt!KiIdleLoop+0x14
 
  3  f8800120  f8802e60            ................
 
ChildEBP RetAddr
f8800980 f8800980 nt!KiIdleLoop+0x14
```

 

 





