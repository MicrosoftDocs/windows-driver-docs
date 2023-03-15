---
title: FLT_PARAMETERS for IRP_MJ_LOCK_CONTROL union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_LOCK_CONTROL.
keywords: ["FLT_PARAMETERS for IRP_MJ_LOCK_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_LOCK_CONTROL union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_LOCK_CONTROL**](irp-mj-lock-control.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PLARGE_INTEGER          Length;
    ULONG POINTER_ALIGNMENT Key;
    LARGE_INTEGER           ByteOffset;
    PEPROCESS               ProcessId;
    BOOLEAN                 FailImmediately;
    BOOLEAN                 ExclusiveLock;
  } LockControl;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **LockControl**: Structure containing the following members.

- **Length**: Pointer to a variable that specifies the length in bytes of the range to be locked.

- **Key**: Key value to be assigned to the byte-range lock.

- **ByteOffset**: Starting byte offset within the file of the range to be locked.

- **ProcessId**: Opaque pointer to the process object for the process that requested the byte-range lock.

- **FailImmediately**: Boolean value specifying whether the lock request should fail if the lock cannot be granted immediately. This member is set to **FALSE** if the requesting thread can be put into a wait state until the request is granted or **TRUE** if it cannot.  

- **ExclusiveLock**: Boolean value specifying whether an exclusive lock is requested. This member is set to **TRUE** if an exclusive lock is requested or **FALSE** if a shared lock is requested.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for the [**IRP_MJ_LOCK_CONTROL**](irp-mj-lock-control.md) operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

IRP_MJ_LOCK_CONTROL can be an IRP-based I/O operation or a fast I/O operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**ACCESS_MASK**](../kernel/access-mask.md)

[**ACCESS_STATE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltAllocateFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatefilelock)

[**FltCheckLockForReadAccess**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltchecklockforreadaccess)

[**FltCheckLockForWriteAccess**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltchecklockforwriteaccess)

[**FltFreeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreefilelock)

[**FltInitializeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitializefilelock)

[**FltProcessFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltprocessfilelock)

[**FltUninitializeFileLock**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuninitializefilelock)

[**IRP_MJ_LOCK_CONTROL**](irp-mj-lock-control.md)

[**PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_complete_lock_callback_data_routine)

[**PUNLOCK_ROUTINE**](punlock-routine.md)
