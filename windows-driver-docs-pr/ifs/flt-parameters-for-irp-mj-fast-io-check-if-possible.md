---
title: FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE.
keywords: ["FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    LARGE_INTEGER             FileOffset;
    ULONG                     Length;
    ULONG POINTER_ALIGNMENT   LockKey;
    BOOLEAN POINTER_ALIGNMENT CheckForReadOperation;
  } FastIoCheckIfPossible;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **FastIoCheckIfPossible**: Structure containing the following members.

- **FileOffset**: Starting byte offset within the cached file.

- **Length**: Length, in bytes, of the data to be read or written.

- **LockKey**: Key value associated with a byte-range lock on the target file. If the range to be read or written overlaps or is a subrange of a nonexclusively locked range within the file, this parameter must be the key for that shared lock. The shared lock must be held by the parent process of the calling thread; otherwise, this parameter is ignored.

**CheckForReadOperation**: Specifies whether this operation is to check for a read or write operation. It is set to **TRUE** for a read operation and **FALSE** for a write operation.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE operations contains the parameters for a **FastIoCheckIfPossible** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE is a fast I/O operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FsRtlAreThereCurrentFileLocks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlaretherecurrentfilelocks)

[**FsRtlCopyRead**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopyread)

[**FsRtlCopyWrite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopywrite)
