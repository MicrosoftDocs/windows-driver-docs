---
title: Accessing Shared State Information
description: Accessing Shared State Information
keywords: ["critical section routines WDK kernel", "timer counters WDK kernel", "shared state information WDK kernel"]
ms.date: 07/17/2025
ms.topic: concept-article
---

# Accessing Shared State Information

Use the following general guidelines when designing and writing [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routines that maintain state information:

- To access data that an ISR also accesses, a driver routine must call a *SynchCritSection* routine. Noncritical section code can be interrupted. Remember that it's not sufficient to just acquire a spin lock to protect data that ISRs also access, because ISRs execute at DIRQL and acquiring a spin lock ([**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock)) only raises IRQL to DISPATCH_LEVEL, which allows an interrupt to invoke the ISR on the current processor.

- Give each *SynchCritSection* routine that maintains state information responsibility for a discrete set of state variables. That is, avoid writing *SynchCritSection* routines that maintain overlapping state information.

  This approach prevents contention, and possibly race conditions, between *SynchCritSection* routines (and the ISR) trying to access the same state concurrently.

  This approach also ensures that each *SynchCritSection* routine returns control as quickly as possible. That is, one *SynchCritSection* routine never has to wait for another that updates some of the same state information to return control.

- Avoid writing a single, large, general-purpose *SynchCritSection* routine that does more testing of conditions to determine what to do than actually doing useful work. On the other hand, avoid having many *SynchCritSection* routines that never execute a conditional statement because each updates only a single byte of state information.

- Ensure every *SynchCritSection* routine returns control as quickly as possible, because running any *SynchCritSection* routine prevents the driver's ISR from executing.

The following example shows a technique for maintaining a timer counter in a device extension. Assume the driver uses the counter to determine if an I/O operation times out. Also assume the driver doesn't overlap I/O operations.

1. The driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine initializes the timer counter to some initial value for each I/O request. The driver then adds a second to its device timeout value, in case its [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine just returned control.

1. The driver's ISR sets this timer counter to minus one.

1. The driver's [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine is called once per second to read the time counter and determine whether the ISR already set it to minus one. If not, the *IoTimer* routine decrements the counter by using [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a SynchCritSection_1 routine.

  If the counter goes to zero, indicating that the request timed out, the SynchCritSection_1 routine calls a SynchCritSection_2 routine to program a device reset operation. If the counter is minus one, the [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine simply returns.

1. If the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine must reprogram the device to begin a partial-transfer operation, it must reinitialize the timer counter as the [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine did.

  The [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine also must use [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call the SynchCritSection_2 routine, or possibly a SynchCritSection_3 routine, to program the device for another transfer operation.

In this scenario, the driver has more than one *SynchCritSection* routine, each with discrete, specific responsibilities: one to maintain its timer counter, and one or more others to program the device. Each *SynchCritSection* routine returns control quickly because it performs a single, discrete task.

The driver has a single SynchCritSection_1 routine which, along with the driver's ISR, maintains the state to the timer counter. Thus, there's no contention for access to the timer counter among several *SynchCritSection* routines and the ISR.
