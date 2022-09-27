---
title: Surface Team Driver Development Best Practices
description: Surface Team Driver Development Best Practices - Common mistakes made by driver developers to avoid.
keywords: ["driver development best practices"]
ms.date: 08/06/2019
---

# Surface Team Driver Development Best Practices

## Introduction

These driver development guidelines were developed over many years by driver developers at Microsoft. Over time when drivers misbehaved and lessons were learned, those lessons were captured and evolved to be this set of guidance. These best practices are used by the Microsoft Surface Hardware team to develop and maintain the device driver code that support the unique Surface hardware experiences.

Like any set of guidelines, there will be legitimate exceptions and alternative approaches that will be equally valid. Consider incorporating these guidelines into your development standards or using them to start your domain specific guidelines for your development environment and your unique requirements. 

## Common mistakes made by driver developers

### Handling I/O

1. Accessing buffers retrieved from IOCTLs without validating the length. See [Failure to Check the Size of Buffers](./failure-to-check-the-size-of-buffers.md).
2. Performing blocking I/O in the context of a user thread or random thread context. See [Introduction to Kernel Dispatcher Objects](./introduction-to-kernel-dispatcher-objects.md).
3. Sending synchronous I/O to another driver without timeout. See [Sending I/O Requests Synchronously](../wdf/sending-i-o-requests-synchronously.md).
4. Using neither-io IOCTLs without understanding security implications. See [Using Neither Buffered Nor Direct I/O](./using-neither-buffered-nor-direct-i-o.md).
5. Not checking the return status of [WdfRequestForwardToIoQueue](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestforwardtoioqueue) or not handling failure correctly and resulting in abandoned WDFREQUESTs.
6. Keeping the WDFREQUEST outside the queue in a non-cancelable state. See [Managing I/O Queues](../wdf/managing-i-o-queues.md), [Completing I/O Requests](../wdf/completing-i-o-requests.md) and [Canceling I/O Requests](../wdf/canceling-i-o-requests.md).
7. Trying to manage cancelation using Mark/UnmarkCancelable function instead of using IoQueues. See [Framework Queue Objects](../wdf/framework-queue-objects.md).
8. Not knowing the difference between file handle Cleanup and Close operations. See [Errors in Handling Cleanup and Close Operations](./errors-in-handling-cleanup-and-close-operations.md).
9. Overlooking potential recursions with I/O completion and resubmission from the completion routine.
10. Not being explicit about the power management attributes of WDFQUEUEs. Not documenting the power management choice clearly. This is the primary cause of [Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE](../debugger/bug-check-0x9f--driver-power-state-failure.md) in WDF drivers. When the device is removed, the framework purges IO from the power managed queue and non-power managed queue in different stages of removal process. Non power managed queues are purged when the final IRP\_MN\_REMOVE\_DEVICE is received. So if you are holding I/O in an non-power managed queue, it’s a good practice to explicitly purges the I/O in the context of [EvtDeviceSelfManagedIoFlush](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush) to avoid deadlock.
11. Not following the rules of handling IRPs. See [Errors in Handling Cleanup and Close Operations](./errors-in-handling-cleanup-and-close-operations.md).

### Synchronization

1. Holding locks for code that doesn't need protection. Do not hold a lock for an entire function when only a small number of operations
 needs to be protected.
2. Calling out of drivers with locks held. This is the primary causes of deadlocks.
3. Using interlocked primitives to create a locking scheme instead of using appropriate system provided locking primitives such as mutex,
 semaphore and spinlocks. See [Introduction to Mutex Objects](./introduction-to-mutex-objects.md), [Semaphore Objects](./semaphore-objects.md)
