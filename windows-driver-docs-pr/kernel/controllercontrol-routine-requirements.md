---
title: ControllerControl Routine Requirements
description: ControllerControl Routine Requirements
ms.assetid: b311c0b0-f7b1-4276-a165-5c658657b198
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, requirements"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# ControllerControl Routine Requirements





As its name implies, a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine is associated with a controller object. When the *ControllerControl* routine executes, the hardware represented by the controller object is free and the controller extension generally is not being accessed by another driver routine unless the controller extension contains context that is shared with the driver's ISR.

Usually, a *ControllerControl* routine does at least the following:

1.  Updates or initializes whatever context the driver maintains in the device extension of the target device object and in the controller extension

    If the driver uses DMA, its *ControllerControl* routine usually is responsible for determining whether a given transfer request must be split up into partial transfers due to any system-imposed or device-imposed limitations on the size of each DMA transfer. In these circumstances, the *ControllerControl* routine also is responsible for calling [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) if the driver has an *AdapterControl* routine.

    If the driver uses PIO, its *ControllerControl* routine also is responsible for [splitting transfer requests](splitting-dma-transfer-requests.md), if its hardware requires it, into partial-transfer ranges and for calling [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) with the MDL at **Irp-&gt;MdlAddress**.

2.  Programs its hardware for the requested I/O operation

    If the device or controller extension can be accessed from the ISR, the *ControllerControl* routine must use a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that is invoked by calling [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302). For more information, see [Using Critical Sections](using-critical-sections.md).

If the driver has a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine, its *ControllerControl* routine also must check the **Irp-&gt;Cancel** field to determine whether the current IRP should be canceled, and do either of the following:

If **Irp-&gt;Cancel** is set to **TRUE**, the *ControllerControl* routine must do the following:

1.  Set STATUS\_CANCELLED for **Status** and zero for **Information** in the I/O status block of the IRP.

2.  Call [**IoFreeController**](https://msdn.microsoft.com/library/windows/hardware/ff549104) to release the controller object so the next device operation can be started promptly.

3.  Call [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) or dequeue the next IRP if the driver manages its own queuing.

4.  Complete the canceled IRP with [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) and return control.

If **Irp-&gt;Cancel** is not set to **TRUE**, the *ControllerControl* routine instead must do the following:

1.  Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to reset the *Cancel* routine entry point for the IRP to **NULL**. Acquire the cancel spin lock for this call if the driver uses the I/O manager-supplied device queue in the device object.

2.  Program the hardware for the requested I/O operation, using a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that is invoked by calling [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302). For more information, see [Using Critical Sections](using-critical-sections.md)

For more information about handling cancelable IRPs, see [Canceling IRPs](canceling-irps.md).

For most interrupt-driven I/O operations except overlapped operations on different devices attached to the physical controller/adapter, a *ControllerControl* routine should return **KeepObject** because the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine completes the operation and the IRP.

As soon as the I/O operation(s) to satisfy the current request are done, the routine that will complete the IRP should call **IoFreeController** and **IoStartNextPacket** so that the next request can be processed as quickly as possible.

If the *ControllerControl* routine itself completes an IRP or if it can set up an operation, such as a disk seek, for one target device object (disk) that could be overlapped with an operation for another device object, the *ControllerControl* routine should return **DeallocateObject**.

 

 




