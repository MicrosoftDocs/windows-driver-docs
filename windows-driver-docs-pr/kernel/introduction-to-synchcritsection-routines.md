---
title: Introduction to SynchCritSection Routines
author: windows-driver-content
description: Introduction to SynchCritSection Routines
ms.assetid: 747f314a-9c7c-427f-bc23-4c6869853852
keywords: ["SynchCritSection", "critical section routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to SynchCritSection Routines


## <a href="" id="ddk-introduction-to-synchcritsection-routines-kg"></a>


*Critical sections* are sections of code that require exclusive access to hardware resources or driver data. That is, the code must not be interrupted by other code that can reference the same resources or data, and the resources or data must not be referenced by more than one processor at a time.

Critical sections should be confined to ISRs and [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines. The system calls these routines only after raising the current processor's IRQL to the device's [*DIRQL*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-interrupt-request-level--dirql-) value and acquiring a spin lock. After a *SynchCritSection* routine returns, the system releases the spin lock and lowers the processor's IRQL.

Raising the processor's IRQL to the device's DIRQL value prevents the current processor from being interrupted, except by a higher-priority device. Acquiring a spin lock prevents other processors from executing any critical section code associated with that spin lock. (This spin lock is sometimes called an *interrupt spin lock*.)

A device driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) and [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routines frequently must access some of the same [hardware resources](hardware-resources.md) (such as device registers or other bus-relative memory) or driver-maintained data as the driver's ISR. Depending on the driver's device or design, its dispatch, [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504), [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049), or timer routines also might access hardware resources or driver-maintained data.

To call any non-ISR critical section, a driver must use the [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) routine. This routine accepts the address of a *SynchCritSection* routine as input, along with driver-defined context information and an interrupt object pointer. The system uses the interrupt object pointer to determine the DIRQL and spin lock to use with the *SynchCritSection* routine. (The driver previously supplied these values, using the [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) function's *SpinLock* and *SynchronizeIrql* parameters.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20SynchCritSection%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


