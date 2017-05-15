---
title: Finding the Failed Process
description: Finding the Failed Process
ms.assetid: 64d1fa71-940f-4f67-87a6-00d41d6f24e0
keywords: ["process, finding failed process"]
---

# Finding the Failed Process


## <span id="ddk_finding_the_failed_process_dbg"></span><span id="DDK_FINDING_THE_FAILED_PROCESS_DBG"></span>


Before finding the failed process, make sure that you are in the context of the accepting processor. To determine the accepting processor, use the [**!pcr**](-pcr.md) extension on each processor and looking for the processor for which an exception handler has been loaded. The exception handler of the accepting processor has an address other than 0xFFFFFFFF.

For example, because the address of **NtTib.ExceptionList** on this processor, is 0xFFFFFFFF, this is not the processor with the failed process:

``` syntax
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

``` syntax
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

When you are in the correct processor context, the [**!process**](-process.md) extension displays the currently running process.

The most interesting parts of the process dump are:

-   The times (a high value indicates that process might be the culprit).

-   The handle count (this is the number in parentheses after **ObjectTable** in the first entry).

-   The thread status (many processes have multiple threads). If the current process is *Idle*, it is likely that either the machine is truly idle or it hung due to some unusual problem.

Although using the **!process 0 7** extension is the best way to find the problem on a hung system, it is sometimes too much information to filter. Instead, use a **!process 0 0** and then a **!process** on the process handle for CSRSS and any other suspicious processes.

When using a **!process 0 7**, many of the threads might be marked "kernel stack not resident" because those stacks are paged out. If those pages are still in the cache that is in transition, you can get more information by using a **.cache decodeptes** before **!process 0 7**:

``` syntax
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
<td align="left"><p>[<strong>!ready</strong>](-ready.md)</p></td>
<td align="left"><p>Identifies the threads that are ready to run, in order of priority.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!kdext*.locks</strong>](-locks---kdext--locks-.md)</p></td>
<td align="left"><p>Identifies any held resource locks, in case there is a deadlock with retail time outs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!vm</strong>](-vm.md)</p></td>
<td align="left"><p>Checks the virtual memory usage.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!poolused</strong>](-poolused.md)</p></td>
<td align="left"><p>Determines whether one type of pool allocation is disproportionately large (pool tagging required).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!memusage</strong>](-memusage.md)</p></td>
<td align="left"><p>Checks the physical memory status.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>!heap</strong>](-heap.md)</p></td>
<td align="left"><p>Checks the validity of the heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!irpfind</strong>](-irpfind.md)</p></td>
<td align="left"><p>Searches nonpaged pool for active IRPs.</p></td>
</tr>
</tbody>
</table>

 

If the information provided does not indicate an unusual condition, try setting a breakpoint at **ntoskrnl!KiSwapThread** to determine whether the processor is stuck in one process or if it is still scheduling other processes. If it is not stuck, set breakpoints in common functions, such as **NtReadFile**, to determine whether the computer is stuck in a specific code path.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Finding%20the%20Failed%20Process%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




