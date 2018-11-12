---
title: Resource Time Outs
description: Resource Time Outs
ms.assetid: ea5b61e0-cb51-4da2-9596-ab85f7b01bed
keywords: ["resource time outs"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Resource Time Outs


## <span id="ddk_resource_time_outs_dbg"></span><span id="DDK_RESOURCE_TIME_OUTS_DBG"></span>


During a resource time out, the thread waiting for the resource will break into the kernel debugger with a message similar to the following:

```console
Resource @ 800e99c0
 ActiveCount = 0001  Flags = IsOwnedExclusive sharedWaiter
 NumberOfExclusiveWaiters = 0000
  Thread = 809cd2f0, Count = 01
  Thread = 809ebc50, Count = 01
  Thread = 00000000, Count = 00
  Thread = 00000000, Count = 00
  Thread = 00000000, Count = 00
NT!DbgBreakPoint+0x4:
800cee04: 000000ad callkd 
```

The thread that holds the lock is the first thread listed (or multiple threads if it is a shared lock). To examine that thread, use a **!thread** extension on the thread ID (809cd2f0, in the previous example). This will give a stack for the thread owning the resource. If it is also waiting for a resource to become available, either the **ExpWaitForResourceExclusive** function or the **ExpWaitForResourceShared** function will be on the stack for that thread.

The first parameter to **ExpWaitForResource*Xxx*** is the lock that is being waited on. To find out about that resource, use a **!locks &lt;*resource id*&gt;** extension, which will give you another thread to check.

If you get to a thread that is not waiting for another resource, that thread is probably the source of the problem. For a list of all held locks, use a **!locks** extension with no parameter at the **kd&gt;** prompt.

### <span id="example"></span><span id="EXAMPLE"></span>Example

```console
Resource @ fc664ee0                  // Here's the resource lock address

 ActiveCount = 0001  Flags = IsOwnedExclusive ExclusiveWaiter
 NumberOfExclusiveWaiters = 0001
  Thread = ffaf5410, Count = 01                // Here's the owning thread
  Thread = 00000000, Count = 00
ntoskrnl!_DbgBreakPoint:
80131400 cc               int     3

kd> kb                                        // Start with a stack
ChildEBP RetAddr  Args to Child
fcd44980 801154c0 fc664ee0 ffab45d0 00110001 ntoskrnl!_DbgBreakPoint
fcd4499c 80102521 fc664ee0 ffb08ea8 fcd44a4c ntoskrnl!_ExpWaitForResource+0x114        // Lock being waited on...

fcd449e8 fc6509fa e12597c8 fef27c08 fee4fca8 ntoskrnl!_ExAcquireResourceExclusiveLite+0xa5
00380020 00000000 00000000 00000000 00000000 nwrdr!_CreateScb+0x2ff

kd> !locks fc664ee0                      // !locks resource address gives lock info
Resource @ nwrdr!_NwScavengerSpinLock (0xfc664ee0)    Exclusively owned
    Contention Count = 45
    NumberOfExclusiveWaiters = 1
     Threads: ffaf5410-01                  // Owning thread again
1 total locks, 1 locks currently held

kd> !thread ffaf5410                     // Check the owning thread

THREAD ffaf5410  Cid e7.e8  Teb: 7ffde000 WAIT: (Executive) KernelMode Non-Alertable
    feecf698  SynchronizationEvent
IRP List:
    fef29208: (0006,00b8) Flags: 00000884  Mdl: feed8328
Not impersonating
Owning Process ffaf5690
WaitTime (seconds)      2781250
Context Switch Count    183175
UserTime                  0:00:23.0153
KernelTime                0:01:01.0187
Start Address 0x77f04644
Initial Sp fec6c000 Current Sp fec6b938
Priority 11 BasePriority 7 PriorityDecrement 0 DecrementCount 8

ChildEBP RetAddr  Args to Child
fec6b950 801044fc feecf668 feecf668 00000080 ntoskrnl!KiSwapContext+0x25
fec6b974 fc655976 feecf698 00000000 00000000 ntoskrnl!_KeWaitForSingleObject+0x218
fec6ba5c fc6509fa e1263968 fef29208 feecf668 nwrdr!_ExchangeWithWait+0x38
fec6ba28 fc6533e5 feecf668 e125b3c8 ffafae08 nwrdr!_CreateScb+0x2ff
fec6bac0 fc652f26 feecf668 fec6bae4 fef29208 nwrdr!_CreateRemoteFile+0x2c9
fec6bb6c fc652b14 feecf668 fef29208 fee50b60 nwrdr!_NwCommonCreate+0x3a2

fec6bbac 80107aea fee50b60 fef29208 804052ac nwrdr!_NwFsdCreate+0x56
fec6bbc0 80142792 fef37700 fec6bdbc fee50b28 ntoskrnl!IofCallDriver+0x38
fec6bd10 80145403 fee50b60 00000000 fec6bdbc ntoskrnl!_IopParseDevice+0x6a0
fec6bd7c 80144c0c 00000000 fec6be34 00000040 ntoskrnl!_ObpLookupObjectName+0x479
fec6be5c 80127803 0012dd64 00000000 80127701 ntoskrnl!_ObOpenObjectByName+0xa2
fec6bef4 801385c3 0012dd64 0012dd3c 00000000 ntoskrnl!_NtQueryAttributesFile+0xc1
fec6bef4 77f716ab 0012dd64 0012dd3c 00000000 ntoskrnl!_KiSystemService+0x83

0012dd20 00000000 00000000 00000000 00000000 ntdll!_ZwQueryAttributesFile+0xb 
```

 

 





