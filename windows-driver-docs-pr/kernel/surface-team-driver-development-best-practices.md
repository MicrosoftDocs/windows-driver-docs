---
title: Surface Team Driver Development Best Practices
description: Surface Team Driver Development Best Practices - Common mistakes made by driver developers to avoid.
ms.assetid: f4847954-8e29-48bb-b9ae-873fc7c29b2d
keywords: ["driver development best practices"]
ms.date: 08/05/2019
ms.localizationpriority: medium
---

# Surface Team Driver Development Best Practices

## Introduction

These driver development guidelines were developed over many years by driver developers at Microsoft. Over time when drivers misbehaved and lessons were learned, those lessons were captured and evolved to be this set of guidance. These best practices are used by the Microsoft Surface Hardware team to develop and maintain the device driver code that support the unique Surface hardware experiences.
 
Like any set of guidelines, there will be legitimate exceptions and alternative approaches that will be equally valid. Consider incorporating these guidelines into your development standards or using them to start your domain specific guidelines for your development environment and your unique requirements. 

## Common mistakes made by driver developers

### Handling I/O

- Accessing buffers retrieved from IOCTLs without validating the length. See Failure to Check the Size of Buffers.
- Performing blocking I/O in the context of a user thread or random thread context. See Introduction to Kernel Dispatcher Objects.
- Sending synchronous I/O to another driver without timeout. See Sending I/O Requests Synchronously
- Using neither-io IOCTLs without understanding security implications. See Using Neither Buffered Nor Direct I/O.
- Not checking the return status of WdfRequestForwardToIoQueue or not handling failure correctly and resulting in abandoned WDFREQUESTs.
- Keeping the WDFREQUEST outside the queue in a non-cancelable state. See Managing I/O Queues, Completing I/O Requests and Canceling I/O Requests
- Trying to manage cancelation using Mark/UnmarkCancelable function instead of using IoQueues. See Framework Queue Objects
- Not knowing the difference between file handle Cleanup and Close operations. See Errors in Handling Cleanup and Close Operations.
- Overlooking potential recursions with I/O completion and resubmission from the completion routine.
- Not being explicit about the power management attributes of WDFQUEUEs. Not documenting the power management choice clearly. This is the primary cause of Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE in WDF drivers. When the device is removed, the framework purges IO from the power managed queue and non-power managed queue in different stages of removal process. Non power managed queues are purged when the final IRP_MN_REMOVE_DEVICE is received. So if you are holding I/O in an non-power managed queue, it’s a good practice to explicitly purges the I/O in the context of EvtDeviceSelfManagedIoFlush to avoid deadlock.
- Not following the rules of handling IRPs. See Different ways of handling IRPs - Cheat sheet. Review mistake 7 in the Synchronization section.
- Assuming EvtIo callbacks will be called in the usermode process context.

### Synchronization

Holding locks for code that doesn't need protection. Do not hold a lock for an entire function when only a small number of operations needs to be protected.
Calling out of drivers with locks held. Primary causes of deadlocks.
Using interlocked primitives to create a locking scheme instead of using appropriate system provided locking primitives such as mutex, semaphore and spinlocks. See Introduction to Mutex Objects, Semaphore Objects and Introduction to Spin Locks.
Using a spinlock where some type of passive lock would be more appropriate. See Fast Mutexes and Guarded Mutexes and Event Objects.For additional perspective on locks review the OSR Article - The State of Synchronization.
Opting into WDF synchronization and execution level model without full understanding of implications. See Using Framework Locks. Unless your driver is monolithic top-level driver directly interacting with the hardware, avoid opting into WDF synchronization as it can lead to deadlocks due to recursion.
Acquiring KEVENT, Semaphore, ERESOURCE, UnsafeFastMutex in the context of multiple threads without entering critical region. Doing this can lead to DOS attack because a thread holding one of these locks can be suspended. See Synchronization Techniques.
Allocating KEVENT on thread stack and returning to the caller while the EVENT is still in use. Typically done when used with IoBuildSyncronousFsdRequest or IoBuildDeviceIoControlRequest. Caller of these calls should make sure that they don't unwind from the stack until I/O manager has signaled the event when the IRP is completed.
Indefinitely waiting in dispatch routines. In general, any kind of wait in dispatch routine is a bad practice.
Inappropriately checking the validity of an object (if blah == NULL) before deleting it. This typically means the author doesn't have full understanding of the code that controls the lifetime of the object.

