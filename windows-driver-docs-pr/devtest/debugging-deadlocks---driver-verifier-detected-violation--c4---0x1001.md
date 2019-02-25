---
title: Debugging deadlocks - DRIVER_VERIFIER_DETECTED_VIOLATION (C4) 0x1001
description: When Driver Verifier detects a spin lock hierarchy violation, Driver Verifiergenerates Bug Check 0xC4 DRIVER_VERIFIER_DETECTED_VIOLATION with a parameter 1 value of 0x1001.
ms.assetid: 4C3ED1DB-5EDC-4386-B91C-CF86973EE1F6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="devtest.debugging_deadlocks_-_driver_verifier_detected_violation__c4___0x1001"></span>Debugging deadlocks - DRIVER\_VERIFIER\_DETECTED\_VIOLATION (C4): 0x1001


When [Driver Verifier](driver-verifier.md) detects a spin lock hierarchy violation, Driver Verifiergenerates [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) with a parameter 1 value of 0x1001.

When the Deadlock Detection option is active (Deadlock Detection is part of the Driver Verifier Standard Options), [Driver Verifier](driver-verifier.md) keeps track of each spin lock allocated and the order in which it was acquired and freed. A lock hierarchy violation means that Driver Verifier has detected a situation where, in at least one case, *LockA* is acquired and held before *LockB* is acquired, and in another, *LockB* is acquired and held before *LockA* is required.

**Important**  This bug check occurs whenever [Driver Verifier](driver-verifier.md) detects that the hierarchy violation has occurred, not when an actual deadlock situation is occurring. This violation enforces strongly enforces that any locks that are shared among the various component of a driver should always be acquired and released in an order which makes the deadlocking of two threads impossible.



**New in Windows 8.1** When [Driver Verifier](driver-verifier.md) encounters this violation, if the debugger is attached, the debugger will ask you for input about the error. In Windows 8 and previous versions of Windows, this violation result in an immediate bug check.

```
************ Verifier Detected a Potential Deadlock *************
**
** Type !deadlock in the debugger for more information.
**
*****************************************************************

*** Verifier assertion failed ***
(B)reak, (I)gnore, (W)arn only, (R)emove assert?
```

To debug this violation on a computer running Windows 8.1, choose **B** (Break), and enter the suggested debugger command ([**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326)):

```
kd> !deadlock
issue: 00001001 97dd800c 86858ce0 00000000 

Deadlock detected (2 locks in 2 threads):

Thread 0: A B.
Thread 1: B A.

Where:

Thread 0 = TERMINATED.
Thread 1 = c4ae2040.

Lock A =   97dd800c (MyTestDriver!AlphaLock+0x00000000) - Type 'Spinlock'.
Lock B =   97dd8008 (MyTestDriver!BravoLock+0x00000000) - Type 'Spinlock'.
```

The [**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326) **3** command can also be used to show more information, including the stack at the time of last acquire:

```
kd> !deadlock 3
issue: 00001001 97dd800c 86858ce0 00000000 

Deadlock detected (2 locks in 2 threads):
# 

Thread 0: TERMINATED took locks in the following order:

Lock A =     97dd800c (MyTestDriver!AlphaLock+0x00000000) - Type 'Spinlock'.

    Node:    8685acd8

    Stack:   97dd65b7 MyTestDriver!SystemControlIrpWorker+0x00000027 
             97dd605a MyTestDriver!Dispatch_SystemControl+0x0000001a 
             820c4b4d nt!IovCallDriver+0x000002cc 
             81ca3772 nt!IofCallDriver+0x00000062 
             81eb165e nt!IopSynchronousServiceTail+0x0000016e 
             81eb5518 nt!IopXxxControlFile+0x000003e8 
             81eb4516 nt!NtDeviceIoControlFile+0x0000002a 
             81d27e17 nt!KiSystemServicePostCall+0x00000000 

Lock B =     97dd8008 (MyTestDriver!BravoLock+0x00000000) - Type 'Spinlock'.

    Node:    86833578

    Stack:   97dd65c5 MyTestDriver!SystemControlIrpWorker+0x00000a4a 
             97dd605a MyTestDriver!Dispatch_SystemControl+0x0000001a 
             820c4b4d nt!IovCallDriver+0x000002cc 
             81ca3772 nt!IofCallDriver+0x00000062 
             81eb165e nt!IopSynchronousServiceTail+0x0000016e 
             81eb5518 nt!IopXxxControlFile+0x000003e8 
             81eb4516 nt!NtDeviceIoControlFile+0x0000002a 
             81d27e17 nt!KiSystemServicePostCall+0x00000000
# 

Thread 1: c4ae2040 (ThreadEntry = 86833a08) took locks in the following order:

Lock B =     97dd8008 (MyTestDriver!BravoLock+0x00000000) - Type 'Spinlock'.

    Node:    86858ce0

    Stack:   97dd65ef MyTestDriver!DeviceControlIrpWorker+0x0000005f 
             97dd605a MyTestDriver!Dispatch_DeviceControl+0x0000001a 
             820c4b4d nt!IovCallDriver+0x000002cc 
             81ca3772 nt!IofCallDriver+0x00000062 
             81eb165e nt!IopSynchronousServiceTail+0x0000016e 
             81eb5518 nt!IopXxxControlFile+0x000003e8 
             81eb4516 nt!NtDeviceIoControlFile+0x0000002a 
             81d27e17 nt!KiSystemServicePostCall+0x00000000 

Lock A =     97dd800c (MyTestDriver!AlphaLock+0x00000000) - Type 'Spinlock'.

    Stack:   << Current stack trace - use kb to display it >>
```

