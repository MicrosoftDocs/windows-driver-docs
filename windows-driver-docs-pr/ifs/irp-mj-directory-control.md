---
title: IRP_MJ_DIRECTORY_CONTROL (FS and Filter Drivers)
description: IRP_MJ_DIRECTORY_CONTROL
keywords: ["IRP_MJ_DIRECTORY_CONTROL  Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_DIRECTORY_CONTROL
api_type:
- NA
ms.date: 02/05/2024
ms.topic: reference
---

# IRP_MJ_DIRECTORY_CONTROL (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_DIRECTORY_CONTROL requests. It can be sent, for example, when a user-mode application has called a Win32 function such as **ReadDirectoryChangesW** or **FindNextVolumeMountPoint** or when a kernel-mode component has called [**ZwQueryDirectoryFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerydirectoryfile) or [**ZwQueryDirectoryFileEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerydirectoryfileex).

## Operation: File System Drivers

The file system driver should check the minor function code to determine which directory control operation is requested. The following are the valid minor function codes:

| Code | Description |
| ---- | ----------- |
| IRP_MN_QUERY_DIRECTORY | Indicates a directory query request. The types of information that can be queried are file-system-dependent, but generally include the following values: FileBothDirectoryInformation, FileDirectoryInformation, FileFullDirectoryInformation, FileIdBothDirectoryInformation, FileIdFullDirectoryInformation, FileNamesInformation, FileObjectIdInformation, FileReparsePointInformation. |
| IRP_MN_NOTIFY_CHANGE_DIRECTORY | Indicates a request for notification of changes to the directory. Usually, instead of satisfying this request immediately, the file system driver holds the IRP in a private queue. When a change occurs to the directory, the file system driver performs the notification, and dequeues and completes the IRP. The file system driver returns the information in a [**FILE_NOTIFY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_information) structure.|
| IRP_MN_NOTIFY_CHANGE_DIRECTORY_EX | Indicates a request for notification of changes to the directory. Usually, instead of satisfying this request immediately, the file system driver holds the IRP in a private queue. When a change occurs to the directory, the file system driver performs the notification, and dequeues and completes the IRP. The file system driver returns information based on the specified *IrpSp->Parameters.NotifyDirectoryEx.DirectoryNotifyInformationClass*.|

> [!NOTE]
> The FileQuotaInformation information class is obsolete. [**IRP_MJ_QUERY_QUOTA**](irp-mj-query-quota.md) should be used instead.

The file system driver should complete the IRP after it performs the requested operation.

## Operation: Legacy File System Filter Drivers

The filter driver must pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a directory control request.

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->UserBuffer** points to a caller-supplied output buffer that receives the requested information about the contents of the directory.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_DIRECTORY_CONTROL and shouldn't be used.

- **IrpSp->Flags** can be set to one or more of the following values for IRP_MN_QUERY_DIRECTORY.

| Flag | Meaning |
| ---- | ------- |
| SL_INDEX_SPECIFIED | Begin the scan at the entry in the directory whose index is given by **IrpSp->Parameters.QueryDirectory.FileIndex**. |
| SL_RESTART_SCAN | Begin the scan at the first entry in the directory. If this flag isn't set, resume the scan from a previous IRP_MN_QUERY_DIRECTORY request. |
| SL_RETURN_SINGLE_ENTRY | Return only the first entry that is found. |
| SL_RETURN_ON_DISK_ENTRIES_ONLY | Instructs any filters that perform directory virtualization or just-in-time expansion to simply pass the request through to the file system and return entries that are currently on disk. |

The following flag can be set for IRP_MN_NOTIFY_CHANGE_DIRECTORY:

| Flag | Meaning |
| ---- | ------- |
| SL_WATCH_TREE | Set to **TRUE** if all subdirectories of this directory should also be watched. Set to **FALSE** if only the directory itself is to be watched.

- **IrpSp->MajorFunction** is set to IRP_MJ_DIRECTORY_CONTROL.

- **IrpSp->MinorFunction** can be set to one of the following values.

  - IRP_MN_QUERY_DIRECTORY
  - IRP_MN_NOTIFY_CHANGE_DIRECTORY
  - IRP_MN_NOTIFY_CHANGE_DIRECTORY_EX

- **IrpSp->Parameters.QueryDirectory.FileIndex** is the index of the file at which to begin the directory scan. This value is ignored if the SL_INDEX_SPECIFIED flag isn't set. This parameter can't be specified in any Win32 function or kernel-mode support routine. Currently it's used only by the NT virtual DOS machine (NTVDM), which exists only on 32-bit NT-based platforms. The file index is undefined for file systems, such as NTFS, in which the position of a file within the parent directory isn't fixed and can be changed at any time to maintain sort order.

- **IrpSp->Parameters.QueryDirectory.FileInformationClass** is set to one of the following values.

  | Value | Meaning |
  | ----- | ------- |
  | **FileBothDirectoryInformation** | Return a [**FILE_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_both_dir_information) structure for each file. |
  | **FileDirectoryInformation** | Return a [**FILE_DIRECTORY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_directory_information) structure for each file. |
  | **FileFullDirectoryInformation** | Return a [**FILE_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_full_dir_information)" structure for each file. |
  | **FileIdBothDirectoryInformation** | Return a [**FILE_ID_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_both_dir_information) structure for each file. |
  | **FileIdFullDirectoryInformation** | Return a [**FILE_ID_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_full_dir_information) structure for each file. |
  | **FileNamesInformation** | Return a [**FILE_NAMES_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_names_information) structure for each file. |
  | **FileObjectIdInformation** | Return a [**FILE_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_objectid_information) structure for each file. |
  | **FileQuotaInformation** | Obsolete. Use [IRP_MJ_QUERY_QUOTA](irp-mj-query-quota.md) instead. |
  | **FileReparsePointInformation** | Return a single [**FILE_REPARSE_POINT_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_reparse_point_information) structure for the directory. |

- **IrpSp->Parameters.QueryDirectory.FileName** is the optional name of a file within the specified directory.

- **IrpSp->Parameters.QueryDirectory.Length** is the length in bytes of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.NotifyDirectory.Length** is the length in bytes of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.NotifyDirectory.CompletionFilter**: For more information, see the description of the **CompletionFilter** parameter to [**FsRtlNotifyFullChangeDirectory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfullchangedirectory).

- **IrpSp->Parameters.NotifyDirectoryEx.Length** is the length in bytes of the buffer pointed to by **Irp->UserBuffer**.

- **IrpSp->Parameters.NotifyDirectoryEx.CompletionFilter**: For more information, see the description of the **CompletionFilter** parameter to [**FsRtlNotifyFullChangeDirectory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfullchangedirectory).

- **IrpSp->Parameters.NotifyDirectoryEx.DirectoryNotifyInformationClass** is one of the following values.

  | Value | Meaning |
  | ----- | ------- |
  | **DirectoryNotifyInformation** | Return a [**FILE_NOTIFY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_information) structure for directory change. |
  | **DirectoryNotifyExtendedInformation** | Return a [**FILE_NOTIFY_EXTENDED_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_extended_information) structure for each directory change. |
  | **DirectoryNotifyFullInformation** | Return a [**FILE_NOTIFY_FULL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_full_information) structure for each directory change. |

## See also

[**FILE_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_both_dir_information)

[**FILE_DIRECTORY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_directory_information)

[**FILE_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_full_dir_information)

[**FILE_ID_BOTH_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_both_dir_information)

[**FILE_ID_FULL_DIR_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_id_full_dir_information)

[**FILE_NAMES_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_names_information)

[**FILE_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_objectid_information)

[**FILE_REPARSE_POINT_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_reparse_point_information)

[**FsRtlNotifyFullChangeDirectory**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlnotifyfullchangedirectory)

[**FILE_NOTIFY_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_information)

[**FILE_NOTIFY_EXTENDED_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_extended_information)

[**FILE_NOTIFY_FULL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_notify_full_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_QUERY_QUOTA**](irp-mj-query-quota.md)

[**ZwQueryDirectoryFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerydirectoryfile)

[**ZwQueryDirectoryFileEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwquerydirectoryfileex)
