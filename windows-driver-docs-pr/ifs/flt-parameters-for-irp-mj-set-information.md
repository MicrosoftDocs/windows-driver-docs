---
title: FLT_PARAMETERS for IRP_MJ_SET_INFORMATION Union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SET_INFORMATION.
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_SET_INFORMATION union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_SET_INFORMATION**](irp-mj-set-information.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                    Length;
    FILE_INFORMATION_CLASS POINTER_ALIGNMENT FileInformationClass;
    PFILE_OBJECT                             ParentOfTarget;
    union {
      struct {
        BOOLEAN ReplaceIfExists;
        BOOLEAN AdvanceOnly;
      };
      ULONG  ClusterCount;
      HANDLE DeleteHandle;
    };
    PVOID                                    InfoBuffer;
  } SetFileInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **SetFileInformation**: Structure containing the following members.

- **Length**: Length, in bytes, of the buffer at **InfoBuffer**.

- **FileInformationClass**: Type of information to be set for the file. One of the following:

  | Value | Meaning |
  | ----- | ------- |
  | FileAllocationInformation | Set [**FILE_ALLOCATION_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_allocation_information) for the file. |
  | FileBasicInformation | Set [**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information) for the file. |
  | FileDispositionInformation | Set [**FILE_DISPOSITION_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information) for the file. |
  | FileEndOfFileInformation | Set [**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information) for the file. |
  | FileLinkInformation | Set [**FILE_LINK_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information) for the file. |
  | FilePositionInformation | Set [**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information) for the file. |
  | FileRenameInformation | Set [**FILE_RENAME_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information) for the file. |
  | FileValidDataLengthInformation | Set [**FILE_VALID_DATA_LENGTH_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_valid_data_length_information) for the file. |

- **ParentOfTarget**: For rename or link operations. If **InfoBuffer-&gt;FileName** contains a fully qualified file name, or if **InfoBuffer-&gt;RootDirectory** is non-**NULL**, this member is a file object pointer for the parent directory of the file that is the target of the operation. Otherwise it is **NULL**.

- ( *unnamed struct* )  
Structure containing the following members.

- **ReplaceIfExists**: For rename or link operations. Set to **TRUE** to specify that a file that already exists with the same name is to be replaced with the given file. Set to **FALSE** if the rename or link operation should fail if a file with the given name already exists.

- **AdvanceOnly**: A flag for end-of-file operations. This determines the use of the **EndOfFile** member [**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information) structure when **FileInformationClass** == **FileEndOfFileInformation**. If **TRUE**, a new valid data length for the file will be set from **EndOfFile** only if it increases the current valid data length. If **FALSE**, a new file size is set from **EndOfFile**.

- **ClusterCount**: Reserved for system use. Do not use.

- **DeleteHandle**: Reserved for system use. Do not use.

- **InfoBuffer**: Pointer to an input buffer that contains the file information to be set.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_SET_INFORMATION operations contains the parameters for a set-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_SET_INFORMATION is an IRP-based operation.

The **AdvanceOnly** member is set to **TRUE** by the cache manager to notify the file system to advance the current valid data length on the disk to the new valid data length in **EndOfFile**. If **AdvanceOnly** is **FALSE**, a new file size, in the **EndOfFile** member, is being set which can be larger or smaller than the current file size.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_ALLOCATION_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_allocation_information)

[**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)

[**FILE_DISPOSITION_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information)

[**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information)

[**FILE_LINK_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information)

[**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)

[**FILE_RENAME_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information)

[**FILE_VALID_DATA_LENGTH_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_valid_data_length_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_SET_INFORMATION**](irp-mj-set-information.md)
