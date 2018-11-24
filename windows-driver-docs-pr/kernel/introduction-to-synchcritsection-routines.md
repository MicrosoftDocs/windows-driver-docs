---
title: Introduction to SynchCritSection Routines
description: Introduction to SynchCritSection Routines
ms.assetid: 747f314a-9c7c-427f-bc23-4c6869853852
keywords: ["SynchCritSection", "critical section routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to SynchCritSection Routines





*Critical sections* are sections of code that require exclusive access to hardware resources or driver data. That is, the code must not be interrupted by other code that can reference the same resources or data, and the resources or data must not be referenced by more than one processor at a time.

Critical sections should be confined to ISRs and [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines. The system calls these routines only after raising the current processor's IRQL to the device's [*DIRQL*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interrupt-request-level--dirql-) value and acquiring a spin lock. After a *SynchCritSection* routine returns, the system releases the spin lock and lowers the processor's IRQL.

Raising the processor's IRQL to the device's DIRQL value prevents the current processor from being interrupted, except by a higher-priority device. Acquiring a spin lock prevents other processors from executing any critical section code associated with that spin lock. (This spin lock is sometimes called an *interrupt spin lock*.)

A device driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) and [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routines frequently must access some of the same [hardware resources](hardware-resources.md) (such as device registers or other bus-relative memory) or driver-maintained data as the driver's ISR. Depending on the driver's device or design, its dispatch, [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504), [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049), or timer routines also might access hardware resources or driver-maintained data.

To call any non-ISR critical section, a driver must use the [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) routine. This routine accepts the address of a *SynchCritSection* routine as input, along with driver-defined context information and an interrupt object pointer. The system uses the interrupt object pointer to determine the DIRQL and spin lock to use with the *SynchCritSection* routine. (The driver previously supplied these values, using the [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) function's *SpinLock* and *SynchronizeIrql* parameters.)

 

 




