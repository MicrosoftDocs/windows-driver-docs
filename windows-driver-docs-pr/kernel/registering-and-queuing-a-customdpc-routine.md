---
title: Registering and Queuing a CustomDpc Routine
author: windows-driver-content
description: Registering and Queuing a CustomDpc Routine
MS-HAID:
- 'Intrupts\_8b881e3c-cf23-4bf3-b73e-b14feb2b16b6.xml'
- 'kernel.registering\_and\_queuing\_a\_customdpc\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7c35f8f8-a6dc-43b1-9120-701227d7b4c5
keywords: ["CustomDpc", "registering CustomDpc routine", "queuing CustomDpc routine"]
---

# Registering and Queuing a CustomDpc Routine


## <a href="" id="ddk-registering-and-queuing-a-customdpc-routine-kg"></a>


A driver registers a [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine for a device object by calling [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) after it has created the device object. The driver can make this call from its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, or from [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) code that handles [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) requests.

Just before the driver's ISR returns control, it can call [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185) to queue the *CustomDpc* routine for execution. The following figure illustrates calls to these routines.

![diagram illustrating using a dpc object for a customdpc routine](images/3cstmdpc.png)

As the previous figure shows, a driver that has a *CustomDpc* routine must provide the storage for a DPC object. Because the driver must pass a pointer to the DPC object from its ISR, the storage must be in resident, system-space memory. Most drivers with *CustomDpc* routines provide storage for their DPC objects in the device extension, but the storage can be in a controller extension if the driver uses a [controller object](using-controller-objects.md) or in nonpaged pool allocated by the driver.

When the driver calls **KeInitializeDpc**, it must pass the entry point for its *CustomDpc* routine, along with pointers to the driver-allocated storage for the DPC object and to a driver-defined context area, which is passed to the *CustomDpc* routine when it is called. Because the context area must be accessible at IRQL = DISPATCH\_LEVEL, it also must be in resident memory.

Unlike a *DpcForIsr* routine, a *CustomDpc* routine is not associated with a device object. Nevertheless, drivers typically include pointers to the target device object and current IRP in the context information supplied to the *CustomDpc* routine. Like a *DpcForIsr* routine, the *CustomDpc* routine uses this information to complete an interrupt-driven I/O operation at a lower IRQL than the ISR.

As the previous figure shows, the ISR passes pointers to the DPC object and to two additional parameters, which are driver-defined, to [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185). If all processors in the machine currently have code running at an IRQL greater than or equal to DISPATCH\_LEVEL, the DPC object is queued until the IRQL falls below DISPATCH\_LEVEL on a processor. Then, the kernel dequeues the DPC object and the driver's *CustomDpc* routine is run on the processor at IRQL DISPATCH\_LEVEL.

Only a single instantiation of any one DPC object can be queued at any given moment. Thus if an ISR calls **KeInsertQueueDpc** more than once with the same *Dpc* pointer before the driver's *CustomDpc* routine is run, the *CustomDpc* routine runs only once after IRQL falls below DISPATCH\_LEVEL on a processor.

A *CustomDpc* routine is responsible for doing whatever is necessary to complete the I/O operation that caused the interrupt.

The ISR and *CustomDpc* routines can be run concurrently on an SMP machine. Therefore, when writing *CustomDpc* routines, follow the guidelines set out in the previous section, [Registering and Queuing a DpcForIsr Routine](registering-and-queuing-a-dpcforisr-routine.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20and%20Queuing%20a%20CustomDpc%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


