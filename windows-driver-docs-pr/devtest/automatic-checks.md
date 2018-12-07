---
title: Automatic Checks
description: Automatic Checks
ms.assetid: ec3cb6a4-d990-4830-914c-064f6c79371a
keywords:
- automatic checks WDK Driver Verifier
- IRQL monitoring WDK Driver Verifier
- stack switching WDK Driver Verifier
- free pool timers WDK Driver Verifier
- clean up checks WDK Driver Verifier
- switching stacks WDK Driver Verifier
- driver unloads WDK Driver Verifier
- Driver Verifier options, Monitoring IRQL and Memory Routines
- Driver Verifier options, Monitoring Stack Switching
- Driver Verifier options, Checking on Driver Unload
- Driver Verifier options, Monitoring Driver Dispatch Routines
- Driver Verifier options, Monitoring Memory Dispatch List (MDL) Usage
ms.date: 10/20/2017
ms.localizationpriority: medium
---

# Automatic Checks


## <span id="ddk_automatic_checks_tools"></span><span id="DDK_AUTOMATIC_CHECKS_TOOLS"></span>


Driver Verifier performs the following checks whenever it is verifying one or more drivers. You cannot activate or deactivate these checks. Starting in the Windows 10, version 1709, these automatic checks have been moved into relevant [standard flags](verifier-command-line.md). As a result, users enabling Driver Verifier with the standard flags should see no reduction in checks applied.

### <span id="ddk_monitoring_irql_and_memory_routines_tools"></span><span id="DDK_MONITORING_IRQL_AND_MEMORY_ROUTINES_TOOLS"></span>Monitoring IRQL and Memory Routines

Driver Verifier monitors the selected driver for the following forbidden actions:

-   Raising IRQL by calling **KeLowerIrql**

-   Lowering IRQL by calling **KeRaiseIrql**

-   Requesting a size zero memory allocation

-   Allocating or freeing paged pool with IRQL &gt; APC\_LEVEL

-   Allocating or freeing nonpaged pool with IRQL &gt; DISPATCH\_LEVEL

-   Trying to free an address that was not returned from a previous allocation

-   Trying to free an address that was already freed

-   Acquiring or releasing a fast mutex with IRQL &gt; APC\_LEVEL

-   Acquiring or releasing a spin lock with IRQL not equal to DISPATCH\_LEVEL

-   Double-releasing a spin lock.

-   Marking an allocation request MUST\_SUCCEED. No such requests are ever permissible.

If Driver Verifier is not active, these violations might not cause an immediate system crash in all cases. Driver Verifier monitors the driver's behavior and issues bug check 0xC4 if any of these violations occur. See [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION) for a list of the bug check parameters.

### <span id="ddk_monitoring_stack_switching_tools"></span><span id="DDK_MONITORING_STACK_SWITCHING_TOOLS"></span>Monitoring Stack Switching

Driver Verifier monitors stack usage by the driver being verified. If the driver switches its stack, and the new stack is neither a thread stack nor a DPC stack, then a bug check is issued. (This will be bug check 0xC4 with the first parameter equal to 0x90.) The stack displayed by the **KB** debugger command will usually reveal the driver that performed this operation.

### <span id="ddk_checking_on_driver_unload_tools"></span><span id="DDK_CHECKING_ON_DRIVER_UNLOAD_TOOLS"></span>Checking on Driver Unload

After a driver that is being verified unloads, Driver Verifier performs several checks to make sure that the driver has cleaned up.

In particular, Driver Verifier looks for:

-   Undeleted timers

-   Pending deferred procedure calls (DPCs)

-   Undeleted lookaside lists

-   Undeleted worker threads

-   Undeleted queues

-   Other similar resources

