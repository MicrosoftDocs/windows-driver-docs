---
title: Queued Spin Locks
description: Queued Spin Locks
keywords: ["queued spin locks WDK kernel", "first-come first-served spin locks WDK kernel", "KeAcquireInStackQueuedSpinLock"]
ms.date: 04/24/2024
ai-usage: ai-assisted
---

# Queued Spin Locks


*Queued spin locks* are a variant of spin locks that work well for highly contended locks.  Traditional, unqueued spin locks are a better choice for lightly contended or shorter duration locks.

Benefits of using a queued spin lock include:  
   
1. **Reduced Processor Contention**: Traditional spin locks can lead to significant processor contention when multiple threads attempt to acquire the lock simultaneously, as they continuously loop (or "spin") checking the lock status. This can degrade system performance, especially on multiprocessor systems. Queued spin locks mitigate this by organizing threads into a queue. When a thread acquires a lock, only the next in line is actively spinning, waiting to acquire the lock. This reduces the CPU cycles wasted on spinning, especially when the lock is held for longer durations.  
   
2. **Fairness and Avoidance of Starvation**: One of the problems with basic spin locks is the lack of fairness; a thread can be starved and never acquire the lock if other threads are continuously acquiring and releasing it. Queued spin locks address this by ensuring that threads acquire the lock in the order they attempted to. This sequential handling prevents starvation and ensures that all threads get serviced over time.  
   
3. **Scalability**: As the number of processors or cores increases in a system, the efficiency of synchronization mechanisms becomes critical for performance. Queued spin locks are more scalable than traditional spin locks because they reduce the overhead on the processors by minimizing the active spinning across all cores. This is particularly important in high-performance, multi-core systems where driver efficiency can directly impact the overall system performance.  
   
4. **Efficient Use of System Resources**: By reducing unnecessary processor spinning, queued spin locks allow the system to use its resources more efficiently. This not only improves the performance of the device driver but also has a positive impact on the system's overall responsiveness and power consumption, which is especially beneficial in power-sensitive environments.  
   
5. **Simplicity and Reliability**: Despite their advantages in reducing contention and improving fairness, queued spin locks abstract the complexity away from the developer. They provide a simple and reliable mechanism for protecting shared resources without the developer having to implement complex locking logic. This simplicity reduces the likelihood of bugs related to improper lock handling, thus enhancing the reliability of the driver.

Below is a simplified code snippet demonstrating the described operations with a queued spin lock in a Windows Kernel Mode Driver. This example shows how to declare and initialize a spin lock using [**KeInitializeSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializespinlock), then acquire and release the lock using [**KeAcquireInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlock) and [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock), respectively.

```cpp
KSPIN_LOCK SpinLock;  
KLOCK_QUEUE_HANDLE LockHandle;  

// Initialize the spin lock  
KeInitializeSpinLock(&SpinLock);  

// Assume this function is called in some kind of context where   
// the below operations make sense, e.g., in a device I/O path  

// Acquire the queued spin lock  
KeAcquireInStackQueuedSpinLock(&SpinLock, &LockHandle);  

// At this point, the current thread holds the spin lock.  
// Perform thread-safe operations here.  
    
// ...  

// Release the queued spin lock  
KeReleaseInStackQueuedSpinLock(&LockHandle);  
```

The driver allocates a [**KLOCK\_QUEUE\_HANDLE**](./eprocess.md) structure that it passes by pointer to **KeAcquireInStackQueuedSpinLock**. The driver passes the same structure by pointer to **KeReleaseInStackQueuedSpinLock** when it releases the spin lock.

Drivers should normally allocate the structure on the stack each time they acquire the lock. A driver should not allocate the structure as part of its device context and then share the same structure from multiple threads.

Drivers must not mix calls to the queued spin lock routines and the ordinary **Ke*Xxx*SpinLock** routines on the same spin lock.

If the driver is already at IRQL = DISPATCH\_LEVEL, it can call [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquireinstackqueuedspinlockatdpclevel) and [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel) instead.

   
   
