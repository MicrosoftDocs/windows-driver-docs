---
title: Synchronization and Notification in Network Drivers
description: Synchronization and Notification in Network Drivers
ms.assetid: 9fd9306f-5431-485f-9d6b-f7d6f25ea1ce
keywords:
- synchronizing access to resources WDK networking
- synchronization WDK networking
- notification WDK networking
- spin locks WDK networking
- network drivers WDK , notifying drivers about events
- notifying drivers about events WDK networking
- shared resources WDL networking
- timers WDK networking
- event notifications WDK networking
- events WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronization and Notification in Network Drivers





Whenever two threads of execution share resources that can be accessed at the same time, either in a uniprocessor computer or on a symmetric multiprocessor (SMP) computer, they need to be synchronized. For example, on a uniprocessor computer, if one driver function is accessing a shared resource and is interrupted by another function that runs at a higher IRQL, such as an ISR, the shared resource must be protected to prevent race conditions that leave the resource in an indeterminate state. On an SMP computer, two threads could be running simultaneously on different processors and attempting to modify the same data. Such accesses must be synchronized.

NDIS provides spin locks that you can use to synchronize access to shared resources between threads that run at the same IRQL. When two threads that share a resource run at different IRQLs, NDIS provides a mechanism for temporarily raising the IRQL of the lower IRQL code so that access to the shared resource can be serialized.

When a thread depends on the occurrence of an event outside the thread, the thread relies on notification. For example, a driver might need to be notified when some time period has passed so that it can check its device. Or a network interface card (NIC) driver might have to perform a periodic operation such as polling. Timers provide such a mechanism.

Events provide a mechanism that two threads of execution can use to synchronize operations. For example, a miniport driver can test the interrupt on a NIC by writing to the device. The driver must wait for an interrupt to notify the driver that the operation was successful. You can use events to synchronize an operation between the thread waiting for the interrupt to complete and the thread that handles the interrupt.

The following subsections in this topic describe these NDIS mechanisms.

