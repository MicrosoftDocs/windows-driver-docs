---
title: Finding the Failed Process
description: Finding the Failed Process
keywords: ["process, finding failed process"]
ms.date: 05/23/2017
---

# Finding the Failed Process


## <span id="ddk_finding_the_failed_process_dbg"></span><span id="DDK_FINDING_THE_FAILED_PROCESS_DBG"></span>


Before finding the failed process, make sure that you are in the context of the accepting processor. To determine the accepting processor, use the [**!pcr**](../debuggercmds/-pcr.md) extension on each processor and looking for the processor for which an exception handler has been loaded. The exception handler of the accepting processor has an address other than 0xFFFFFFFF.

For example, because the address of **NtTib.ExceptionList** on this processor, is 0xFFFFFFFF, this is not the processor with the failed process:

```dbgcmd
0: kd> !pcr 
PCR Processor 0 @ffdff000
 NtTib.ExceptionList: ffffffff
            NtTib.StackBase: 80470650
           NtTib.StackLimit: 8046d860
         NtTib.SubSystemTib: 00000000
              NtTib.Version: 00000000
          NtTib.UserPointer: 00000000
              NtTib.SelfTib: 00000000

                    SelfPcr: ffdff000
                       Prcb: ffdff120
                       Irql: 00000000
                        IRR: 00000000
                        IDR: ffffffff
              InterruptMode: 00000000
                        IDT: 80036400
                        GDT: 80036000
                        TSS: 80257000

              CurrentThread: 8046c610
                 NextThread: 00000000
                 IdleThread: 8046c610

                  DpcQueue: 
```

However, the results for Processor 1 are quite different. In this case, the value of **NtTib.ExceptionList** is **f0823cc0**, not 0xFFFFFFFF, indicating that this is the processor on which the exception occurred.

```dbgcmd
0: kd> ~1 
1: kd> !pcr
PCR Processor 1 @81497000
 NtTib.ExceptionList: f0823cc0
            NtTib.StackBase: f0823df0
           NtTib.StackLimit: f0821000
         NtTib.SubSystemTib: 00000000
              NtTib.Version: 00000000
          NtTib.UserPointer: 00000000
              NtTib.SelfTib: 00000000

                    SelfPcr: 81497000
                       Prcb: 81497120
                       Irql: 00000000
 IRR: 00000000
                        IDR: ffffffff
              InterruptMode: 00000000
                        IDT: 8149b0e8
 GDT: 8149b908
                        TSS: 81498000

              CurrentThread: 81496d28
                 NextThread: 00000000
                 IdleThread: 81496d28

                  DpcQueue: 
```

When you are in the correct processor context, the [**!process**](../debuggercmds/-process.md) extension displays the currently running process.

The most interesting parts of the process dump are:

-   The times (a high value indicates that process might be the culprit).

-   The handle count (this is the number in parentheses after **ObjectTable** in the first entry).

-   The thread status (many processes have multiple threads). If the current process is *Idle*, it is likely that either the machine is truly idle or it hung due to some unusual problem.

Although using the **!process 0 7** extension is the best way to find the problem on a hung system, it is sometimes too much information to filter. Instead, use a **!process 0 0** and then a **!process** on the process handle for CSRSS and any other suspicious processes.

When using a **!process 0 7**, many of the threads might be marked "kernel stack not resident" because those stacks are paged out. If those pages are still in the cache that is in transition, you can get more information by using a **.cache decodeptes** before **!process 0 7**:

```dbgcmd
kd> .cache decodeptes 
kd> !process 0 7 
```

If you can identify the failing process, use **!process** *&lt;process&gt;* **7** to show the kernel stacks for each thread in the process. This output can identify the problem in kernel mode and reveal what the suspect process is calling.

In addition to **!process**, the following extensions can help to determine the cause of an unresponsive computer:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Extension</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><a href="../debuggercmds/-ready.md" data-raw-source="[!ready](../debuggercmds/-ready.md)">!ready</a></strong></p></td>
<td align="left"><p>Identifies the threads that are ready to run, in order of priority.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="../debuggercmds/-locks---kdext--locks-.md" data-raw-source="[!kdext*.locks](../debuggercmds/-locks---kdext--locks-.md)">!kdext*.locks</a></strong></p></td>
<td align="left"><p>Identifies any held resource locks, in case there is a deadlock with retail time outs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="../debuggercmds/-vm.md" data-raw-source="[!vm](../debuggercmds/-vm.md)">!vm</a></strong></p></td>
<td align="left"><p>Checks the virtual memory usage.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="../debuggercmds/-poolused.md" data-raw-source="[!poolused](../debuggercmds/-poolused.md)">!poolused</a></strong></p></td>
<td align="left"><p>Determines whether one type of pool allocation is disproportionately large (pool tagging required).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="../debuggercmds/-memusage.md" data-raw-source="[!memusage](../debuggercmds/-memusage.md)">!memusage</a></strong></p></td>
<td align="left"><p>Checks the physical memory status.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong><a href="../debuggercmds/-heap.md" data-raw-source="[!heap](../debuggercmds/-heap.md)">!heap</a></strong></p></td>
<td align="left"><p>Checks the validity of the heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><a href="../debuggercmds/-irpfind.md" data-raw-source="[!irpfind](../debuggercmds/-irpfind.md)">!irpfind</a></strong></p></td>
<td align="left"><p>Searches nonpaged pool for active IRPs.</p></td>
</tr>
</tbody>
</table>

 

If the information provided does not indicate an unusual condition, try setting a breakpoint at **ntoskrnl!KiSwapThread** to determine whether the processor is stuck in one process or if it is still scheduling other processes. If it is not stuck, set breakpoints in common functions, such as **NtReadFile**, to determine whether the computer is stuck in a specific code path.

 

 