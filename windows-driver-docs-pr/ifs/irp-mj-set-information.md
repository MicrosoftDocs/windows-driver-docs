---
title: IRP_MJ_SET_INFORMATION (IFS)
description: IRP_MJ_SET_INFORMATION
keywords: ["IRP_MJ_SET_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_INFORMATION
api_type:
- NA
ms.date: 01/14/2021
---

# IRP_MJ_SET_INFORMATION (IFS)

## When Sent

The IRP_MJ_SET_INFORMATION request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **SetEndOfFile** or when a kernel-mode component has called [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether it represents a user file or directory open. If it does, the file system driver should process the request as appropriate and complete the IRP.

The following types of information can be set on files *and* directories:

* FileBasicInformation
* FileDispositionInformation
* FileLinkInformation (for file systems that allow cycles to be created in the directory hierarchy)
* FilePositionInformation
* FileRenameInformation

The following types of information can be set only on files:

* FileAllocationInformation
* FileEndOfFileInformation
* FileLinkInformation (for file systems, such as NTFS, that do not allow cycles to be created in the directory hierarchy)
* FileValidDataLengthInformation

## Operation: File System Filter Drivers

The filter driver must pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set file information request:

*DeviceObject*: Pointer to the target device object.

*Irp->AssociatedIrp.SystemBuffer*: Pointer to an input buffer that contains the file or directory information to be set. This information is stored in one of the following structures:

* [**FILE_ALLOCATION_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_allocation_information)
* [**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)
* [**FILE_DISPOSITION_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information)
* [**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information)
* [**FILE_LINK_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information)
* [**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)
* [**FILE_RENAME_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information)
* [**FILE_VALID_DATA_LENGTH_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_valid_data_length_information)

*Irp->IoStatus*: Pointer to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter to [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile).

*IrpSp->FileObject*: Pointer to the file object that is associated with *DeviceObject*. This parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure is not valid during the processing of IRP_MJ_SET_INFORMATION and should not be used.

*IrpSp->MajorFunction*: Set to IRP_MJ_SET_INFORMATION.

*IrpSp->MinorFunction*: Can be IRP_MN_KERNEL_CALL when *Irp->Parameters.SetFile.FileInformationClass* is **FileValidDataLengthInformation**. This indicates that the source of the request is a trusted kernel component, allowing drivers to bypass security checks.

*IrpSp->Parameters.SetFile.AdvanceOnly*: A flag for end-of-file operations. This determines the use of the **EndOfFile** member [**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information) structure when **FileInformationClass** == **FileEndOfFileInformation**. If **TRUE**, a new valid data length for the file will be set from **EndOfFile** only if it increases the current valid data length. If **FALSE**, a new file size is set from **EndOfFile**.

*IrpSp->Parameters.SetFile.ClusterCount*: Reserved for system use.

*IrpSp->Parameters.SetFile.DeleteHandle*: Reserved for system use.

*IrpSp->Parameters.SetFile.FileInformationClass*: The type of information to be set for the file. One of the following:

| Value | Meaning |
| ----- | ------- |
| **FileAllocationInformation** | Set [**FILE_ALLOCATION_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_allocation_information) for the file. |
| **FileBasicInformation** | Set [**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information) for the file. |
| **FileDispositionInformation** | Set [**FILE_DISPOSITION_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information) for the file. |
| **FileEndOfFileInformation** | Set [**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information) for the file. |
| **FileLinkInformation** | Set [**FILE_LINK_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information) for the file. |
| **FilePositionInformation** | Set [**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information) for the file. |
| **FileRenameInformation** | Set [**FILE_RENAME_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information) for the file. |
| **FileValidDataLengthInformation** | Set [**FILE_VALID_DATA_LENGTH_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_valid_data_length_information) for the file. See *Irp->MinorFunction* for additional information. |

*IrpSp->Parameters.SetFile.FileObject*: For rename or link operations. If *Irp->AssociatedIrp.SystemBuffer->FileName* contains a fully qualified file name, or if *Irp->AssociatedIrp.SystemBuffer->RootDirectory* is non-**NULL**, this member is a file object pointer for the parent directory of the file that is the target of the operation. Otherwise it is **NULL**.

*IrpSp->Parameters.SetFile.Length*: Length, in bytes, of the buffer pointed to by *Irp->AssociatedIrp.SystemBuffer*.

*IrpSp->Parameters.SetFile.ReplaceIfExists*: Set to **TRUE** to specify that if a file with the same name already exists, it should be replaced with the given file. Set to **FALSE** if the rename operation should fail if a file with the given name already exists.

## Remarks

The **AdvanceOnly** member is set to **TRUE** by the cache manager to notify the file system to advance the current valid data length on the disk to the new valid data length in **EndOfFile**. If **AdvanceOnly** is **FALSE**, a new file size, in the **EndOfFile** member, is being set which can be larger or smaller than the current file size.

## See also

[**FILE_ALLOCATION_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_allocation_information)

[**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)

[**FILE_DISPOSITION_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information)

[**FILE_END_OF_FILE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_end_of_file_information)

[**FILE_LINK_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_link_information)

[**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)

[**FILE_RENAME_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_rename_information)

[**FILE_VALID_DATA_LENGTH_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_valid_data_length_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md)

[**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)
