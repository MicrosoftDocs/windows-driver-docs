---
title: Using Framework Locks
description: Using Framework Locks
ms.assetid: d036a2d5-a9e9-4375-84b0-fbd797ee6f13
keywords:
- synchronization WDK KMDF
- synchronization locks WDK KMDF
- locking WDK KMDF
- callback synchronization locks WDK KMDF
- spin locks WDK KMDF
- wait locks WDK KMDF
- interrupt locks WDK KMDF
- framework interrupt locks WDK KMDF
- framework wait locks WDK KMDF
- framework spin locks WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Framework Locks


Sometimes drivers must provide driver-specific synchronization of I/O request-related callback functions, either in addition to or as a replacement for framework-supplied synchronization. Drivers can use callback synchronization locks, spin locks, wait locks, and interrupt locks to synchronize driver code.

### Callback Synchronization Locks

If you have set up your driver to use the framework's [automatic synchronization](using-automatic-synchronization.md) capability, the framework acquires a synchronization lock before calling the driver's I/O request-related event callback functions.

These *callback synchronization locks*, which are associated with framework device objects and queue objects, can also be acquired by drivers. To acquire a synchronization lock, a driver calls [**WdfObjectAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff548721). To release the lock, the driver calls [**WdfObjectReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff548765).

You might want your driver to use the callback synchronization locks if the driver uses the framework's device-level or queue-level synchronization of I/O request-related callback functions but must synchronize some code that runs at IRQL = PASSIVE\_LEVEL with callback functions that run at IRQL = DISPATCH\_LEVEL. This is because drivers can use automatic synchronization only for callback functions that execute at the same IRQL.

For example, a driver can use automatic synchronization for a work-item object only if the execution level of the work-item object's parent is **WdfExecutionLevelPassive** (because a work item's callback function always executes at IRQL= PASSIVE\_LEVEL). Therefore, if a driver specifies **WdfExecutionLevelDispatch** in the **ExecutionLevel** member of a device object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure, the driver cannot set the **AutomaticSerialization** member of a child work-item object's configuration structure. Instead, the driver must acquire a callback synchronization lock to synchronize the [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback functions with the parent device object's callback functions.

### Framework Wait Locks

Use framework wait locks to synchronize access to driver data from code that runs at IRQL = PASSIVE\_LEVEL. Before a driver can use a framework wait lock, it must call [**WdfWaitLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551171) to create a wait-lock object. The driver can then call [**WdfWaitLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff551168) to acquire the lock and [**WdfWaitLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff551173) to release it.

### <a href="" id="framework-spin-locks"></a> Framework Spin Locks

Use framework spin locks to synchronize access to driver data from code that runs at IRQL &lt;= DISPATCH\_LEVEL. When a driver thread acquires a spin lock, the system sets the thread's IRQL to DISPATCH\_LEVEL. When the thread releases the lock, the system restores the thread's IRQL to its previous level.

A driver that is not using automatic framework synchronization might use a spin lock to synchronize access to a device object's context space, if the context space is writable and if more than one of the driver's event callback functions access the space.

Before a driver can use a framework spin lock it must call [**WdfSpinLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550042) to create a spin-lock object. The driver can then call [**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040) to acquire the lock and [**WdfSpinLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff550044) to release it.

For an example use of spin locks, see [Synchronizing Cancellation of Sent Requests](synchronizing-cancellation-of-sent-requests.md).

### Framework Interrupt Locks

For interrupt objects that support DIRQL interrupt handling, framework interrupt locks are spin locks. After your driver acquires an interrupt spin lock, the driver executes at the device's DIRQL until it releases the lock. For more information about using interrupt locks, see [Synchronizing Interrupt Code](synchronizing-interrupt-code.md).

For interrupt objects that support passive-level handling, framework interrupt locks are wait locks. After your driver acquires an interrupt wait lock, the driver executes at IRQL = PASSIVE\_LEVEL until it releases the lock. For more information about passive-level handling, see [Supporting Passive Level Interrupts](supporting-passive-level-interrupts.md).

 

 





