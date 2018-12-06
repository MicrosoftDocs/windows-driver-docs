---
title: Writing an ISR
description: Writing an ISR
ms.assetid: d696d683-e010-4a5c-ba2d-f536ab5f38b2
keywords: ["interrupt service routines WDK kernel , writing", "ISRs WDK kernel , writing", "writing ISRs", "interrupt objects WDK kernel , writing ISRs", "I/O WDK kernel , interrupts"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing an ISR





Drivers for physical devices that generate interrupts must have at least one interrupt service routine (ISR). The ISR must do whatever is appropriate to the device to dismiss the interrupt, possibly including stopping the device from interrupting. Then, it should do only what is necessary to save state and queue a DPC to finish the I/O operation at a lower priority (IRQL) than that at which the ISR executes.

A driver's ISR executes in an interrupt context, at some system-assigned [*DIRQL*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interrupt-request-level--dirql-), as specified by the *SynchronizeIrql* parameter to [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378).

ISRs are interruptible. Another device with a higher system-assigned DIRQL can interrupt, or a high-IRQL system interrupt can occur, at any time.

Before the system calls an ISR, it acquires the interrupt's spin lock so the ISR cannot simultaneously execute on another processor. After the ISR returns, the system releases the spin lock.

Because an ISR runs at a relatively high IRQL, which masks off interrupts with an equivalent or lower IRQL on the current processor, it should return control as quickly as possible. Additionally, running an ISR at DIRQL restricts the set of support routines the ISR can call. For more information, see [Managing Hardware Priorities](managing-hardware-priorities.md).

Typically, an ISR performs the following general steps:

-   If the device that caused the interrupt is not one supported by the ISR, the ISR immediately returns **FALSE**.

-   Otherwise, the ISR clears the interrupt if necessary, saving whatever device context is necessary, and queues a DPC to complete the I/O operation at a lower IRQL. See [DPC Objects and DPCs](dpc-objects-and-dpcs.md) for more information. The ISR must then return **TRUE**.

Specifically, in drivers that do not overlap device I/O operations, the ISR should do the following:

1.  Determine whether the interrupt is spurious. If so, return **FALSE** immediately so the ISR of the device that interrupted will be called promptly. Otherwise, continue interrupt processing.

2.  Stop the device from interrupting, if necessary.

3.  Gather whatever context information the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) (or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972)) routine will need to complete I/O processing for the current operation.

4.  Store this context in an area accessible to the *DpcForIsr* or *CustomDpc* routine, usually in the device extension of the target device object for which processing the current I/O request caused the interrupt.

    If a driver overlaps I/O operations, the context information must include a count of outstanding requests the DPC routine is required to complete, along with whatever context the DPC routine needs to complete each request. If the ISR is called to handle another interrupt before the DPC has run, it must not overwrite the saved context for a request that has not yet been completed by the DPC.

5.  If the driver has a *DpcForIsr* routine, call [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657) with pointers to the current IRP, the target device object, and the saved context. **IoRequestDpc** queues the *DpcForIsr* routine to be run as soon as IRQL falls below DISPATCH\_LEVEL on a processor.

    If the driver has a *CustomDpc* routine, call [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185) with a pointer to the DPC object (associated with the *CustomDpc* routine) and pointer(s) to any saved context the *CustomDpc* routine will need to complete the operation. Usually, the ISR also passes pointers to the current IRP and the target device object. The *CustomDpc* routine is run as soon as IRQL falls below DISPATCH\_LEVEL on a processor.

6.  Return **TRUE** to indicate that its device generated the interrupt.

In general, an ISR does no actual I/O processing to satisfy an IRP. Instead, it stops its device from interrupting, sets up necessary state information, and queues the driver's *DpcForIsr* or *CustomDpc* to do whatever I/O processing is necessary to satisfy the current request that caused the device to interrupt.

An ISR must run at DIRQL for the shortest possible interval. Following this guideline increases I/O throughput for every device in the machine because running at DIRQL masks off all interrupts to which the system has assigned a lesser or equal IRQL value.

The *SynchronizeIrql* of the driver's interrupt objects, specified when the driver called **IoConnectInterrupt**, determines the DIRQL at which the driver's ISR executes. For more information, see [Synchronizing Access to Device Data](synchronizing-access-to-device-data.md).

 

 