The debugger suggests using the [**kb (Display Stack Backtrace)**](https://msdn.microsoft.com/library/windows/hardware/ff551943) command to display the current stack trace.

```
kd> kb
ChildEBP RetAddr  Args to Child              
89b2cac4 820da328 97dd800c 86858ce0 00000000 nt!VfReportIssueWithOptions+0x86
89b2caf4 820d92a2 00000001 00000000 97dd65fd nt!ViDeadlockAnalyze+0x1d1
89b2cb7c 820d424e 86858ce0 00000000 97dd65fd nt!VfDeadlockAcquireResource+0x2fd
89b2cb9c 97dd65fd 00007780 89b2cbbc 97dd605a nt!VerifierKfAcquireSpinLock+0x8c
89b2cba8 97dd605a 9a9e7780 88d08f48 00000000 MyTestDriver!DeviceControlIrpWorker+0x54a
89b2cbbc 820c4b4d 9a9e7780 88d08f48 820c4881 MyTestDriver!Dispatch_DeviceControl+0x1a
(Inline) -------- -------- -------- -------- nt!IopfCallDriver+0x47
89b2cbe0 81ca3772 81eb165e b3c9ff80 88d08f48 nt!IovCallDriver+0x2cc
89b2cbf4 81eb165e 88d08fdc 88d08f48 00000000 nt!IofCallDriver+0x62
```

The debugger output shows that the driver in question violated this rule by acquiring and holding Lock A before acquiring Lock B on one thread, and now has acquired Lock B and is attempting to acquire Lock A on another thread. Note that the first thread (Thread 0) is terminated, so the acquisition and subsequent release of those two locks happened at some point since the driver image was loaded.

When proper symbols for the test driver are loaded, the debugger will show the function in which the lock was acquired at the time. In this example, it so happens that both Lock A and Lock B are acquired in the same function. In Thread 0, they are both acquired in *SystemControlIrpWorker*. In Thread 1, they are both acquired in *DeviceControlIrpWorker* (shown in the Lock B output from **!deadlock 3** and the current stack output (**kb**).

At this point, a review of the source code of each function should reveal that a code path exists where the locks can be acquired in such order.

Both *MyTestDriver!AlphaLock* and *MyTestDriver!BravoLock* are objects globally available in the driver:

```
include "MyTestDriverHeader.h"

// Locks used to control access to various objects
extern KSPIN_LOCK AlphaLock;
extern KSPIN_LOCK BravoLock;
```

Inside of function *SystemControlIrpWorker*, there exists a path where AlphaLock (Lock A in the **!deadlock** output) is acquired and held when BravoLock (Lock B) is acquired. It is also worth noting that the locks are properly released in the reverse order in which they’re acquired. (The following code is heavily edited to show only the elements required to generate this scenario).

```ManagedCPlusPlus
NTSTATUS SystemControlIrpWorker(_In_ PIRP Irp)
{
    KIRQL IrqlAlpha;
    KIRQL IrqlBravo;
    // <<Other local variable declarations removed>>

    // <<Various lines of code not shown>>

    KeAcquireSpinLock (&AlphaLock, &IrqlAlpha);

    // <<Various lines of code not shown>>

    KeAcquireSpinLock (&BravoLock, &IrqlBravo);

    // <<Various lines of code not shown>>

    KeReleaseSpinLock (&BravoLock, IrqlBravo);
    KeReleaseSpinLock (&AlphaLock, IrqlAlpha);

    // <<Various lines of code not shown>>
}
```

If you review the following *DeviceControlIrpWorker* example function, you can see that it’s possible to acquire the locks in reverse order. That is, BravoLock can be acquired and held when attempting to acquire AlphaLock. The following example is simplified, but it shows that there is a possible path where a violation could occur.

```ManagedCPlusPlus
NTSTATUS DeviceControlIrpWorker(_In_ PIRP Irp, 
                                _In_ BOOLEAN bSomeCondition)
{
    KIRQL IrqlAlpha;
    KIRQL IrqlBravo;
    // <<Other local variable declarations removed>>

    if (bSomeCondition == FALSE)
    {
        //
        // Note that if bSomeCondition is FALSE, then AlphaLock is acquired here
        // If bSomeCondition is TRUE, it is not needed to be acquired right now
        //
        KeAcquireSpinLock (&AlphaLock, &IrqlAlpha);
    }

    // <<Various lines of code not shown>>

    KeAcquireSpinLock (&BravoLock, &IrqlBravo);

    // <<Various lines of code not shown>>

    if (bSomeCondition == TRUE)
    { 
        //
        // Need to acquire AlphaLock here for upcoming code logic
        //
        KeAcquireSpinLock (&AlphaLock, &IrqlAlpha);

        // <<Various lines of code not shown>>

        KeReleaseSpinLock (&AlphaLock, IrqlAlpha);
    }

    // <<Various lines of code not shown>>

    KeReleaseSpinLock (&BravoLock, IrqlBravo);

    if (bSomeCondition == FALSE)
    {
        //
        // Release the AlphaLock, which was acquired much earlier
        //
        KeReleaseSpinLock (&AlphaLock, IrqlAlpha);
    }

    // <<Various lines of code not shown>>
}
```

To fix this potential violation, the correct thing to do would be to ensure that whenever the driver attempts to acquire AlphaLock, it checks and makes sure BravoLock is not held. The simplest fix could be to simply release BravoLock and re-acquire it as soon as AlphaLock is acquired. But more significant code changes might be necessary if it’s vital that whatever data BravoLock is protecting does not change while waiting for AlphaLock and the re-acquisition of BravoLock.

For more information about spin locks and other synchronization techniques, see [Spin Locks](https://msdn.microsoft.com/library/windows/hardware/ff563830).

## <span id="related_topics"></span>Related topics


[Spin Locks](https://msdn.microsoft.com/library/windows/hardware/ff563830)

[**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187)

[**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326)










