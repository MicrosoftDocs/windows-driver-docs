---
title: FLT_PARAMETERS for IRP_MJ_RELEASE_FOR_MOD_WRITE Union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_RELEASE_FOR_MOD_WRITE.
keywords: ["FLT_PARAMETERS for IRP_MJ_RELEASE_FOR_MOD_WRITE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 02/02/2024
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_RELEASE_FOR_MOD_WRITE union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_RELEASE_FOR_MOD_WRITE.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PERESOURCE ResourceToRelease;
  } ReleaseForModifiedPageWriter;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **ReleaseForModifiedPageWriter**: Structure containing the following members.

- **ResourceToRelease**: Pointer to the resource to be released.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_RELEASE_FOR_MOD_WRITE operations contains the parameters for a **ReleaseForModifiedPageWriter** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_RELEASE_FOR_MOD_WRITE is a file system (FSFilter) callback operation.

IRP_MJ_RELEASE_FOR_MOD_WRITE is typically invoked from the modified page writer as part of a special kernel APC. It always runs at IRQL = APC_LEVEL. Because it might be called in the context of a special kernel APC, it can preempt kernel-mode code that executes at IRQL = PASSIVE_LEVEL, including both user APCs and normal kernel APCs. Therefore, take care when waiting on resources that may be held by a thread that the IRP_MJ_RELEASE_FOR_MODE_WRITE operation may have preempted. Attempting to wait on such resources may result in a deadlock.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flt_is_fastio_operation)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks)
