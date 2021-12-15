---
title: Synchronizing Interrupt Code
description: Learn about synchronizing interrupt code. See factors that complicate driver code for hardware interrupts and view rules used to avoid those complications.
keywords:
- hardware interrupts WDK KMDF , synchronization
- interrupts WDK KMDF , synchronization
- synchronization WDK interrupts
ms.date: 04/20/2017
---

# Synchronizing Interrupt Code


The following factors complicate driver code that handles hardware interrupts on multiprocessor systems:

-   Each time a device interrupts, it provides interrupt-specific information that is volatile because it can be overwritten the next time that the device interrupts.

-   Devices interrupt at relatively high IRQLs and their interrupt service routines (ISRs) can interrupt the execution of other driver code.

-   For DIRQL interrupts, the ISR must run at DIRQL while holding a driver-supplied spin lock, so that the ISR can prevent additional interrupts while it saves volatile information. The DIRQL prevents interruption by the current processor, and the spin lock prevents interruption by another processor.

-   The ISR must run quickly because the device cannot interrupt while the ISR is executing. Long ISR execution times can slow the system or possibly cause data loss.

-   Both the ISR and the deferred procedure call (DPC) routine must typically access a storage area in which the ISR stores the device's volatile data. These routines must synchronize with each other so that they do not access the storage area at the same time.

Because of all of these factors, you must use the following rules when writing driver code that handles interrupts:

-   Only the [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function accesses volatile interrupt data, such as device registers that contain interrupt information.

    The [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function should move the volatile data to a driver-defined interrupt data buffer that the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function, [*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem) callback function, or multiple [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback functions can access.

    If your driver provides [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem) callback functions for its interrupt objects, the best place to store interrupt data is the interrupt object's [context space](framework-object-context-space.md). The interrupt object's callback functions can access the object's context space by using the object handle that they receive.

    If your driver provides multiple [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback functions for each [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function, you might store interrupt data in each DPC object's context space.

-   All driver code that accesses the interrupt data buffer must be synchronized so that only one routine accesses the data at a time.

    For DIRQL interrupt objects, the [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function accesses this data buffer at IRQL = DIRQL while holding the interrupt object's driver-supplied spin lock. Therefore, all routines that access the buffer must also run at DIRQL while holding the spin lock. (Typically, the interrupt's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback function is the only other routine that must access the buffer.)

    All routines that access an interrupt data buffer, except for the [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function, must do one of the following:

    -   Call [**WdfInterruptSynchronize**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsynchronize) to schedule an [*EvtInterruptSynchronize*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_synchronize) callback function that accesses the interrupt data buffer.
    -   Place code that accesses the interrupt data buffer between calls to [**WdfInterruptAcquireLock**](/previous-versions/ff547340(v=vs.85)) and [**WdfInterruptReleaseLock**](/previous-versions/ff547376(v=vs.85)).

    Both of these techniques allow the [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) function to access interrupt data at DIRQL while holding the interrupt's spin lock. The DIRQL prevents interruption by the current processor, and the spin lock prevents interruption by another processor.

    If your device supports multiple interrupt vectors or messages, and if you want to synchronize your driver's handling of these interrupts, you can assign a single spin lock to multiple DIRQL interrupt objects. The framework determines the highest DIRQL of the set of interrupts, and it always acquires the spin lock at that DIRQL so that the synchronized code cannot be interrupted by any interrupt vectors or messages in the set.

    For [passive-level interrupt objects](supporting-passive-level-interrupts.md), the framework acquires the passive-level interrupt lock before calling the driver's [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function at IRQL = PASSIVE\_LEVEL. As a result, all routines that access the buffer must either acquire the interrupt lock or internally synchronize buffer access. Typically, the interrupt's [*EvtInterruptWorkItem*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_workitem) callback function is the only other routine that accesses the buffer. For information about acquiring the interrupt lock from an *EvtInterruptWorkItem* callback function, see the Remarks section of that page.

    You can also synchronize your driver's handling of multiple interrupt vectors by assigning a single wait lock to multiple passive-level interrupt objects.

-   If some of your code that handles DIRQL interrupts must run at IRQL = PASSIVE\_LEVEL, your [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback function can create one or more [work items](using-framework-work-items.md) so that the code will run as [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback functions.

    Alternatively, in KMDF versions 1.11 and later, the driver can request an interrupt work item by calling [**WdfInterruptQueueWorkItemForIsr**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueueworkitemforisr). (Recall that a driver's [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function can call **WdfInterruptQueueWorkItemForIsr** or [**WdfInterruptQueueDpcForIsr**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptqueuedpcforisr), but not both.)

-   If it is important to synchronize a driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) and [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback functions with each other and with other callback functions that are associated with a device, your driver can set the **AutomaticSerialization** member to **TRUE** in the interrupt's [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure and the DPC object's [**WDF\_DPC\_CONFIG**](/windows-hardware/drivers/ddi/wdfdpc/ns-wdfdpc-_wdf_dpc_config) structure. Alternatively, the driver can use [framework spin locks](using-framework-locks.md#framework-spin-locks). (Setting the **AutomaticSerialization** member to **TRUE** does not synchronize an [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function with other callback functions. Use [**WdfInterruptSynchronize**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptsynchronize) or [**WdfInterruptAcquireLock**](/previous-versions/ff547340(v=vs.85)) to synchronize an *EvtInterruptIsr* callback function, as described previously in this topic.)

For more information about synchronizing driver routines, see [Synchronization Techniques for Framework-Based Drivers](./using-automatic-synchronization.md).

 

