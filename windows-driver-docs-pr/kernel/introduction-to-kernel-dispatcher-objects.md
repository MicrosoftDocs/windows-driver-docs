---
title: Introduction to Kernel Dispatcher Objects
description: Kernel dispatcher objects include timer objects, event objects, semaphore objects, mutex objects, and thread objects.
keywords: ["kernel dispatcher objects WDK , about kernel dispatcher objects", "dispatcher objects WDK kernel , about kernel dispatcher objects", "wait states WDK kernel", "Signaled state WDK kernel", "Not-Signaled state WDK kernel"]
ms.date: 07/21/2021
---

# Introduction to Kernel Dispatcher Objects

The kernel defines a set of object types called *kernel dispatcher objects*, or just *dispatcher objects*. Dispatcher objects include timer objects, event objects, semaphore objects, mutex objects, and thread objects.

Drivers can use dispatcher objects as synchronization mechanisms within a nonarbitrary thread context while executing at IRQL equal to PASSIVE_LEVEL.

## Dispatcher Object States

Every kernel-defined dispatcher object type has a state that is either set to Signaled or set to Not-Signaled.

A group of threads can synchronize their operations if one or more threads call [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject), **KeWaitForMutexObject**, or [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects). These functions take dispatcher object pointers as input and wait until another routine or thread sets one or more dispatcher objects to the Signaled state.

When a thread calls the **KeWaitForSingleObject** to wait for a dispatcher object (or **KeWaitForMutexObject** for a mutex), the thread is put into a *wait* state until the dispatcher object is set to the Signaled state. A thread can call **KeWaitForMultipleObjects** to wait either for any, or for all, of a set of dispatcher objects to be set to Signaled.

Whenever a dispatcher object is set to the Signaled state, the kernel changes the state of any thread waiting for that object to *ready*. (Synchronization timers and synchronization events are exceptions to this rule; when a synchronization event or timer is signaled, only one waiting thread is set to the ready state. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md) and [Event Objects](event-objects.md).) A thread in the ready state will be scheduled to run according to its current run-time [thread priority](thread-priorities.md) and the current availability of processors for any thread with that priority.

### When Can Drivers Wait for Dispatcher Objects?

In general, drivers can wait for dispatcher objects to be set only if at least one of the following circumstances is true:

- The driver is executing in a nonarbitrary thread context.

    That is, you can identify the thread that will enter a wait state. In practice, the only driver routines that execute in a nonarbitrary thread context are the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device), [*Reinitialize*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize), and [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routines of any driver, plus the dispatch routines of highest-level drivers. All these routines are called directly by the system.

- The driver is performing a completely synchronous I/O request.

    That is, no driver queues any operations while handling the I/O request, and no driver returns until the driver below it has finished handling the request.

Additionally, a driver cannot enter a wait state if it is executing at or above IRQL equal to DISPATCH_LEVEL.

Based on these limitations, you must use the following rules:

- The **DriverEntry**, *AddDevice*, *Reinitialize*, and *Unload* routines of any driver can wait for dispatcher objects.

- The dispatch routines of a highest-level driver can wait for dispatcher objects.

- The dispatch routines of lower-level drivers can wait for dispatch objects, if the I/O operation is synchronous, such as create, flush, shutdown, and close operations, some device I/O control operations, and some PnP and power operations.

- The dispatch routines of lower-level drivers cannot wait for a dispatcher object for the completion of asynchronous I/O operations.

- A driver routine that is executing at or above IRQL DISPATCH_LEVEL must not wait for a dispatcher object to be set to the Signaled state.

- A driver must not attempt to wait for a dispatcher object to be set to the Signaled state for the completion of a transfer operation to or from a paging device.

- Driver dispatch routines servicing read/write requests generally cannot wait for a dispatcher object to be set to the Signaled state.

- A dispatch routine for a device I/O control request can wait for a dispatcher object to be set to the Signaled state only if the transfer type for the I/O control code is METHOD_BUFFERED.

- SCSI miniport drivers should not use kernel dispatcher objects. SCSI miniport drivers should call only [SCSI Port Library Routines](/windows-hardware/drivers/ddi/index).

Every other standard driver routine executes in an arbitrary thread context: that of whatever thread happens to be current when the driver routine is called to process a queued operation or to handle a device interrupt. Moreover, most standard driver routines are run at a raised IRQL, either at DISPATCH_LEVEL, or for device drivers, at DIRQL.

If necessary, a driver can create a device-dedicated thread, which can wait for the driver's other routines (except an ISR or [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine) to set a dispatcher object to the Signaled state and reset to the Not-Signaled state.

As a general guideline, if you expect that your new device driver will often need to stall for longer than 50 microseconds while it waits for device-state changes during I/O operations, consider implementing a driver with a device-dedicated thread. If the device driver is also a highest-level driver, consider using [system worker threads](system-worker-threads.md) and implementing one or more worker-thread callback routines. See [**PsCreateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread) and [Managing Interlocked Queues with a Driver-Created Thread](managing-interlocked-queues-with-a-driver-created-thread.md).
