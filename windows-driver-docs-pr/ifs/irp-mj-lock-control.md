---
title: IRP_MJ_LOCK_CONTROL (FS and Filter Drivers)
description: IRP_MJ_LOCK_CONTROL
keywords: ["IRP_MJ_LOCK_CONTROL Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_LOCK_CONTROL
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_LOCK_CONTROL (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_LOCK_CONTROL requests.

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether the target device object is the file system's control device object. If so, the file system driver should complete the IRP as appropriate without processing the lock request.

Otherwise, if the request has been issued on a handle that represents a user file open, the file system driver should perform the operation indicated by the minor function code and complete the IRP. If not, the driver should fail the IRP.

The following are the valid minor function codes:

| Code | Description |
| ---- | ----------- |
| IRP_MN_LOCK  | Indicates a byte-range lock request, possibly on behalf of a user-mode application that has called the Win32 [**LockFile**](/windows/win32/api/fileapi/nf-fileapi-lockfile) function. |
| IRP_MN_UNLOCK_ALL        | Indicates a request to release all byte-range locks for a file, usually because the last outstanding handle to a file object is being closed. |
| IRP_MN_UNLOCK_ALL_BY_KEY | Indicates a request to release all byte-range locks with a specified key value. |
| IRP_MN_UNLOCK_SINGLE     | Indicates a request to release a single byte-range lock, possibly on behalf of a user-mode application that has called the Win32 [**UnlockFile**](/windows/win32/api/fileapi/nf-fileapi-unlockfile) function. |

## Operation: Legacy File System Filter Drivers

File system filter drivers should pass the IRP down to the next-lower driver on the stack after performing any needed processing.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a lock control request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **IrpSp->FileObject** points to the file object that is associated with *DeviceObject*.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_LOCK_CONTROL and shouldn't be used.

- **IrpSp->Flags** can be one or more of the following values:

| Flag | Meaning |
| ---- | ------- |
| SL_EXCLUSIVE_LOCK   | If this flag is set, an exclusive byte-range lock is requested. Otherwise, a shared lock is requested. |
| SL_FAIL_IMMEDIATELY | If this flag is set, the lock request should fail if it can't be granted immediately. |

- **IrpSp->MajorFunction** is set to IRP_MJ_LOCK_CONTROL.

- **IrpSp->MinorFunction** is set to one of the following values:

  - IRP_MN_LOCK
  - IRP_MN_UNLOCK_ALL
  - IRP_MN_UNLOCK_ALL_BY_KEY
  - IRP_MN_UNLOCK_SINGLE

- **IrpSp->Parameters.LockControl.ByteOffset** is the starting byte offset within the file of the byte range to be locked or unlocked.

- **IrpSp->Parameters.LockControl.Key** is the key for the byte-range lock.

- **IrpSp->Parameters.LockControl.Length** is the length, in bytes, of the byte range to be locked or unlocked.

## See also

[**FltProcessFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltprocessfilelock)

[**FsRtlProcessFileLock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprocessfilelock)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)
