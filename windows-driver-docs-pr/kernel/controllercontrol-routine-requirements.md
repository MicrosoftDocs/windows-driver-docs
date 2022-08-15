---
title: ControllerControl Routine Requirements
description: ControllerControl Routine Requirements
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, requirements"]
ms.date: 07/21/2021
---

# ControllerControl Routine Requirements

As its name implies, a [*ControllerControl*](writing-controllercontrolroutines.md) routine is associated with a controller object. When the *ControllerControl* routine executes, the hardware represented by the controller object is free and the controller extension generally is not being accessed by another driver routine unless the controller extension contains context that is shared with the driver's ISR.

Usually, a *ControllerControl* routine does at least the following:

1. Updates or initializes whatever context the driver maintains in the device extension of the target device object and in the controller extension

    If the driver uses DMA, its *ControllerControl* routine usually is responsible for determining whether a given transfer request must be split up into partial transfers due to any system-imposed or device-imposed limitations on the size of each DMA transfer. In these circumstances, the *ControllerControl* routine also is responsible for calling [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) if the driver has an *AdapterControl* routine.

    If the driver uses PIO, its *ControllerControl* routine also is responsible for [splitting transfer requests](splitting-dma-transfer-requests.md), if its hardware requires it, into partial-transfer ranges and for calling [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) with the MDL at **Irp->MdlAddress**.

1. Programs its hardware for the requested I/O operation

    If the device or controller extension can be accessed from the ISR, the *ControllerControl* routine must use a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that is invoked by calling [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution). For more information, see [Using Critical Sections](using-critical-sections.md).

If the driver has a [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine, its *ControllerControl* routine also must check the **Irp->Cancel** field to determine whether the current IRP should be canceled, and do either of the following:

If **Irp->Cancel** is set to **TRUE**, the *ControllerControl* routine must do the following:

1. Set STATUS\_CANCELLED for **Status** and zero for **Information** in the I/O status block of the IRP.

1. Call [**IoFreeController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iofreecontroller) to release the controller object so the next device operation can be started promptly.

1. Call [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) or dequeue the next IRP if the driver manages its own queuing.

1. Complete the canceled IRP with [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) and return control.

If **Irp->Cancel** is not set to **TRUE**, the *ControllerControl* routine instead must do the following:

1. Call [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) to reset the *Cancel* routine entry point for the IRP to **NULL**. Acquire the cancel spin lock for this call if the driver uses the I/O manager-supplied device queue in the device object.

1. Program the hardware for the requested I/O operation, using a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that is invoked by calling [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution). For more information, see [Using Critical Sections](using-critical-sections.md)

For more information about handling cancelable IRPs, see [Canceling IRPs](canceling-irps.md).

For most interrupt-driven I/O operations except overlapped operations on different devices attached to the physical controller/adapter, a *ControllerControl* routine should return **KeepObject** because the [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine completes the operation and the IRP.

As soon as the I/O operation(s) to satisfy the current request are done, the routine that will complete the IRP should call **IoFreeController** and **IoStartNextPacket** so that the next request can be processed as quickly as possible.

If the *ControllerControl* routine itself completes an IRP or if it can set up an operation, such as a disk seek, for one target device object (disk) that could be overlapped with an operation for another device object, the *ControllerControl* routine should return **DeallocateObject**.
