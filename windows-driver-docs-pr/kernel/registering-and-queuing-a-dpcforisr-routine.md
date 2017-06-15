---
title: Registering and Queuing a DpcForIsr Routine
author: windows-driver-content
description: Registering and Queuing a DpcForIsr Routine
MS-HAID:
- 'Intrupts\_ff19f7ee-f65a-4b1f-a3e8-ca33bd3d9649.xml'
- 'kernel.registering\_and\_queuing\_a\_dpcforisr\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 32253573-842e-40bc-9616-8d1ccd7afa29
keywords: ["DpcForIsr", "registering DpcForIsr routine", "queuing DpcForIsr routine"]
---

# Registering and Queuing a DpcForIsr Routine


## <a href="" id="ddk-registering-and-queuing-a-dpcforisr-routine-kg"></a>


A driver registers a [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine for a device object by calling [**IoInitializeDpcRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549307) after it has created the device object. The driver can make this call from its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, or from [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) code that handles [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) requests.

To queue the *DpcForIsr* routine for execution, the driver's ISR calls [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657) just before it returns. The following figure illustrates calls to these routines.

![diagram illustrating using a dpc object for a dpcforisr routine](images/3dpcisr.png)

As the previous figure shows, calling **IoInitializeDpcRequest** associates a DPC object with a driver-supplied *DpcForIsr* routine and a driver-created device object. The I/O manager allocates memory for the DPC object and calls [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) on the driver's behalf.

When the ISR is called to handle a device interrupt at DIRQL, it should return control to the system as soon as possible for better overall system and driver performance. Usually, an ISR merely clears the interrupt, gathers whatever context information the *DpcForIsr* routine needs to complete the operation that caused the interrupt, calls [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657), and returns.

When the ISR calls **IoRequestDpc**, it passes a pointer to the device object, a pointer to the *DeviceObject*-&gt;**CurrentIrp**, and a pointer to a driver-determined context. The I/O manager calls [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185) on the driver's behalf, which queues the DPC object. When IRQL falls below DISPATCH\_LEVEL on a processor, the kernel dequeues the DPC object and runs the driver's *DpcForIsr* routine on that processor at IRQL DISPATCH\_LEVEL.

The *DpcForIsr* routine is responsible for doing whatever is necessary to complete the I/O requested in the current IRP. On entry, the routine receives a pointer to the DPC object, along with pointers to the device object, IRP, and context area, which were passed in the ISR's call to **IoRequestDpc**. The context area must be in resident memory, and is usually in the device extension. Alternatively, it can be in nonpaged pool allocated by the driver, or in a controller extension if the driver uses a [controller object](using-controller-objects.md).

Because ISR and *DpcForIsr* routines can run concurrently on SMP machines, you must follow these guidelines:

-   The ISR must call **IoRequestDpc** just before it returns control. Otherwise, the *DpcForIsr* routine might be run on another processor before the ISR has finished setting up the context area for the *DpcForIsr* routine.

-   The *DpcForIsr* routine and any other driver routine that shares a context area with the ISR must call [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302), specifying a driver-supplied [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that accesses the shared context area in a multiprocessor-safe manner.

-   If a driver uses the device extension to maintain context about its device I/O operations, the *DpcForIsr* routine should never call [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) for the input device object (nor dequeue an IRP for the input device object, if the driver manages its own IRP queuing) until just before it calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

    Otherwise, the driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) (or queue-management routines) might start another I/O operation that overwrites the shared context area before the *DpcForIsr* routine can complete the current operation. This is because the ISR can be called again if the device interrupts while or before the *DpcForIsr* routine executes (assuming interrupts are still enabled).

Even on a uniprocessor machine, the ISR could be called again if the device interrupts while or before the *DpcForIsr* routine is run. If this occurs, the *DpcForIsr* routine is run only once. In other words, there is no one-to-one correspondence between an ISR's calls to **IoRequestDpc** and instantiations of the *DpcForIsr* routine if a driver overlaps I/O operations for its target device objects.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20and%20Queuing%20a%20DpcForIsr%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


