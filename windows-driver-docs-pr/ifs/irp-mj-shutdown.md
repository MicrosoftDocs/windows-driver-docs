---
title: IRP_MJ_SHUTDOWN (FS and filter drivers)
description: IRP_MJ_SHUTDOWN
keywords: ["IRP_MJ_SHUTDOWN Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SHUTDOWN
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_SHUTDOWN (FS and filter drivers)

## When Sent

The I/O Manager or a file system driver sends the IRP_MJ_SHUTDOWN request when the system is being shut down.

## Operation: File System Drivers

The file system should perform any necessary cleanup and complete the IRP with STATUS_SUCCESS.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a shutdown request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **IrpSp->MajorFunction** is set to IRP_MJ_SET_SHUTDOWN.

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SHUTDOWN (WDK Kernel Reference)**](../kernel/irp-mj-shutdown.md)