Problems such as these can potentially cause system bug checks to be issued a while after the driver unloads, and the cause of these bug checks can be hard to determine. When Driver Verifier is active, such violations will result in bug check 0xC7 being issued immediately after the driver is unloaded. See [**Bug Check 0xC7**](https://msdn.microsoft.com/library/windows/hardware/ff560198) (TIMER\_OR\_DPC\_INVALID) for a list of the bug check parameters.


### <span id="Monitoring__Memory_Descriptor_List__MDL__Usage"></span><span id="monitoring__memory_descriptor_list__mdl__usage"></span><span id="MONITORING__MEMORY_DESCRIPTOR_LIST__MDL__USAGE"></span>Monitoring Memory Descriptor List (MDL) Usage

In Windows Vista, Driver Verifier also monitors the selected driver for the following forbidden actions:

-   Calling [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) or MmProbeAndLockProcessPages on an MDL that does not have the appropriate flags. For example, it is incorrect to call **MmProbeAndLockPages** for an MDL that has been created by using [**MmBuildMdlForNonPagedPool**](https://msdn.microsoft.com/library/windows/hardware/ff554498).

-   Calling [**MmMapLockedPages**](https://msdn.microsoft.com/library/windows/hardware/ff554622) on an MDL that does not have the appropriate flags. For example, it is incorrect to call **MmMapLockedPages** for an MDL that is already mapped to a system address or and MDL that is not locked.

-   Calling [**MmUnlockPages**](https://msdn.microsoft.com/library/windows/hardware/ff556381) or [**MmUnmapLockedPages**](https://msdn.microsoft.com/library/windows/hardware/ff556391) on a partial MDL, that is, and MDL created by using [**IoBuildPartialMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548324).

-   Calling **MmUnmapLockedPages** on an MDL that is not mapped to a system address.

If Driver Verifier is not active, these violations might not cause the system to stop responding immediately in all cases. Driver Verifier monitors the driver's behavior and issues bug check 0xC4 if any of these violations occur. See [**Bug Check 0xC4**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (DRIVER\_VERIFIER\_DETECTED\_VIOLATION) for a list of the bug check parameters.

### <span id="Synchronization_Object_Allocation_from_NonPagedPoolSession_Memory"></span><span id="synchronization_object_allocation_from_nonpagedpoolsession_memory"></span><span id="SYNCHRONIZATION_OBJECT_ALLOCATION_FROM_NONPAGEDPOOLSESSION_MEMORY"></span>Synchronization Object Allocation from NonPagedPoolSession Memory

Starting in Windows 7, Driver Verifier checks for synchronization objects from session memory.

Synchronization objects must be nonpageable. They must also live in the global, system-wide virtual address space.

A graphics driver can allocate session memory by calling APIs such as [**EngAllocMem**](https://msdn.microsoft.com/library/windows/hardware/ff564176). Unlike the global address space, the session address space is virtualized for each Terminal Server session. This means that the same virtual address that is used in the context of two different sessions refers to two different objects. The Windows kernel must be able to access synchronization objects from any Terminal Server session. Trying to reference a session memory address from a different session has unpredictable results, such as system crashes or silent corruption of another session’s data.

Starting in Windows 7, when a verified driver initializes a synchronization object by calling APIs such as [**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137) or [**KeInitializeMutex**](https://msdn.microsoft.com/library/windows/hardware/ff552147), Driver Verifier checks whether the address of the object falls inside the session virtual address space. If Driver Verifier detects this kind of incorrect address, it issues a [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with a parameter 1 value of 0xDF.

### <span id="Object_Reference_Counter_Changes_from_0_to_1"></span><span id="object_reference_counter_changes_from_0_to_1"></span><span id="OBJECT_REFERENCE_COUNTER_CHANGES_FROM_0_TO_1"></span>Object Reference Counter Changes from 0 to 1

Starting in Windows 7, Driver Verifier checks for additional classes of incorrect object references.

When the Windows kernel object manager creates an object, such as a File object or a Thread object, the new object’s reference counter is set to 1. The reference counter is incremented by calls to APIs such as [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686) or [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679). The reference counter is decremented by every [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) call for the same object.

After the reference counter reaches the 0 value, the object becomes eligible to be freed. The object manager might free it immediately, or it might free it later. Calling [**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686) or [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) and changing the reference counter from 0 to 1 means incrementing the reference counter of an already freed object. This is always incorrect because it can result in corrupting someone else’s memory allocation.

### <span id="System_Shutdown_Blocks_or_Delays"></span><span id="system_shutdown_blocks_or_delays"></span><span id="SYSTEM_SHUTDOWN_BLOCKS_OR_DELAYS"></span>System Shutdown Blocks or Delays

Starting in Windows 7, Driver Verifier issues a break into the kernel debugger if the system shutdown does not finish 20 minutes after it started. Driver Verifier assigns the start of the system shutdown as the time when the Windows kernel begins shutting down its various subsystems, such as the Registry, Plug And Play, or the I/O manager subsystems.

If a kernel debugger is not attached to the system, Driver Verifier issues a [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187), with a parameter 1 value of 0x115, instead of this breakpoint.

Frequently a system shutdown that cannot finish in less than 20 minutes indicates that one of the drivers that is running on that system is malfunctioning. Running **!analyze -v** from the kernel debugger displays the stack trace of the system worker thread that is responsible for the shutdown. You should examine that stack trace and determine whether the shutdown thread is blocked by one of the drivers that are being tested.

Sometimes the system cannot shut down because it is subject to heavy stress testing—even though all drivers are functioning correctly. The user can choose to continue the execution after this Driver Verifier breakpoint and check whether the system eventually shuts down.

 

 





