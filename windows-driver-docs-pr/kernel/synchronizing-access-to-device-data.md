---
title: Synchronizing Access to Device Data
description: Synchronizing Access to Device Data
ms.assetid: aaed8006-6773-4d20-b3a0-b48131f728c6
keywords: ["interrupt service routines WDK kernel , synchronization", "ISRs WDK kernel , synchronization", "interrupt objects WDK kernel , synchronization", "synchronization WDK kernel , interrupts", "single interrupt vectors WDK kernel", "critical section routines WDK kernel", "interrupt spin locks WDK kernel", "spin locks WDK kernel", "synchronization WDK kernel , device data access", "SynchCritSection", "SynchronizeIrql", "SpinLock parameter"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Synchronizing Access to Device Data





Typically, a driver's [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) or [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routines (ISRs) must share access to driver data and hardware resources with other driver routines. Since ISRs execute in an interrupt context at an elevated IRQL, and since a system might have multiple processors, it is important to synchronize access to shared data and resources so that each routine can be guaranteed to temporarily have exclusive access to this shared information, without interruption.

The system supports this synchronization by executing the ISR within an *interrupt critical section*. An interrupt has an assigned spin lock, the *interrupt spin lock*, and IRQL, the *interrupt synchronization IRQL*. The system guarantees this code executing within the critical section exclusive access to shared information, by raising the processor's IRQL to the interrupt synchronization IRQL and acquiring the interrupt spin lock before executing the code. The system always enters the interrupt's critical section before executing its ISR. Different interrupts can share the same critical section by sharing their interrupt spin lock and synchronization IRQL.

Drivers can implement code that runs in the interrupt's critical section by supplying a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine. When the driver uses [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call the *SynchCritSection* routine, the system automatically enters the critical section for the interrupt specified by the *Interrupt* parameter.

Raising the processor's IRQL to the interrupt's synchronization IRQL prevents the current processor from being interrupted, except by an interrupt with a higher synchronization IRQL. Acquiring a spin lock prevents other processors from executing any critical section code associated with that spin lock.

The system assigns the interrupt spin lock and synchronization IRQL for the interrupt when the driver calls [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378). In most instances, the driver can allow the system to determine both values:

-   If the driver uses the CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED versions of **IoConnectInterruptEx**, and specifies a **NULL** spin lock, the system will allocate a spin lock to be shared across all of the device's interrupts. The system also determines the value for the synchronization IRQL (drivers can optionally specify a higher value). All of the driver's interrupts will share the same critical section.

-   If the driver uses the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx** and has only a single interrupt vector, the driver can specify a **NULL** spin lock. The system will allocate a spin lock for only that particular interrupt, which will have its own critical section.

A driver must allocate its own spin lock only when using the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx** and when it has multiple interrupt vectors that must share the same critical section. A driver can specify its own spin lock and synchronization IRQL by using the **SpinLock** and **SynchronizeIrql** members of **IO\_CONNECT\_INTERRUPT\_PARAMETERS**. For more information, see [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541).

For information about writing and entering critical sections, see [Using Critical Sections](using-critical-sections.md).

 

 




