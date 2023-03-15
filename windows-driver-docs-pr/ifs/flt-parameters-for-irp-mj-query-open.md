---
title: FLT_PARAMETERS for IRP_MJ_QUERY_OPEN union
description: The following union component is used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_OPEN.
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_OPEN union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_QUERY_OPEN union

The following union component is used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP_MJ_QUERY_OPEN.

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    PIRP                   Irp;
    PVOID                  FileInformation;
    PULONG                 Length;
    FILE_INFORMATION_CLASS FileInformationClass;
  } QueryOpen;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **Irp**: A pointer to the IRP associated with this operation.

- **FileInformation**: A pointer to a caller-allocated buffer into which the routine writes the requested information about the file object. The **FileInformationClass** member specifies the type of information that the caller requests.

- **Length**: The size, in bytes, of the buffer pointed to by **FileInformation**.

- **FileInformationClass**: Specifies the type of information to be returned about the file, in the buffer that **FileInformation** points to. Device and intermediate drivers can specify any of the following [**FILE_INFORMATION_CLASS**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class) values. Other values cause the call to fail and should not be passed to PreQueryOpen/PostQueryOpen calls.

  | FILE_INFORMATION_CLASS value | Type of information returned |
  | --- | --- |
  | FileStatInformation | A [**FILE_STAT_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stat_information) structure. This structure contains an access mask. For more information about access masks, see [ACCESS_MASK](../kernel/access-mask.md). |
  | FileStatLxInformation | A [**FILE_STAT_LX_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stat_lx_information) structure. This structure contains an access mask. For more information about access masks, see [ACCESS_MASK](../kernel/access-mask.md). |
  | FileCaseSensitiveInformation | A [**FILE_CASE_SENSITIVE_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_case_sensitive_information) structure. |

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_QUERY_OPEN operations contains the parameters for an **QueryOpen** operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_QUERY_OPEN is a file system (FSFilter) callback operation.

For more information about FSFilter callback operations, see the reference entry for [**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks).

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

[**FsRtlRegisterFileSystemFilterCallbacks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlregisterfilesystemfiltercallbacks)
