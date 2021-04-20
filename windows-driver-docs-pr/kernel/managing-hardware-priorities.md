---
title: Managing Hardware Priorities
description: Managing Hardware Priorities
keywords: ["prioritizing criteria WDK kernel", "hardware priorities WDK kernel", "IRQL levels WDK kernel", "PASSIVE_LEVEL WDK", "APC_LEVEL WDK", "DISPATCH_LEVEL WDK", "DIRQL WDK", "interrupt service routines WDK kernel , hardware priorities", "ISRs WDK kernel , hardware priorities"]
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Managing Hardware Priorities





The IRQL at which a driver routine executes determines which kernel-mode driver support routines it can call. For example, some driver support routines require that the caller be running at IRQL = DISPATCH\_LEVEL. Others cannot be called safely if the caller is running at any IRQL higher than PASSIVE\_LEVEL.

Following is a list of IRQLs at which the most commonly implemented standard driver routines are called. The IRQLs are listed from lowest to highest priority.

<a href="" id="passive-level"></a>**PASSIVE\_LEVEL**  
**Interrupts Masked Off** — None.

**Driver Routines Called at** PASSIVE\_LEVEL — [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device), [*Reinitialize*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize), [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routines, most dispatch routines, driver-created threads, worker-thread callbacks.

<a href="" id="apc-level"></a>**APC\_LEVEL**  
**Interrupts Masked Off** — APC\_LEVEL interrupts are masked off.

**Driver Routines Called at** APC\_LEVEL — Some dispatch routines (see [Dispatch Routines and IRQLs](dispatch-routines-and-irqls.md)).

<a href="" id="dispatch-level"></a>**DISPATCH\_LEVEL**  
**Interrupts Masked Off** — DISPATCH\_LEVEL and APC\_LEVEL interrupts are masked off. Device, clock, and power failure interrupts can occur.

**Driver Routines Called at** DISPATCH\_LEVEL — [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio), [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control), [*AdapterListControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_list_control), [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049), [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine), [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) (while holding the cancel spin lock), [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine), [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983), [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routines.

<a href="" id="dirql"></a>**DIRQL**  
**Interrupts Masked Off** — All interrupts at IRQL&lt;= DIRQL of driver's interrupt object. Device interrupts with a higher DIRQL value can occur, along with clock and power failure interrupts.

Driver Routines Called at DIRQL — [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine), [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routines.

The only difference between APC\_LEVEL and PASSIVE\_LEVEL is that a process executing at APC\_LEVEL cannot get APC interrupts. But both IRQLs imply a thread context and both imply that the code can be paged out.

Lowest-level drivers process IRPs while running at one of three IRQLs:

-   PASSIVE\_LEVEL, with no interrupts masked off on the processor, in the driver's Dispatch routine(s)

    **DriverEntry**, *AddDevice*, *Reinitialize*, and *Unload* routines also are run at PASSIVE\_LEVEL, as are any driver-created system threads.

-   DISPATCH\_LEVEL, with DISPATCH\_LEVEL and APC\_LEVEL interrupts masked off on the processor, in the *StartIo* routine

    *AdapterControl*, *AdapterListControl*, *ControllerControl*, *IoTimer*, *Cancel* (while it holds the cancel spin lock), and *CustomTimerDpc* routines also are run at DISPATCH\_LEVEL, as are *DpcForIsr* and *CustomDpc* routines.

-   Device IRQL (DIRQL), with all interrupts at less than or equal to the *SynchronizeIrql* of the driver's interrupt object(s) masked off on the processor, in the ISR and *SynchCritSection* routines

Most higher-level drivers process IRPs while running at either of two IRQLs:

-   PASSIVE\_LEVEL, with no interrupts masked off on the processor, in the driver's dispatch routines

    **DriverEntry**, *Reinitialize*, *AddDevice*, and *Unload* routines also are run at PASSIVE\_LEVEL, as are any driver-created system threads or worker-thread callback routines or file system drivers.

-   DISPATCH\_LEVEL, with DISPATCH\_LEVEL and APC\_LEVEL interrupts masked off on the processor, in the driver's *IoCompletion* routine(s)

    *IoTimer*, *Cancel*, and *CustomTimerDpc* routines also are run at DISPATCH\_LEVEL.

In some circumstances, intermediate and lowest-level drivers of mass-storage devices are called at IRQL APC\_LEVEL. In particular, this can occur at a page fault for which a file system driver sends an [**IRP\_MJ\_READ**](./irp-mj-read.md) request to lower drivers.

Most standard driver routines are run at an IRQL that allows them simply to call the appropriate support routines. For example, a device driver must call [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) while running at IRQL DISPATCH\_LEVEL. Since most device drivers call these routines from a *StartIo* routine, usually they are running at DISPATCH\_LEVEL already.

Note that a device driver that has no *StartIo* routine because it sets up and manages its own queues of IRPs is not necessarily running at DISPATCH\_LEVEL IRQL when it should call **AllocateAdapterChannel**. Such a driver must nest its call to **AllocateAdapterChannel** between calls to [**KeRaiseIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql) and [**KeLowerIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql) so that it runs at the required IRQL when it calls **AllocateAdapterChannel** and restores the original IRQL when the calling routine regains control.

When calling driver support routines, be aware of the following.

- Calling [**KeRaiseIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql) with an input *NewIrql* value that is less than the current IRQL causes a fatal error. Calling [**KeLowerIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql) except to restore the original IRQL (that is, after a call to **KeRaiseIrql**) also causes a fatal error.

- While running at IRQL &gt;= DISPATCH\_LEVEL, calling [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) or [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) for kernel-defined dispatcher objects to wait for a nonzero interval causes a fatal error.

- The only driver routines that can safely wait for events, semaphores, mutexes, or timers to be set to the signaled state are those that run in a nonarbitrary thread context at IRQL PASSIVE\_LEVEL, such as driver-created threads, the **DriverEntry** and *Reinitialize* routines, or dispatch routines for inherently synchronous I/O operations (such as most device I/O control requests).

- Even while running at IRQL PASSIVE\_LEVEL, pageable driver code must not call [**KeSetEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent), [**KeReleaseSemaphore**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasesemaphore), or [**KeReleaseMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasemutex) with the input *Wait* parameter set to **TRUE**. Such a call can cause a fatal page fault.

- Any routine that is running at greater than IRQL APC\_LEVEL can neither allocate memory from paged pool nor access memory in paged pool safely. If a routine running at IRQL greater than APC\_LEVEL causes a page fault, it is a fatal error.

- A driver must be running at IRQL DISPATCH\_LEVEL when it calls [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel) and [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel).

  A driver can be running at IRQL &lt;= DISPATCH\_LEVEL when it calls **KeAcquireSpinLock** but it must release that spin lock by calling **KeReleaseSpinLock**. In other words, it is a programming error to release a spin lock acquired with **KeAcquireSpinLock** by calling **KeReleaseSpinLockFromDpcLevel**.

  A driver must not call **KeAcquireSpinLockAtDpcLevel**, **KeReleaseSpinLockFromDpcLevel**, **KeAcquireSpinLock**, or **KeReleaseSpinLock** while running at IRQL &gt; DISPATCH\_LEVEL.

- Calling a support routine that uses a spin lock, such as an **ExInterlocked<em>Xxx</em>** routine, raises IRQL on the current processor either to DISPATCH\_LEVEL or to DIRQL if the caller is not already running at a raised IRQL.

- Driver code that runs at IRQL &gt; PASSIVE\_LEVEL should execute as quickly as possible. The higher the IRQL at which a routine runs, the more important it is for good overall performance to tune that routine to execute as quickly as possible. For example, any driver that calls **KeRaiseIrql** should make the reciprocal call to **KeLowerIrql** as soon as it can.

For more information about determining priorities, see the [Scheduling, Thread Context, and IRQL](https://go.microsoft.com/fwlink/p/?linkid=59757) white paper.

 

