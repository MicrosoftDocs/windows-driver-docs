---
title: IRP_MJ_PNP (FS and Filter Drivers)
description: IRP_MJ_PNP
keywords: ["IRP_MJ_PNP Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_PNP
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_PNP (FS and filter drivers)

## When Sent

The Plug and Play Manager sends the IRP_MJ_PNP request whenever Plug and Play activity occurs on the system. Other operating system components and other kernel-mode drivers can also send certain IRP_MJ_PNP requests, depending on the minor function code.

For more information about Plug and Play IRP processing requirements for drivers, see [Plug and Play](../kernel/introduction-to-plug-and-play.md).

For reference information about IRP_MJ_PNP minor function codes, see [Plug and Play Minor IRPs](../kernel/plug-and-play-minor-irps.md).

## Operation: File System Drivers

The file system should check the minor function code to determine which operation is requested. File systems must handle the following minor function codes:

| Code | Description |
| ---- | ----------- |
| IRP_MN_CANCEL_REMOVE_DEVICE | Indicates that a previous query-remove device request was canceled. This request is sent to alert the file system in case it needs to perform any cleanup related to the cancellation. |
| IRP_MN_QUERY_REMOVE_DEVICE | Indicates that a device is about to be removed. If a file system is mounted on the device, the PnP Manager sends this request to the file system and to any file system filters. If there are open handles to the device, the file system typically fails the query-remove request. If not, the file system typically locks the volume to prevent future create requests from succeeding. If a mounted file system doesn't support a query-remove request, the PnP Manager fails the query-remove request for the device. |
| IRP_MN_REMOVE_DEVICE | Indicates that a device is about to be removed. If a file system is mounted on the device, the PnP Manager sends this IRP to the file system and to any file system filters. The file system should immediately pass this IRP to the storage driver for the device, setting a completion routine in which the file system then dismounts the volume. |
| IRP_MN_START_DEVICE | Indicates that a device is being started. The file system should pass this IRP to the storage driver for the device. |
| IRP_MN_SURPRISE_REMOVAL | Indicates that a device has been removed. If a file system was mounted on the device, the PnP Manager sends this IRP to the file system and to any file system filters. The file system should immediately pass this IRP to the storage driver for the device, setting a completion routine in which the file system then dismounts the volume. |

## Operation: Legacy File System Filter Drivers

File system filter drivers should handle PnP IRPs according to the following guidelines:

- When the user is about to gracefully remove a volume, the PnP Manager sends an IRP_MN_QUERY_REMOVE_DEVICE request. On receiving this IRP, the filter must close all open handles on the volume and pass the IRP down to the next-lower driver on the stack. This step is important. If the driver fails to close all open handles, the volume is prevented from being dismounted, which in turn prevents the physical device from being ejected.

  On receiving an IRP_MN_QUERY_REMOVE_DEVICE request, the FAT file system immediately dismounts all volumes that it can safely remove. Thus any filter attached to a FAT volume should expect that its filter device object will be freed before the filter's completion routine is called. The NTFS file system doesn't do this. Thus a filter attached to an NTFS volume can expect that its device object is still attached to the volume when the filter's completion routine is called.

- IRPs that are received after an IRP_MN_QUERY_REMOVE_DEVICE request but before an IRP_MN_CANCEL_REMOVE_DEVICE or IRP_MN_REMOVE_DEVICE request is received, can safely be passed down the stack for the storage device stack to fail them, or held in a queue until the cancel-remove or remove-device request is received.

- If a filter receives an IRP_MN_CANCEL_REMOVE_DEVICE request after it has already closed all open handles for a volume in response to an IRP_MN_QUERY_REMOVE_DEVICE request, it can reopen the handles. However, the filter can only do this reopen in its completion routine, after the IRP has been completed successfully by the drivers below it in the stack.

- When a filter receives an IRP_MN_REMOVE_DEVICE request, it typically doesn't need to perform any processing on the IRP, unless it has been holding IRPs in a queue since receiving the IRP_MN_QUERY_REMOVE_DEVICE request. If it's holding IRPs in a queue, the filter must dequeue all IRPs for the volume and *fail* them before passing the IRP down to the next-lower driver on the stack.

- On receiving an IRP_MN_SURPRISE_REMOVAL request, the filter should do the following operations:

  - Close all open handles to the volume, because the file system can't clean up the stack until there are no outstanding references.

  - If the filter is holding IRPs in a queue, it can either fail them or pass them down the stack for the storage device stack to fail them.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a Plug and Play request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **IrpSp->FileObject** should point to **NULL** for PnP IRPs.

- **IrpSp->MajorFunction** is set to IRP_MJ_PNP.

- **IrpSp->MinorFunction** is set to one of the following values:

  - IRP_MN_CANCEL_REMOVE_DEVICE
  - IRP_MN_QUERY_REMOVE_DEVICE
  - IRP_MN_REMOVE_DEVICE
  - IRP_MN_START_DEVICE
  - IRP_MN_SURPRISE_REMOVAL

## See also

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_PNP (WDK Kernel Reference)**](../kernel/irp-mj-pnp.md)

[**IRP_MN_CANCEL_REMOVE_DEVICE**](../kernel/irp-mn-cancel-remove-device.md)

[**IRP_MN_QUERY_REMOVE_DEVICE**](../kernel/irp-mn-query-remove-device.md)

[**IRP_MN_REMOVE_DEVICE**](../kernel/irp-mn-remove-device.md)

[**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md)

[**IRP_MN_SURPRISE_REMOVAL**](../kernel/irp-mn-surprise-removal.md)
