---
title: FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION.
keywords: ["FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    FS_FILTER_SECTION_SYNC_TYPE SyncType;
    ULONG POINTER_ALIGNMENT     PageProtection;
    PFS_FILTER_SECTION_SYNC_OUTPUT OutputInformation;
  } AcquireForSectionSynchronization;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **SyncType**: The type of synchronization requested for the section. This parameter is set to **SyncTypeCreateSection** if a section is being created; otherwise, it is set to **SyncTypeOther**.

- **PageProtection**: The type of page protection requested for the section. Must be zero if **SyncType** is SyncTypeOther. Otherwise, this parameter must be one of the defined [memory protection constant values](/windows/win32/memory/memory-protection-constants).

- **OutputInformation**: A [**FS_FILTER_SECTION_SYNC_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fs_filter_section_sync_output) structure that specifies information describing the attributes of the section that is being created.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION operations contains the parameters for an **AcquireForSectionSynchronization** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_ACQUIRE_FOR_SECTION_SYNCHRONIZATION is a file system (FSFilter) callback operation.

If the enumerated value of the **SyncType** member is set to **SyncTypeOther**, a file system minifilter or legacy filter driver cannot fail this operation. If **SyncType** is set to **SyncTypeCreateSection**, a file system minifilter or legacy filter driver is allowed to fail with a STATUS_INSUFFICIENT_RESOURCES error if there is not enough memory to create the section.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

## Requirements

**Version**: Available in Windows XP and later versions of the Windows operating system.

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks)
