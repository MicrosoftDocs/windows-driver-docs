---
title: Debugging a Deadlock
description: Debugging a Deadlock
ms.assetid: ee7990d9-2d4e-4e48-9214-539eebd1d8db
keywords: ["deadlocks", "thread, no ready threads"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Deadlock


## <span id="ddk_debugging_deadlocks_no_ready_threads__dbg"></span><span id="DDK_DEBUGGING_DEADLOCKS_NO_READY_THREADS__DBG"></span>


When a thread needs exclusive access to code or some other resource, it requests a *lock*. If it can, Windows responds by giving this lock to the thread. At this point, nothing else in the system can access the locked code. This happens all the time and is a normal part of any well-written multithreaded application. Although a particular code segment can only have one lock on it at a time, multiple code segments can each have their own lock.

A *deadlock* arises when two or more threads have requested locks on two or more resources, in an incompatible sequence. For instance, suppose that Thread One has acquired a lock on Resource A and then requests access to Resource B. Meanwhile, Thread Two has acquired a lock on Resource B and then requests access to Resource A. Neither thread can proceed until the other thread's lock is relinquished, and, therefore, neither thread can proceed.

User-mode deadlocks arise when multiple threads of one application have blocked each others' access to the same resources. Kernel-mode deadlocks arise when multiple threads (from the same process or from distinct processes) have blocked each others' access to the same kernel resource. The procedure used to debug a deadlock depends on whether the deadlock occurs in user mode or in kernel mode.

### <span id="debugging_a_user_mode_deadlock"></span><span id="DEBUGGING_A_USER_MODE_DEADLOCK"></span>Debugging a User-Mode Deadlock

When a deadlock occurs in user mode, use the following procedure to debug it:

1.  Issue the [**!ntsdexts.locks**](-locks---ntsdexts-locks-.md) extension. In user mode, you can just type **!locks** at the debugger prompt; the **ntsdexts** prefix is assumed.

2.  This extension displays all the critical sections associated with the current process, along with the ID for the owning thread and the lock count for each critical section. If a critical section has a lock count of zero, it is not locked. Use the [**~ (Thread Status)**](---thread-status-.md) command to see information about the threads that own the other critical sections.

3.  Use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command for each of these threads to determine whether they are waiting on other critical sections.

4.  Using the output of these **kb** commands, you can find the deadlock: two threads that are each waiting on a lock held by the other thread. In rare cases, a deadlock could be caused by more than two threads holding locks in a circular pattern, but most deadlocks involve only two threads.

Here is an illustration of this procedure. You begin with the **!ntdexts.locks** extension:

```dbgcmd
0:006>  !locks 
CritSec ftpsvc2!g_csServiceEntryLock+0 at 6833dd68
LockCount          0
RecursionCount     1
OwningThread       a7
EntryCount         0
ContentionCount    0
*** Locked
 
CritSec isatq!AtqActiveContextList+a8 at 68629100
LockCount          2
RecursionCount     1
OwningThread       a3
EntryCount         2
ContentionCount    2
*** Locked
 
CritSec +24e750 at 24e750
LockCount          6
RecursionCount     1
OwningThread       a9
EntryCount         6
ContentionCount    6
*** Locked 
```

The first critical section displayed has no locks and, therefore, can be ignored.

The second critical section displayed has a lock count of 2 and is, therefore, a possible cause of a deadlock. The owning thread has a thread ID of 0xA3.

You can find this thread by listing all threads with the [**~ (Thread Status)**](---thread-status-.md) command, and looking for the thread with this ID:

```dbgcmd
0:006>  ~ 
   0  Id: 1364.1330 Suspend: 1 Teb: 7ffdf000 Unfrozen
   1  Id: 1364.17e0 Suspend: 1 Teb: 7ffde000 Unfrozen
   2  Id: 1364.135c Suspend: 1 Teb: 7ffdd000 Unfrozen
   3  Id: 1364.1790 Suspend: 1 Teb: 7ffdc000 Unfrozen
   4  Id: 1364.a3 Suspend: 1 Teb: 7ffdb000 Unfrozen
   5  Id: 1364.1278 Suspend: 1 Teb: 7ffda000 Unfrozen
.  6  Id: 1364.a9 Suspend: 1 Teb: 7ffd9000 Unfrozen
   7  Id: 1364.111c Suspend: 1 Teb: 7ffd8000 Unfrozen
   8  Id: 1364.1588 Suspend: 1 Teb: 7ffd7000 Unfrozen 
```

In this display, the first item is the debugger's internal thread number. The second item (the `Id` field) contains two hexadecimal numbers separated by a decimal point. The number before the decimal point is the process ID; the number after the decimal point is the thread ID. In this example, you see that thread ID 0xA3 corresponds to thread number 4.

You then use the [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command to display the stack that corresponds to thread number 4:

```dbgcmd
0:006>  ~4 kb 
  4  id: 97.a3   Suspend: 0 Teb 7ffd9000 Unfrozen
ChildEBP RetAddr  Args to Child
014cfe64 77f6cc7b 00000460 00000000 00000000 ntdll!NtWaitForSingleObject+0xb
014cfed8 77f67456 0024e750 6833adb8 0024e750 ntdll!RtlpWaitForCriticalSection+0xaa 
014cfee0 6833adb8 0024e750 80000000 01f21cb8 ntdll!RtlEnterCriticalSection+0x46
014cfef4 6833ad8f 01f21cb8 000a41f0 014cff20 ftpsvc2!DereferenceUserDataAndKill+0x24
014cff04 6833324a 01f21cb8 00000000 00000079 ftpsvc2!ProcessUserAsyncIoCompletion+0x2a
014cff20 68627260 01f21e0c 00000000 00000079 ftpsvc2!ProcessAtqCompletion+0x32
014cff40 686249a5 000a41f0 00000001 686290e8 isatq!I_TimeOutContext+0x87
014cff5c 68621ea7 00000000 00000001 0000001e isatq!AtqProcessTimeoutOfRequests_33+0x4f
014cff70 68621e66 68629148 000ad1b8 686230c0 isatq!I_AtqTimeOutWorker+0x30
014cff7c 686230c0 00000000 00000001 000c000a isatq!I_AtqTimeoutCompletion+0x38
014cffb8 77f04f2c 00000000 00000001 000c000a isatq!SchedulerThread_297+0x2f
00000001 000003e6 00000000 00000001 000c000a kernel32!BaseThreadStart+0x51
```

Notice that this thread has a call to the **WaitForCriticalSection** function, which means that not only does it have a lock, it is waiting for code that is locked by something else. We can find out which critical section we are waiting on by looking at the first parameter of the call to **WaitForCriticalSection**. This is the first address under **Args to Child**: "24e750". So this thread is waiting on the critical section at address 0x24E750. This was the third critical section listed by the **!locks** extension that you used earlier.

In other words, thread 4, which owns the second critical section, is waiting on the third critical section. Now turn your attention to the third critical section, which is also locked. The owning thread has thread ID 0xA9. Returning to the output of the **~** command that you saw previously, note that the thread with this ID is thread number 6. Display the stack backtrace for this thread:

```dbgcmd
0:006>  ~6 kb 
ChildEBP RetAddr  Args to Child
0155fe38 77f6cc7b 00000414 00000000 00000000 ntdll!NtWaitForSingleObject+0xb
0155feac 77f67456 68629100 6862142e 68629100 ntdll!RtlpWaitForCriticalSection+0xaa 
0155feb4 6862142e 68629100 0009f238 686222e1 ntdll!RtlEnterCriticalSection+0x46
0155fec0 686222e1 0009f25c 00000001 0009f238 isatq!ATQ_CONTEXT_LISTHEAD__RemoveFromList
0155fed0 68621412 0009f238 686213d1 0009f238 isatq!ATQ_CONTEXT__CleanupAndRelease+0x30
0155fed8 686213d1 0009f238 00000001 01f26bcc isatq!AtqpReuseOrFreeContext+0x3f
0155fee8 683331f7 0009f238 00000001 01f26bf0 isatq!AtqFreeContext+0x36
0155fefc 6833984b ffffffff 00000000 00000000 ftpsvc2!ASYNC_IO_CONNECTION__SetNewSocket
0155ff18 6833adcd 77f05154 01f26a58 00000000 ftpsvc2!USER_DATA__Cleanup+0x47
0155ff28 6833ad8f 01f26a58 000a3410 0155ff54 ftpsvc2!DereferenceUserDataAndKill+0x39
0155ff38 6833324a 01f26a58 00000000 00000040 ftpsvc2!ProcessUserAsyncIoCompletion+0x2a
0155ff54 686211eb 01f26bac 00000000 00000040 ftpsvc2!ProcessAtqCompletion+0x32
0155ff88 68622676 000a3464 00000000 000a3414 isatq!AtqpProcessContext+0xa7
0155ffb8 77f04f2c abcdef01 ffffffff 000ad1b0 isatq!AtqPoolThread+0x32
0155ffec 00000000 68622644 abcdef01 00000000 kernel32!BaseThreadStart+0x51
```

This thread, too, is waiting for a critical section to be freed. In this case, it is waiting on the critical section at 0x68629100. This was the second critical section in the list generated earlier by the **!locks** extension.

This is the deadlock. Thread 4, which owns the second critical section, is waiting on the third critical section. Thread 6, which owns the third critical section, is waiting on the second critical section.

Having confirmed the nature of this deadlock, you can use the usual debugging techniques to analyze threads 4 and 6.

### <span id="debugging_a_kernel_mode_deadlock"></span><span id="DEBUGGING_A_KERNEL_MODE_DEADLOCK"></span>Debugging a Kernel-Mode Deadlock

There are several debugger extensions that are useful for debugging deadocks in kernel mode:

-   The [**!kdexts.locks**](-locks---kdext--locks-.md) extension displays information about all locks held on kernel resources and the threads holding these locks. (In kernel mode, you can just type **!locks** at the debugger prompt; the **kdexts** prefix is assumed.)

-   The [**!qlocks**](-qlocks.md) extension displays the state of all queued spin locks.

-   The [**!wdfkd.wdfspinlock**](-deadlock.md) extension displays information about a Kernel-Mode Driver Framework (KMDF) spin-lock object.

-   The [**!deadlock**](-deadlock.md) extension is used in conjunction with Driver Verifier to detect inconsistent use of locks in your code that have the potential to cause deadlocks.

When a deadlock occurs in kernel mode, use the **!kdexts.locks** extension to list all the locks currently acquired by threads.

You can usually pinpoint the deadlock by finding one non-executing thread that holds an exclusive lock on a resource that is required by an executing thread. Most of the locks are shared.

 

 





