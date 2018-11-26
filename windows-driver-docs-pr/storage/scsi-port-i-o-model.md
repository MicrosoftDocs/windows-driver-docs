---
title: SCSI Port I/O Model
description: SCSI Port I/O Model
ms.assetid: c79fdc99-30ae-4c4a-a130-2b8743bbff7f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Port I/O Model


## <span id="ddk_scsi_port_i_o_model_kg"></span><span id="DDK_SCSI_PORT_I_O_MODEL_KG"></span>


The SCSI Port driver communicates with its miniport driver by means of a series of pointers to miniport driver callback routines in its dispatch table and driver object. The miniport driver calls [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine in order to initialize SCSI Port's dispatch table and driver object with these callback pointers. One such callback pointer is the entry point for the miniport driver's start I/O routine that is used to process I/O requests. The port driver assigns this pointer to the **DriverStartIo** member of the driver object.

Whenever SCSI Port receives an I/O request from a higher-level driver, it queues the request in an internal queue. For more information about the SCSI Port's internal queues, see [SCSI Port Driver's Queue Management](scsi-port-driver-s-queue-management.md).

Once the target device is ready to receive the next I/O request, SCSI Port calls [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370), which in turn calls the miniport driver start I/O callback routine that is stored in **DriverObject-&gt;DriverStartIo**. For information about the operation and required characteristics of the miniport driver's start I/O routine, see [SCSI Miniport Driver's HwScsiStartIo Routine](scsi-miniport-driver-s-hwscsistartio-routine.md).

SCSI Port raises the IRQL of the processor before calling the miniport driver's start I/O routine, in order to mask out interrupts and to guarantee that the start I/O routine has synchronized access to critical operating system and driver structures.

While the flow of I/O request packets between a storage class driver and the SCSI Port driver is asynchronous, the flow of I/O request packets between the SCSI Port driver and the target device is synchronous. SCSI Port uses an internal queuing system that makes it possible for class drivers to send new I/O requests to SCSI Port before previous I/O requests have completed. However, SCSI Port does not send the next I/O request to the target device until it receives notification from the miniport driver that the miniport driver is ready to receive the next I/O request. The miniport driver notifies SCSI Port by making a call to the [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) library routine.

The Storport Driver offers a more flexible I/O model, in particular with regard to the masking of interrupts. For information about the differences between the Storport I/O model and the SCSI Port I/O model, see [Storport I/O Model](storport-i-o-model.md).

 

 