and [Introduction to Spin Locks](./introduction-to-spin-locks.md).
4. Using a spinlock where some type of passive lock would be more appropriate. See [Fast Mutexes and Guarded Mutexes](./fast-mutexes-and-guarded-mutexes.md) and [Event Objects](./event-objects.md). For additional perspective on locks review the OSR Article - [The State of Synchronization](https://www.osr.com/nt-insider/2015-issue3/the-state-of-synchronization/).
5. Opting into WDF synchronization and execution level model without full understanding of implications. See [Using Framework Locks](../wdf/using-framework-locks.md). Unless your driver is monolithic top-level driver directly
interacting with the hardware, avoid opting into WDF synchronization as it can lead to deadlocks due to recursion.
6. Acquiring KEVENT, Semaphore, ERESOURCE, UnsafeFastMutex in the context of multiple threads without entering critical region. Doing
this can lead to DOS attack because a thread holding one of these locks can be suspended. See [Introduction to Kernel Dispatcher Objects](./introduction-to-kernel-dispatcher-objects.md).
7. Allocating KEVENT on thread stack and returning to the caller while the EVENT is still in use. Typically done when used with
[IoBuildSyncronousFsdRequest](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest)
or [IoBuildDeviceIoControlRequest](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest). Caller of these calls should make sure that they don't unwind from the stack until I/O manager has signaled the event when the IRP is
completed.
8. Indefinitely waiting in dispatch routines. In general, any kind of wait in dispatch routine is a bad practice.
9. Inappropriately checking the validity of an object (if blah == NULL) before deleting it. This typically means the author doesn't have
full understanding of the code that controls the lifetime of the object.

### Object Management

1. Not explicitly parenting WDF objects. See [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).
2. Parenting WDF object to WDFDRIVER instead of parenting to an object that provides better lifetime management and optimizes memory usage.
For example, parenting WDFREQUEST to a WDFDEVICE instead of IOTARGET. See [Using General Framework Objects](../wdf/using-general-framework-objects.md), [Framework Object Life Cycle](../wdf/framework-object-life-cycle.md) and [Summary of Framework Objects](../wdf/summary-of-framework-objects.md).
3. Not doing rundown protection of shared memory resources accessed across drivers. See [ExInitializeRundownProtection function](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializerundownprotection).
4. Mistakenly queuing the same work item while the previous one is already in the queue or already running. This is can be a problem if
the client makes an assumption that every work item queued is going to get executed. See [Using Framework WorkItems](../wdf/using-framework-work-items.md). For more information about queuing WorkItems, see the
[DMF\_QueuedWorkitem](https://github.com/Microsoft/DMF/blob/master/Dmf/Modules.Library/Dmf_QueuedWorkItem.md)
module in the Driver Module Framework (DMF) project - <https://github.com/Microsoft/DMF>.
5. Queuing timer before posting the message the timer is expected to process. See [Using Timers](../wdf/using-timers.md).
6. Performing an operation in a workitem that can block or take indefinitely long time to complete.
7. Designing a solution that results in a flood of work items to be queued. It can lead to unresponsive system or DOS attack if the bad
guy can control the action (e.g. pumping I/O in to a driver that queues a new work item for every I/O). See [Using Framework Work
Items](../wdf/using-framework-work-items.md).
8. Not ensuing that work item DPC callbacks have run to completion before deleting the object. See [Guidelines for Writing DPC Routines](./guidelines-for-writing-dpc-routines.md)
and the [WdfDpcCancel function](/windows-hardware/drivers/ddi/wdfdpc/nf-wdfdpc-wdfdpccancel).
9. Creating threads instead of using work items for short duration/non-polling tasks. See [System Worker Threads](./system-worker-threads.md).
10. Not ensuring threads have run to completion before deleting or unload driver. For more information about thread rundown
synchronization, look at the code associated with look at the code associated with [DMF_Thread](https://github.com/Microsoft/DMF/blob/master/Dmf/Modules.Library/Dmf_Thread.md) module in the Driver Module Framework (DMF) project - https://github.com/Microsoft/DMF. 
11. Using a single driver to manage devices that are different but interdependent and using global variables to share information.

### Memory

1. Not marking passive-execution code as PAGEABLE, when possible. Paging driver code can reduce the size of the driver's code
footprint, thus freeing system space for other uses. Be cautious marking code pageable that raises IRQL \>= DISPATCH\_LEVEL or could
be called at raised IRQL. See [When Should Code and Data Be Pageable](./when-should-code-and-data-be-pageable-.md) and [Making Drivers Pageable](./making-drivers-pageable.md) and [Detecting Code That Can Be Pageable](./detecting-code-that-can-be-pageable.md).
2. Declaring large structures on the stack, Should use the heap/poolinstead. See [Using the KernelStack](./using-the-kernel-stack.md) and [Allocating System-Space Memory](./allocating-system-space-memory.md).
3. Unnecessarily zeroing WDF Object context. This can indicate a lack of clarity on when memory will be zeroed out automatically.

### General Driver Guidelines

1. Mixing WDM and WDF primitives. Using WDM primitives where WDF primitives can be used. Using WDF primitives protects you from
gotchas, improves debugging and more importantly makes your driver portable to usermode.
2. Naming FDOs and creating symbolic links when not needed. See [Manage
driver access control](../driversecurity/driver-security-checklist.md#manage-driver-access-control).
3. Copy pasting and using GUIDs and other constant values from sample drivers.
4. Consider the use of the Driver Module Framework (DMF) open source code in your driver project. DMF is an extension to WDF that enables extra functionality for a WDF driver developer. See [Introducing Driver Module Framework](https://blogs.windows.com/windowsdeveloper/2018/08/15/introducing-driver-module-framework/).
5. Using registry as an inter-process notification mechanism or as a mailbox. For an alternative, see
[DMF\_NotifyUserWithEvent](https://github.com/Microsoft/DMF/blob/master/Dmf/Modules.Library/Dmf_NotifyUserWithEvent.md)
and [DMF\_NotifyUserWithRequest](https://github.com/Microsoft/DMF/blob/master/Dmf/Modules.Library/Dmf_NotifyUserWithRequest.md)
modules available in the DMF project - <https://github.com/Microsoft/DMF>.
6. Assuming all parts of registry will be available for access during the early boot phase of the system.
7. Taking dependency on the load order of another driver or service. As the load order can be changed outside of the control of your driver, this can result in a driver that works initially, but later fails in an unpredictable pattern.
8. Recreating driver libraries that are already available, such as WDF provides for PnP described in [Supporting PnP and Power Management in Your Driver](../wdf/supporting-pnp-and-power-management-in-your-driver.md) or those provided in the bus interface as described in the OSR
article [Using Bus Interfaces for Driver to Driver Communication](https://www.osr.com/nt-insider/2014-issue2/using-bus-interfaces-driver-driver-communication/).

### PnP/Power

1. Interfacing with another driver in a non-pnp friendly way - not registering for pnp device change notifications. See [Registering for Device Interface Change Notification](./registering-for-device-interface-change-notification.md).
2. Creating ACPI nodes to enumerate devices and creating power dependencies among them instead of using bus driver or system
provided software device creation interfaces to PNP and power dependencies in an elegant way. See [Supporting PnP and Power Management in Function Drivers](../wdf/supporting-pnp-and-power-management-in-function-drivers.md).
3. Marking the device not-disableable - forcing a reboot on driver update.
4. Hiding the device in the device manager. See [Hiding Devices from Device Manager](./hiding-devices-from-device-manager.md).
5. Making assumptions that driver will be used for only one instance of the device.
6. Making assumptions that driver will never get unloaded. See [PnP Driver's Unload Routine](./pnp-driver-s-unload-routine.md).
7. Not handling spurious interface arrival notification. This can happen and drivers are expected to handle this condition safely.
8. Not implementing a S0 Idle power policy, which is important for devices that are DRIPS constraints or children thereof. See
[Supporting Idle Power-Down](../wdf/supporting-idle-power-down.md).
9. Not checking [WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) return status leads to power reference leak due to WdfDeviceStopIdle/ResumeIdle imbalance and eventually 9F bug check.
10. Not knowing that PrepareHardware/ReleaseHardware can be called more than once due to resource rebalancing. These callbacks should be restricted to initializing hardware resources. See [EVT\_WDF\_DEVICE\_PREPARE\_HARDWARE](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware).
11. Using PrepareHardware/ReleaseHardware for allocating software resources. Software resource allocation static to the device should be done either in AddDevice or in SelfManagedIoInit if the allocation of resources required interacting with hardware. See [EVT\_WDF\_DEVICE\_SELF\_MANAGED\_IO\_INIT](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init).

### Coding Guidelines

1. Not using safe string and integer functions. See [Using Safe String Functions](./using-safe-string-functions.md) and [Using Safe Integer Functions](./ntintsafe-design-guide.md).
2. Not using typedefs for defining constants.
3. Using globals and static variables. Avoid storing per device context in globals. Globals are meant for sharing information across multiple instances of devices. As an alternative, consider using WDFDRIVER object context for sharing information across multiple instances of devices.
4. Not using descriptive names for variables.
5. Not being consistent in naming variables - case consistency. Not following the existing style of coding when making updates to existing code. For example, using different variable names for common structures in different functions.
6. Not commenting important design choices - power management, locks, state management, use of workitems, DPCs, timers, global resource usage, resource pre-allocation, complex expressions/conditional statements.
7. Commenting about things that are obvious from the name of the API being called. Making your comment the English language equivalent of the function name (such as writing the comment “Create the Device Object” when calling WdfDeviceCreate).
8. Don’t create macros that have a return call. See [Functions (C++)](/cpp/cpp/functions-cpp).
9. No or incomplete Source Code Annotations (SAL). See [SAL 2.0 Annotations for Windows Drivers](../devtest/sal-2-annotations-for-windows-drivers.md).
10. Using macros instead of inline functions.
11. Using macros for constants in place of [constexpr](/cpp/cpp/constexpr-cpp)
when using C++
12. Compiling your driver with the C compiler, instead of the C++ compiler to ensure you get strong type checking.

### Error Handling

1. Not reporting critical driver errors and gracefully marking the device non-functional.
2. Not returning appropriate NT error status that translates to meaningful WIN32 error status. See [Using NTSTATUS
Values](./using-ntstatus-values.md).
3. Not using NTSTATUS macros to check the returned status of system functions.
4. Not asserting on state variables or flags where needed.
5. Checking to see if the pointer is valid before accessing it to work around race conditions.
6. ASSERTING on NULL pointers. If you attempt to use a NULL pointer to access memory Windows will bug check. The parameters of the bug check will provide the necessary information to fix the null pointer. Overtime, when many unneeded ASSERT statements are added to the code, they consume memory and slow the system.
7. ASSERTING on object context pointer. The driver framework guarantees that object will always get allocated with context.

### Tracing

1. Not defining WPP custom types and using it in trace calls to get human readable traces messages. See [Adding WPP Software Tracing to a Windows Driver](../devtest/adding-wpp-software-tracing-to-a-windows-driver.md).
2. Not using IFR tracing. See [Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers](../wdf/using-wpp-software-tracing-in-kmdf-and-umdf-2-drivers.md).
3. Calling out function names in WPP trace calls. WPP already tracks function names and line numbers.
4. Not using ETW events to measure performance and other critical user experience impacting events. See [Adding Event Tracing to Kernel-Mode Drivers](../devtest/adding-event-tracing-to-kernel-mode-drivers.md).
5. Not reporting critical errors in eventlog and gracefully marking the device non-functional.

### Verification

1. Not running driver verifier with both standard and advanced settings during development and testing. See [Driver Verifier](../devtest/driver-verifier.md). In the advanced settings, it is recommended to enable all rules, except those rules that are related to low resource simulation. It is preferable to run the low resource simulation tests in isolation to make it easier to debug issues.
2. Not running DevFund test on the driver or the device class the driver is part of with advanced verifier settings enabled. See [How to run the DevFund Tests via the command-line](../devtest/run-devfund-tests-via-the-command-line.md).
3. Not verifying that the driver is HVCI compliant. See [Implement HVCI compatibile code](../driversecurity/implement-hvci-compatible-code.md).
4. Not running AppVerifier on WUDFhost.exe during development and testing of user mode drivers. See [Application Verifier](../devtest/application-verifier.md).
5. Not checking usage of memory using the [\!wdfpoolusage](../debugger/-wdfkd-wdfpoolusage.md)
 debugger extension at runtime to make sure WDF objects are not abandoned. Memory, requests and workitems are common victims of these issues.
6. Not using the [\!wdfkd](../debugger/kernel-mode-driver-framework-extensions--wdfkd-dll-.md)
 debugger extension to inspect the object tree to make sure objects are parented correctly and checking the attributes of major objects such WDFDRIVER, WDFDEVICE, IO.
