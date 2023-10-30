---
title: FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_DIRECTORY_CONTROL.
keywords: ["FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_DIRECTORY_CONTROL union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_DIRECTORY_CONTROL**](irp-mj-directory-control.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...   ;
  union {
    struct {
      ULONG                   Length;
      PUNICODE_STRING         FileName;
      FILE_INFORMATION_CLASS  FileInformationClass;
      ULONG POINTER_ALIGNMENT FileIndex;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } QueryDirectory;
    struct {
      ULONG                   Length;
      ULONG POINTER_ALIGNMENT CompletionFilter;
      ULONG                   Spare1;
      ULONG POINTER_ALIGNMENT Spare2;
      PVOID                   DirectoryBuffer;
      PMDL                    MdlAddress;
    } NotifyDirectory;
  } DirectoryControl;
  ...   ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **DirectoryControl**: Structure containing the following members.

- **QueryDirectory**: Union component used for IRP_MN_QUERY_DIRECTORY operations.

- **Length**: Length, in bytes, of the buffer that the **QueryDirectory.DirectoryBuffer** member points to.

- **FileName**: Pointer to a [**UNICODE_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure that contains the name of a file within the specified directory.

- **FileInformationClass**: Specifies one of the values described below.

  | Value | Meaning |
  |-------|---------|
  | FileBothDirectoryInformation   | Return a [**FILE_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_both_dir_information) structure for each file.                      |
  | FileDirectoryInformation       | Return a [**FILE_DIRECTORY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_directory_information) structure for each file.                     |
  | FileFullDirectoryInformation   | Return a [**FILE_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_full_dir_information) structure for each file.                      |
  | FileIdBothDirectoryInformation | Return a [**FILE_ID_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_both_dir_information) structure for each file.               |
  | FileIdFullDirectoryInformation | Return a [**FILE_ID_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_full_dir_information) structure for each file.               |
  | FileNamesInformation           | Return a [**FILE_NAMES_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_names_information) structure for each file.                             |
  | FileObjectIdInformation        | Return a [**FILE_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_objectid_information) structure for each file.                       |
  | FileReparsePointInformation    | Return a single [**FILE_REPARSE_POINT_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_reparse_point_information) structure for the directory. |

- **FileIndex**: Index of the file where the directory scan begins. Ignored if the SL_INDEX_SPECIFIED flag is not set. This parameter cannot be specified in any Win32 function or kernel-mode support routine. Currently it is used only by the NT virtual DOS machine (NTVDM), which exists only on 32-bit NT-based operating systems. Note that the file index is undefined for file systems, such as NTFS, in which the position of a file within the parent directory is not fixed and can be changed at any time to maintain sort order.

- **DirectoryBuffer**: Pointer to a caller-supplied output buffer that receives the requested information about the contents of the directory. This member is optional and can be NULL if a MDL is provided in **QueryDirectory.MdlAddress**. See **Remarks**.

- **MdlAddress**: Address of a memory descriptor list (MDL) that describes the buffer that the **QueryDirectory.DirectoryBuffer** member points to. This member is optional and can be **NULL** if a buffer is provided in **QueryDirectory.DirectoryBuffer**. See **Remarks**.

- **NotifyDirectory**: Union component used for IRP_MN_NOTIFY_CHANGE_DIRECTORY operations.

- **Length**: Length, in bytes, of the buffer that the **NotifyDirectory.DirectoryBuffer** member points to.

- **CompletionFilter**: Bitmask of flags that specify the types of changes to files or directories that should cause the IRPs in the notify list to be completed. The possible flag values are described following.

  | Flag | Meaning  |
  |------|----------|
  | FILE_NOTIFY_CHANGE_FILE_NAME    | A file has been added, deleted, or renamed in this directory.                  |
  | FILE_NOTIFY_CHANGE_DIR_NAME     | A subdirectory has been created, removed, or renamed.                          |
  | FILE_NOTIFY_CHANGE_NAME          | This directory's name has changed.                                             |
  | FILE_NOTIFY_CHANGE_ATTRIBUTES    | The value of an attribute of this file, such as last access time, has changed. |
  | FILE_NOTIFY_CHANGE_SIZE          | This file's size has changed.                                                  |
  | FILE_NOTIFY_CHANGE_LAST_WRITE   | This file's last modification time has changed.                                |
  | FILE_NOTIFY_CHANGE_LAST_ACCESS  | This file's last access time has changed.                                      |
  | FILE_NOTIFY_CHANGE_CREATION      | This file's creation time has changed.                                         |
  | FILE_NOTIFY_CHANGE_EA            | This file's extended attributes have been modified.                            |
  | FILE_NOTIFY_CHANGE_SECURITY      | This file's security information has changed.                                  |
  | FILE_NOTIFY_CHANGE_STREAM_NAME  | A file stream has been added, deleted, or renamed in this directory.           |
  | FILE_NOTIFY_CHANGE_STREAM_SIZE  | This file stream's size has changed.                                           |
  | FILE_NOTIFY_CHANGE_STREAM_WRITE | This file stream's data has changed.                                           |

- **Spare1**: Not currently used.

- **Spare2**: Not currently used.

- **DirectoryBuffer**: Pointer to a caller-supplied output buffer that receives the requested information about the contents of the directory. This member is optional and can be NULL if a MDL is provided in **NotifyDirectory.MdlAddress**. See **Remarks**.

- **MdlAddress**: Address of an MDL that describes the buffer that the **NotifyDirectory.DirectoryBuffer** member points to. This member is optional and can be **NULL** if a buffer is provided in **NotifyDirectory.DirectoryBuffer**. See **Remarks**.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_DIRECTORY_CONTROL operations contains the parameters for an IRP-based directory-control-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

If both a **DirectoryBuffer** and **MdlAddress** buffer are provided, it is recommended that minifilters use the MDL. The memory that **DirectoryBuffer** points to is valid when it is a user mode address being accessed within the context of the calling process, or if it is a kernel mode address.

If a minifilter changes the value of **MdlAddress**, then after its post operation callback, Filter Manager will free the MDL currently stored in **MdlAddress** and restore the previous value of **MdlAddress**.

IRP_MJ_DIRECTORY_CONTROL is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_both_dir_information)

[**FILE_DIRECTORY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_directory_information)

[**FILE_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_full_dir_information)

[**FILE_ID_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_both_dir_information)

[**FILE_ID_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_full_dir_information)

[**FILE_NAMES_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_names_information)

[**FILE_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_objectid_information)

[**FILE_REPARSE_POINT_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_reparse_point_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltNotifyFilterChangeDirectory**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltnotifyfilterchangedirectory)

[**FsRtlNotifyFilterChangeDirectory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfilterchangedirectory)

[**FsRtlNotifyFilterReportChange**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfilterreportchange)

[**FsRtlNotifyFullChangeDirectory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfullchangedirectory)

[**FsRtlNotifyFullReportChange**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfullreportchange)

[**IRP_MJ_DIRECTORY_CONTROL**](irp-mj-directory-control.md)

[**ZwQueryDirectoryFile**](/previous-versions/ff567047(v=vs.85))