### Object Management

Not explicitly parenting WDF objects. See Introduction to Framework Objects.
Parenting WDF object to WDFDRIVER instead of parenting to an object that provides better lifetime management and optimizes memory usage. For example, parenting WDFREQUEST to a WDFDEVICE instead of IOTARGET. See Using General Framework Objects, Framework Object Life Cycle and Summary of Framework Objects.
Not doing rundown protection of shared memory resources accessed across drivers. See ExInitializeRundownProtection function.
Mistakenly queuing the same work item while the previous one is already in the queue or already running. This is can be a problem if the client makes an assumption that every work item queued is going to get executed. See Using Framework Work Items. For more information about queuing WorkItems, see the DMF_QueuedWorkitem module in the Driver Module Framework (DMF) project - https://github.com/Microsoft/DMF.
Queuing timer before posting the message the timer is expected to process. See Using Timers.
Performing an operation in a workitem that can block or take indefinitely long time to complete.
Designing a solution that results in a flood of work items to be queued. It can lead to unresponsive system or DOS attack if the bad guy can control the action (e.g. pumping I/O in to a driver that queues a new work item for every I/O). See Using Framework Work Items.
Not ensuing that work item DPC callbacks have run to completion before deleting the object. See Guidelines for Writing DPC Routines and the WdfDpcCancel function.
Creating threads instead of using work items for short duration/non-polling tasks. See System Worker Threads
Not ensuring threads have run to completion before deleting or unload driver. For more information about thread rundown synchronization, look at the code associated with DMF_Thread module in the Driver Module Framework (DMF) project - https://github.com/Microsoft/DMF. 
Using a single driver to manage devices that are different but interdependent and using global variables to share information.

### Memory

Not marking passive-execution code as PAGEABLE, when possible. Paging driver code can reduce the size of the driver's code footprint, thus freeing system space for other uses. Be cautious marking code pageable that raises IRQL >= DISPATCH_LEVEL or could be called at raised IRQL. See When Should Code and Data Be Pageable  and Making Drivers Pageable and Detecting Code That Can Be Pageable.
Declaring large structures on the stack, Should use the heap/pool instead. See Using the Kernel Stack and Allocating System-Space Memory.
Unnecessarily zeroing WDF Object context. This can indicate a lack of clarity on when memory will be zeroed out automatically.

### General Driver Guidelines

Mixing WDM and WDF primitives. Using WDM primitives where WDF primitives can be used. Using WDF primitives protects you from gotchas, improves debugging and more importantly makes your driver portable to usermode.
Naming FDOs and creating symbolic links when not needed. See Manage driver access control.
Copy pasting and using GUIDs and other constant values from sample drivers.
Consider the use of the Driver Module Framework (DMF) open source code in your driver project. DMF is an extension to WDF that enables extra functionality for a WDF driver developer.  See Introducing Driver Module Framework.
Using registry as an inter-process notification mechanism or as a mailbox. For an alternative, see DMF_NotifyUserWithEvent and DMF_NotifyUserWithRequest modules available in the DMF project - https://github.com/Microsoft/DMF.
Assuming all parts of registry will be available for access during the early boot phase of the system.
Taking dependency on the load order of another driver or service. As the load order can be changed outside of the control of your driver, this can result in a driver that works initially, but later fails in an unpredictable pattern.
Recreating driver libraries that are already available, such as WDF provides for PnP described in Supporting PnP and Power Management in Your Driver or those provided in the bus interface as described in the OSR article Using Bus Interfaces for Driver to Driver Communication.

### PnP/Power

