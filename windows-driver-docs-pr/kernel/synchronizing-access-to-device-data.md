---
title: Synchronizing Access to Device Data
author: windows-driver-content
description: Synchronizing Access to Device Data
ms.assetid: aaed8006-6773-4d20-b3a0-b48131f728c6
keywords: ["interrupt service routines WDK kernel , synchronization", "ISRs WDK kernel , synchronization", "interrupt objects WDK kernel , synchronization", "synchronization WDK kernel , interrupts", "single interrupt vectors WDK kernel", "critical section routines WDK kernel", "interrupt spin locks WDK kernel", "spin locks WDK kernel", "synchronization WDK kernel , device data access", "SynchCritSection", "SynchronizeIrql", "SpinLock parameter"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Synchronizing Access to Device Data


## <a href="" id="ddk-synchronizing-access-to-device-data-kg"></a>


Typically, a driver's [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) or [*InterruptMessageService*](https://msdn.microsoft.com/library/windows/hardware/ff547940) routines (ISRs) must share access to driver data and hardware resources with other driver routines. Since ISRs execute in an interrupt context at an elevated IRQL, and since a system might have multiple processors, it is important to synchronize access to shared data and resources so that each routine can be guaranteed to temporarily have exclusive access to this shared information, without interruption.

The system supports this synchronization by executing the ISR within an *interrupt critical section*. An interrupt has an assigned spin lock, the *interrupt spin lock*, and IRQL, the *interrupt synchronization IRQL*. The system guarantees this code executing within the critical section exclusive access to shared information, by raising the processor's IRQL to the interrupt synchronization IRQL and acquiring the interrupt spin lock before executing the code. The system always enters the interrupt's critical section before executing its ISR. Different interrupts can share the same critical section by sharing their interrupt spin lock and synchronization IRQL.

Drivers can implement code that runs in the interrupt's critical section by supplying a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine. When the driver uses [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call the *SynchCritSection* routine, the system automatically enters the critical section for the interrupt specified by the *Interrupt* parameter.

Raising the processor's IRQL to the interrupt's synchronization IRQL prevents the current processor from being interrupted, except by an interrupt with a higher synchronization IRQL. Acquiring a spin lock prevents other processors from executing any critical section code associated with that spin lock.

The system assigns the interrupt spin lock and synchronization IRQL for the interrupt when the driver calls [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378). In most instances, the driver can allow the system to determine both values:

-   If the driver uses the CONNECT\_LINE\_BASED or CONNECT\_MESSAGE\_BASED versions of **IoConnectInterruptEx**, and specifies a **NULL** spin lock, the system will allocate a spin lock to be shared across all of the device's interrupts. The system also determines the value for the synchronization IRQL (drivers can optionally specify a higher value). All of the driver's interrupts will share the same critical section.

-   If the driver uses the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx** and has only a single interrupt vector, the driver can specify a **NULL** spin lock. The system will allocate a spin lock for only that particular interrupt, which will have its own critical section.

A driver must allocate its own spin lock only when using the CONNECT\_FULLY\_SPECIFIED version of **IoConnectInterruptEx** and when it has multiple interrupt vectors that must share the same critical section. A driver can specify its own spin lock and synchronization IRQL by using the **SpinLock** and **SynchronizeIrql** members of **IO\_CONNECT\_INTERRUPT\_PARAMETERS**. For more information, see [**IO\_CONNECT\_INTERRUPT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff550541).

For information about writing and entering critical sections, see [Using Critical Sections](using-critical-sections.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronizing%20Access%20to%20Device%20Data%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


