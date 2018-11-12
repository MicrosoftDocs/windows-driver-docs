---
title: deadlock
description: The deadlock extension displays information about deadlocks collected by the Deadlock Detection option of Driver Verifier.
ms.assetid: c0e6074f-8afe-4526-a30f-427aac67ab99
keywords: ["Deadlock Detection (Driver Verifier)", "deadlock Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- deadlock
api_type:
- NA
ms.localizationpriority: medium
---

# !deadlock


The **!deadlock** extension displays information about deadlocks collected by the **Deadlock Detection** option of Driver Verifier.

```dbgcmd
!deadlock 
!deadlock 1
```

## <span id="ddk__deadlock_dbg"></span><span id="DDK__DEADLOCK_DBG"></span>


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

For information about Driver Verifier, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

This extension will only provide useful information if Driver Verifier's **Deadlock Detection** option has detected a lock hierarchy violation and issued [**bug check 0xC4**](bug-check-0xc4--driver-verifier-detected-violation.md) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION).

Without any arguments, the **!deadlock** extension causes the basic lock hierarchy topology to be displayed. If the problem is not a simple cyclical deadlock, this command will describe the situation that has occurred.

The **!deadlock 1** extension causes stack traces to be displayed. The stacks displayed will be the ones active at the time the locks were acquired.

Here is an example:

```dbgcmd
0:kd> !deadlock

Deadlock detected (2 resources in 2 threads):

Thread 0: A B
Thread 1: B A

Where:
Thread 0 = 8d3ba030
Thread 1 = 8d15c030
Lock A =   bba2af30 Type 'Spinlock'
Lock B =   dummy!GlobalLock Type 'Spinlock'
```

This tells you which threads and which locks are involved. However, it is intended to be a summary and may not be enough information to adequately debug the situation.

Use **!deadlock 1** to print out the contents of the call stacks at the time that each lock participating in the deadlock was acquired. Because these are run-time stack traces, they will be more complete if a checked build is being used. On a free build, they may be truncated after as little as one line.

```dbgcmd
0:kd> !deadlock 1

Deadlock detected (2 resources in 2 threads):

Thread 0 (8D14F750) took locks in the following order:

    Lock A -- b7906f30 (Spinlock)
    Stack:   dummy!DummyActivateVcComplete+0x63
             dummy!dummyOpenVcChannels+0x2E1
             dummy!DummyAllocateRecvBufferComplete+0x436
             dummy!DummyAllocateComplete+0x55
             NDIS!ndisMQueuedAllocateSharedHandler+0xC9
             NDIS!ndisWorkerThread+0xEE

    Lock B -- dummy!GlobalLock (Spinlock)
    Stack:   dummy!dummyQueueRecvBuffers+0x2D
             dummy!DummyActivateVcComplete+0x90
             dummy!dummyOpenVcChannels+0x2E1
             dummy!DummyAllocateRecvBufferComplete+0x436
             dummy!DummyAllocateComplete+0x55

Thread 1 (8D903030) took locks in the following order:

    Lock B -- dummy!GlobalLock (Spinlock)
    Stack:   dummy!dummyRxInterruptOnCompletion+0x25D
             dummy!DummyHandleInterrupt+0x32F
             NDIS!ndisMDpcX+0x3C
             ntkrnlpa!KiRetireDpcList+0x5D

    Lock A -- b7906f30 (Spinlock)
    Stack:   << Current stack >>
```

With this information, you have almost everything you need, except the current stack:

```dbgcmd
0: kd> k
ChildEBP RetAddr
f78aae6c 80664c58 ntkrnlpa!DbgBreakPoint
f78aae74 8066523f ntkrnlpa!ViDeadlockReportIssue+0x2f
f78aae9c 806665df ntkrnlpa!ViDeadlockAnalyze+0x253
f78aaee8 8065d944 ntkrnlpa!VfDeadlockAcquireResource+0x20b
f78aaf08 bfd6df46 ntkrnlpa!VerifierKeAcquireSpinLockAtDpcLevel+0x44
f78aafa4 b1bf2d2d dummy!dummyRxInterruptOnCompletion+0x2b5
f78aafc4 bfde9d8c dummy!DummyHandleInterrupt+0x32f
f78aafd8 804b393b NDIS!ndisMDpcX+0x3c
f78aaff4 804b922b ntkrnlpa!KiRetireDpcList+0x5d
```

From this you can see which locks were involved and where they were acquired. This should be enough information for you to debug the deadlock. If the source code is available, you can use the debugger to see exactly where the problem occurred:

```dbgcmd
0: kd> .lines
Line number information will be loaded

0: kd> u dummy!DummyActivateVcComplete+0x63 l1
dummy!DummyActivateVcComplete+63 [d:\nt\drivers\dummy\vc.c @ 2711]:
b1bfe6c9 837d0c00         cmp     dword ptr [ebp+0xc],0x0

0: kd> u dummy!dummyQueueRecvBuffers+0x2D l1
dummy!dummyQueueRecvBuffers+2d [d:\nt\drivers\dummy\receive.c @ 2894]:
b1bf4e39 807d0c01         cmp     byte ptr [ebp+0xc],0x1

0: kd> u dummy!dummyRxInterruptOnCompletion+0x25D l1
dummy!dummyRxInterruptOnCompletion+25d [d:\nt\drivers\dummy\receive.c @ 1424]:
b1bf5d05 85f6             test    esi,esi

0: kd> u dummy!dummyRxInterruptOnCompletion+0x2b5 l1
dummy!dummyRxInterruptOnCompletion+2b5 [d:\nt\drivers\dummy\receive.c @ 1441]:
b1bf5d5d 8b4648           mov     eax,[esi+0x48]
```

Now you know the name of the source file and the line number where the acquisition took place. In this case, the source files will show that the threads behaved as follows:

-   Thread 1: **DummyActivateVcComplete** took the **dummy** miniport lock. It then called **dummyQueueRecvBuffers**, which took the **dummy** global lock.

-   Thread 2: **dummyRxInterruptOnCompletion** took the global lock. Then, a few lines later, it took the miniport lock.

At this point, the deadlock becomes entirely clear.

 

 





