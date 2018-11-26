---
title: Accessing Shared State Information
description: Accessing Shared State Information
ms.assetid: f3e5ac07-cab1-4f66-90e4-88b2e28079a5
keywords: ["critical section routines WDK kernel", "timer counters WDK kernel", "shared state information WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Accessing Shared State Information





Use the following general guidelines for designing and writing [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines that maintain state:

-   To access data that an ISR also accesses, a driver routine must call a *SynchCritSection* routine. Non-critical section code can be interrupted. Remember that it is not sufficient to simply acquire a spin lock to protect data that ISRs also access, because ISRs execute at DIRQL and acquiring a spin lock ([**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)) only raises IRQL to DISPATCH\_LEVEL, which allows an interrupt to invoke the ISR on the current processor.

-   Give each *SynchCritSection* routine that maintains state information responsibility for a discrete set of state variables. That is, avoid writing *SynchCritSection* routines that maintain overlapping state information.

    This prevents contention, and possibly race conditions, between *SynchCritSection* routines (and the ISR) trying to access the same state concurrently.

    This also ensures that each *SynchCritSection* routine returns control as quickly as possible because one *SynchCritSection* routine never has to wait for another that updates some of the same state information to return control.

-   Avoid writing a single, large, general-purpose *SynchCritSection* routine that does more testing of conditions to determine what to do than actually doing useful work. On the other hand, avoid having many *SynchCritSection* routines that never execute a conditional statement because each updates only a single byte of state information.

-   Every *SynchCritSection* routine must return control as quickly as possible, because running any *SynchCritSection* routine prevents the driver's ISR from executing.

Following is a technique for maintaining a timer counter in a device extension. Assume the driver uses the counter to determine if an I/O operation has timed out. Also assume the driver does not overlap I/O operations.

-   The driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine initializes the timer counter to some initial value for each I/O request. The driver then adds a second to its device time-out value, in case its [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine has just returned control.

-   The driver's ISR must set this timer counter to minus one.

-   The driver's [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine is called once per second to read the time counter and determine whether the ISR has already set it to minus one. If not, the *IoTimer* routine decrements the counter by using [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a SynchCritSection\_1 routine.

    If the counter goes to zero, indicating that the request timed out, the SynchCritSection\_1 routine calls a SynchCritSection\_2 routine to program a device reset operation. If the counter is minus one, the [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine simply returns.

-   If the driver's [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine must reprogram the device to begin a partial-transfer operation, it must reinitialize the timer counter as the [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine did.

    The [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine also must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call the SynchCritSection\_2 routine, or possibly a SynchCritSection\_3 routine, to program the device for another transfer operation.

In this scenario, the driver has more than one *SynchCritSection* routine, each with discrete, specific responsibilities; one to maintain its timer counter, and one or more others to program the device. Each *SynchCritSection* routine can return control quickly because it performs a single, discrete task.

Note that the driver has a single SynchCritSection\_1 routine which, along with the driver's ISR, maintains the state to the timer counter. Thus, there is no contention for access to the timer counter among several *SynchCritSection* routines and the ISR.

 

 