Interfacing with another driver in a non-pnp friendly way - not registering for pnp device change notifications. See Registering for Device Interface Change Notification
Creating ACPI nodes to enumerate devices and creating power dependencies among them instead of using bus driver or system provided software device creation interfaces to PNP and power dependencies in an elegant way. See Supporting PnP and Power Management in Function Drivers.
Marking the device not-disableable - forcing a reboot on driver update.
Hiding the device in the device manager. See Hiding Devices from Device Manager.
Making assumptions that driver will be used for only one instance of the device.
Making assumptions that driver will never get unloaded. See PnP Driver's Unload Routine.
Not handling spurious interface arrival notification. This can happen and drivers are expected to handle this condition safely.
Not implementing a S0 Idle power policy, which is important for devices that are DRIPS constraints or children thereof. See Supporting Idle Power-Down.
Not checking WdfDeviceStopIdle return status leads to power reference leak due to WdfDeviceStopIdle/ResumeIdle imbalance and eventually 9F bug check.
Not knowing that PrepareHardware/ReleaseHardware can be called more than once due to resource rebalancing. These callbacks should be restricted to initializing hardware resources. See EVT_WDF_DEVICE_PREPARE_HARDWARE.
Using PrepareHardware/ReleaseHardware for allocating software resources. Software resource allocation static to the device should be done either in AddDevice or in SelfManagedIoInit if the allocation of resources required interacting with hardware. See EVT_WDF_DEVICE_SELF_MANAGED_IO_INIT..

### Coding Guidelines

Not using safe string and integer functions. See Using Safe String Functions and Using Safe Integer Functions.
Not using typedefs for defining constants.
Using globals and static variables. Avoid storing per device context in globals. Globals are meant for sharing information across multiple instances of devices. As an alternative, consider using WDFDRIVER object context for sharing information across multiple instances of devices.
Not using descriptive names for variables.
Not being consistent in naming variables - case consistency. Not following the existing style of coding when making updates to existing code. For example, using different variable names for common structures in different functions. 
Not commenting important design choices - power management, locks, state management, use of workitems, DPCs, timers, global resource usage, resource pre-allocation, complex expressions/conditional statements.
Commenting about things that are obvious from the name of the API being called. Making your comment the English language equivalent of the function name (such as writing the comment “Create the Device Object” when calling WdfDeviceCreate).
Don’t create macros that have a return call. See Functions (C++).
No or incomplete Source Code Annotations (SAL). See SAL 2.0 Annotations for Windows Drivers.
Using macros instead of inline functions.
Using macros for constants in place of constexpr  when using C++
Compiling your driver with the C compiler, instead of the C++ compiler to ensure you get strong type checking.

### Error Handling

Not reporting critical driver errors and gracefully marking the device non-functional.
Not returning appropriate NT error status that translates to meaningful WIN32 error status. See Using NTSTATUS Values.
Not using NTSTATUS macros to check the returned status of system functions.
Not asserting on state variables or flags where needed.
Checking to see if the pointer is valid before accessing it to work around race conditions.
ASSERTING on NULL pointers. If you attempt to use a NULL pointer to access memory Windows will bug check. The parameters of the bug check will provide the necessary information to fix the null pointer. Overtime, when many unneeded ASSERT statements are added to the code, they consume memory, slow the system and make checked build binaries unusable. Note that asserts are not included in the free retail build.
ASSERTING on object context pointer. The driver framework guarantees that object will always get allocated with context.

### Tracing

Not defining WPP custom types and using it in trace calls to get human readable traces messages. See Adding WPP Software Tracing to a Windows Driver.
Not using IFR tracing. See Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers.
Calling out function names in WPP trace calls. WPP already tracks function names and line numbers.
Not using ETW events to measure performance and other critical user experience impacting events. See Adding Event Tracing to Kernel-Mode Drivers
Not reporting critical errors in eventlog and gracefully marking the device non-functional.

### Verification

Not running driver verifier with both standard and advanced settings during development and testing. See Driver Verifier. In the advanced settings, it is recommended to enable all rules, except those rules that are related to low resource simulation. It is preferable to run the low resource simulation tests in isolation to make it easier to debug issues.
Not running DevFund test on the driver or the device class the driver is part of with advanced verifier settings enabled. See How to run the DevFund Tests via the command-line.
Not verifying to make sure the driver is HVCI compliant. See Evaluate HVCI driver compatibility.
Not running AppVerifier on WUDFhost.exe during development and testing of user mode drivers. See Application Verifier.
Not checking usage of memory using the !wdfpoolusage debugger extension at runtime to make sure WDF objects are not abandoned. Memory, requests and workitems are common victims of these issues.
Not using the !wdfkd debugger extension to inspect the object tree to make sure objects are parented correctly and checking the attributes of major objects such WDFDRIVER, WDFDEVICE, IOTARGETs to make sure the properties set on them are as expected.
