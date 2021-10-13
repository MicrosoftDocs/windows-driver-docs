---
title: FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_MOD_WRITE union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_ACQUIRE_FOR_MOD_WRITE.
keywords: ["FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_MOD_WRITE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 07/17/2019
ms.localizationpriority: medium
---

# FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_MOD_WRITE union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_ACQUIRE_FOR_MOD_WRITE.

## Syntax

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PLARGE_INTEGER EndingOffset;
    PERESOURCE     *ResourceToRelease;
  } AcquireForModifiedPageWriter;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

```AcquireForModifiedPageWriter```

Structure containing the following members.

```EndingOffset```

Pointer to a variable that contains the offset of the last byte being written plus one.

```ResourceToRelease```

Pointer to a pointer to the resource ([ERESOURCE](../kernel/eresource-structures.md)) to be acquired.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_ACQUIRE_FOR_MOD_WRITE operations contains the parameters for an **AcquireForModifiedPageWriter** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

IRP_MJ_ACQUIRE_FOR_MOD_WRITE is a file system (FSFilter) callback operation. In this operation, *ResourceToRelease* is a pointer to the pointer to the resource to acquire (pre-operation) or that was acquired (post-operation). The resource will be released in an IRP_MJ_RELEASE_FOR_MOD_WRITE callback operation.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

## Requirements

**Header**: *Fltkernel.h* (include *Fltkernel.h*)


## See also

[FLT_CALLBACK_DATA](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[FLT_IO_PARAMETER_BLOCK](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[FLT_PARAMETERS](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks)
