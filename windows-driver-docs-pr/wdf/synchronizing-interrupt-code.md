---
title: Synchronizing Interrupt Code
description: Synchronizing Interrupt Code
ms.assetid: a24477dc-f75d-4ab6-8695-d8a85247e276
keywords:
- hardware interrupts WDK KMDF , synchronization
- interrupts WDK KMDF , synchronization
- synchronization WDK interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Interrupt Code


The following factors complicate driver code that handles hardware interrupts on multiprocessor systems:

-   Each time a device interrupts, it provides interrupt-specific information that is volatile because it can be overwritten the next time that the device interrupts.

-   Devices interrupt at relatively high IRQLs and their interrupt service routines (ISRs) can interrupt the execution of other driver code.

-   For DIRQL interrupts, the ISR must run at DIRQL while holding a driver-supplied spin lock, so that the ISR can prevent additional interrupts while it saves volatile information. The DIRQL prevents interruption by the current processor, and the spin lock prevents interruption by another processor.

-   The ISR must run quickly because the device cannot interrupt while the ISR is executing. Long ISR execution times can slow the system or possibly cause data loss.

-   Both the ISR and the deferred procedure call (DPC) routine must typically access a storage area in which the ISR stores the device's volatile data. These routines must synchronize with each other so that they do not access the storage area at the same time.

Because of all of these factors, you must use the following rules when writing driver code that handles interrupts:

-   Only the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function accesses volatile interrupt data, such as device registers that contain interrupt information.

    The [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function should move the volatile data to a driver-defined interrupt data buffer that the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function, [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function, or multiple [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions can access.

    If your driver provides [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback functions for its interrupt objects, the best place to store interrupt data is the interrupt object's [context space](framework-object-context-space.md). The interrupt object's callback functions can access the object's context space by using the object handle that they receive.

    If your driver provides multiple [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions for each [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, you might store interrupt data in each DPC object's context space.

-   All driver code that accesses the interrupt data buffer must be synchronized so that only one routine accesses the data at a time.

    For DIRQL interrupt objects, the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function accesses this data buffer at IRQL = DIRQL while holding the interrupt object's driver-supplied spin lock. Therefore, all routines that access the buffer must also run at DIRQL while holding the spin lock. (Typically, the interrupt's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function is the only other routine that must access the buffer.)

    All routines that access an interrupt data buffer, except for the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, must do one of the following:

    -   Call [**WdfInterruptSynchronize**](https://msdn.microsoft.com/library/windows/hardware/ff547389) to schedule an [*EvtInterruptSynchronize*](https://msdn.microsoft.com/library/windows/hardware/ff541742) callback function that accesses the interrupt data buffer.
    -   Place code that accesses the interrupt data buffer between calls to [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340) and [**WdfInterruptReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff547376).

    Both of these techniques allow the [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) function to access interrupt data at DIRQL while holding the interrupt's spin lock. The DIRQL prevents interruption by the current processor, and the spin lock prevents interruption by another processor.

    If your device supports multiple interrupt vectors or messages, and if you want to synchronize your driver's handling of these interrupts, you can assign a single spin lock to multiple DIRQL interrupt objects. The framework determines the highest DIRQL of the set of interrupts, and it always acquires the spin lock at that DIRQL so that the synchronized code cannot be interrupted by any interrupt vectors or messages in the set.

    For [passive-level interrupt objects](supporting-passive-level-interrupts.md), the framework acquires the passive-level interrupt lock before calling the driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function at IRQL = PASSIVE\_LEVEL. As a result, all routines that access the buffer must either acquire the interrupt lock or internally synchronize buffer access. Typically, the interrupt's [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function is the only other routine that accesses the buffer. For information about acquiring the interrupt lock from an *EvtInterruptWorkItem* callback function, see the Remarks section of that page.

    You can also synchronize your driver's handling of multiple interrupt vectors by assigning a single wait lock to multiple passive-level interrupt objects.

-   If some of your code that handles DIRQL interrupts must run at IRQL = PASSIVE\_LEVEL, your [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function can create one or more [work items](using-framework-work-items.md) so that the code will run as [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback functions.

    Alternatively, in KMDF versions 1.11 and later, the driver can request an interrupt work item by calling [**WdfInterruptQueueWorkItemForIsr**](https://msdn.microsoft.com/library/windows/hardware/hh439270). (Recall that a driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function can call **WdfInterruptQueueWorkItemForIsr** or [**WdfInterruptQueueDpcForIsr**](https://msdn.microsoft.com/library/windows/hardware/ff547371), but not both.)

-   If it is important to synchronize a driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) and [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback functions with each other and with other callback functions that are associated with a device, your driver can set the **AutomaticSerialization** member to **TRUE** in the interrupt's [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure and the DPC object's [**WDF\_DPC\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551296) structure. Alternatively, the driver can use [framework spin locks](using-framework-locks.md#framework-spin-locks). (Setting the **AutomaticSerialization** member to **TRUE** does not synchronize an [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function with other callback functions. Use [**WdfInterruptSynchronize**](https://msdn.microsoft.com/library/windows/hardware/ff547389) or [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340) to synchronize an *EvtInterruptIsr* callback function, as described previously in this topic.)

For more information about synchronizing driver routines, see [Synchronization Techniques for Framework-Based Drivers](synchronization-techniques-for-wdf-drivers.md).

 

 