-   [Spin Locks](#spin-locks)
-   [Avoiding Spin Lock Problems](#avoiding-spin-lock-problems)
-   [Timers](#timers)
-   [Events](#events)

### Spin Locks

A *spin lock* provides a synchronization mechanism for protecting resources shared by kernel-mode threads running at IRQL &gt; PASSIVE\_LEVEL in either a uniprocessor or a multiprocessor computer. A spin lock handles synchronization among various threads of execution that are running concurrently on an SMP computer. A thread acquires a spin lock before accessing protected resources. The spin lock keeps any thread but the one holding the spin lock from using the resource. On a SMP computer, a thread that is waiting on the spin lock loops attempting to acquire the spin lock until it is released by the thread that holds the lock.

Another characteristic of spin locks is the associated IRQL. Attempted acquisition of a spin lock temporarily raises the IRQL of the requesting thread to the IRQL associated with the spin lock. This prevents all lower IRQL threads on the same processor from preempting the executing thread. Threads, on the same processor, running at a higher IRQL can preempt the executing thread, but these threads cannot acquire the spin lock because it has a lower IRQL. Therefore, after a thread has acquired a spin lock, no other threads can acquire the spin lock until it has been released. A well-written network driver minimizes the amount of time a spin lock is held.

A typical use for a spin lock is to protect a queue. For example, the miniport driver send function, [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440), might queue packets passed to it by a protocol driver. Because other driver functions also use this queue, *MiniportSendNetBufferLists* must protect the queue with a spin lock so that only one thread at a time can manipulate the links or contents. *MiniportSendNetBufferLists* acquires the spin lock, adds the packet to the queue and then releases the spin lock. Using a spin lock ensures that the thread holding the lock is the only thread modifying the queue links while the packet is safely added to the queue. When the miniport driver takes the packets off the queue, such an access is protected by the same spin lock. When running instructions that modify the head of the queue or any of the link fields making up the queue, the driver must protect the queue with a spin lock.

A driver must take care not to overprotect a queue. For example, the driver can perform some operations (for example, filling in a field containing the length) in the network driver-reserved field of a packet before it queues the packet. The driver can do this outside the code region protected by the spin lock, but must do it before queuing the packet. After the packet is on the queue and the running thread releases the spin lock, the driver must assume that other threads can dequeue the packet immediately.

### Avoiding Spin Lock Problems

To avoid a possible deadlock, an NDIS driver should release all NDIS spin locks before calling an NDIS function other than an **Ndis*Xxx*Spinlock** function. If an NDIS driver does not comply with this requirement, a deadlock could occur as follows:

1. Thread 1, which holds NDIS spin lock A, calls an **Ndis*Xxx*** function that attempts to acquire NDIS spin lock B by calling the [**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699) function.

2. Thread 2, which holds NDIS spin lock B, calls an **Ndis*Xxx*** function that attempts to acquire NDIS spin lock A by calling the **NdisAcquireSpinLock** function.

3. Thread 1 and thread 2, which are each waiting for the other to release its spin lock, become deadlocked.

Microsoft Windows operating systems do not restrict a network driver from simultaneously holding more than one spin lock. However, if one section of the driver attempts to acquire spin lock A while holding spin lock B, and another section attempts to acquire spin lock B while holding spin lock A, deadlock results. If it acquires more than one spin lock, a driver should avoid deadlock by enforcing an order of acquisition. That is, if a driver enforces acquiring spin lock A before spin lock B, the situation described above will not occur.

Acquiring a spin lock raises the IRQL to DISPATCH\_LEVEL and stores the old IRQL in the spin lock. Releasing the spin lock sets the IRQL to the value stored in the spin lock. Because NDIS sometimes enters drivers at PASSIVE\_LEVEL, problems can arise with the following code sequence:

```syntax
NdisAcquireSpinLock(A);
NdisAcquireSpinLock(B);
NdisReleaseSpinLock(A);
NdisReleaseSpinLock(B);
```

A driver should not access spin locks in this sequence for the following reasons:

-   Between releasing spin lock A and releasing spin lock B, the code is running at PASSIVE\_LEVEL instead of DISPATCH\_LEVEL and is subject to inappropriate interruption.

-   After releasing spin lock B, the code is running at DISPATCH\_LEVEL which could cause the caller to fault at much later time with an IRQL\_NOT\_LESS\_OR\_EQUAL stop error.

Using spin locks impacts performance and, in general, a driver should not use many spin locks. Occasionally, functions that are usually distinct (for example, send and receive functions) have minor overlaps for which two spin locks can be used. Use of more than one spin lock might be a worthwhile tradeoff in order to allow the two functions to operate independently on separate processors.

### Timers

Timers are used for polling or timing out operations. A driver creates a timer and associates a function with the timer. The associated function is called when the period specified in the timer expires. Timers can be one-shot or periodic. Once a periodic timer is set, it will continue to fire at the expiration of every period until explicitly cleared. A one-shot timer must be reset each time it fires.

Timers are created and initialized by calling [**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618) and set by calling [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563). If a nonperiodic timer is used, it must reset by calling **NdisSetTimerObject**. A timer is cleared by calling [**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624).

### Events

Events are used to synchronize operations between two threads of execution. An event is allocated by a driver and initialized by calling [**NdisInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562732). A thread running at IRQL = PASSIVE\_LEVEL calls [**NdisWaitEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564651) to put itself into a wait state. When a driver thread waits on an event, it specifies a maximum time to wait as well as the event to be waited on. The thread's wait is satisfied when [**NdisSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564539) is called causing the event to be signaled, or when the specified maximum wait-time interval expires, whichever occurs first.

Typically, the event is set by a cooperating thread that calls **NdisSetEvent**. Events are unsignaled when they are created and must be set in order to signal waiting threads. Events remain signaled until [**NdisResetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564526) is called.

## Related topics


[Multiprocessor Support in Network Drivers](multiprocessor-support-in-network-drivers.md)

 

 






