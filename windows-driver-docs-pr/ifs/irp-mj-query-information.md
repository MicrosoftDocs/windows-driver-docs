---
title: IRP_MJ_QUERY_INFORMATION (FS and Filter Drivers)
description: IRP_MJ_QUERY_INFORMATION
keywords: ["IRP_MJ_QUERY_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_INFORMATION
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_QUERY_INFORMATION (FS and filter drivers)

## When Sent

The I/O Manager, other operating system components, and other kernel-mode drivers send IRP_MJ_QUERY_INFORMATION requests.  This request can be sent, for example, when a user-mode application has called a Win32 function such as **GetFileInformationByHandle** or when a kernel-mode component has called [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether it represents a user open of a file or directory. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

The types of file and directory information that can be queried are file system-dependent, but generally include the following values:

- FileAllInformation
- FileAlternateNameInformation
- FileAttributeTagInformation
- FileBasicInformation
- FileCompressionInformation
- FileEaInformation
- FileInternalInformation
- FileNameInformation
- FileNetworkOpenInformation
- FilePositionInformation
- FileStandardInformation
- FileStreamInformation
- FileHardLinkInformation

Although the FileAccessInformation, FileAlignmentInformation, and FileModeInformation information types can also be passed as a parameter to [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile), this information is file-system-independent. Thus **ZwQueryInformationFile** supplies this information directly, without sending an IRP_MJ_QUERY_INFORMATION request to the file system.

For a list of all possible information types, see the FILE_INFORMATION_CLASS enumeration in *ntifs.h*.

## Operation: Network Redirector Drivers

A network redirector driver not based on [RDBSS](./the-rdbss-driver-and-library.md) that receives an IRP_MJ_QUERY_INFORMATION request for FileAllInformation or FileNameInformation must respond with the full "\\server\\share\\file" path for the file name with a single leading backslash before the server name. This format for name information must be returned for a file accessed as a Universal Naming Convention (UNC) name (*\\\\server\\share\\folder\\filename.txt*, for example) or a file located on a mapped drive (*x:\\folder\\filename.txt*, for example).

For a network mini-redirector driver (a driver that links dynamically with rdbss.sys or that links statically with rdbsslib.lib), RDBSS handles an IRP_MJ_QUERY_INFORMATION request for FileNameInformation and returns the correct name information. For a network mini-redirector driver, RDBSS handles an IRP_MJ_QUERY_INFORMATION request for FileAllInformation for the name information part of the request. The other parts of the FileAllInformation request are sent as separate requests to the network mini-redirector driver to resolve.

A network redirector that receives an IRP_MJ_QUERY_INFORMATION request for FileAlternateNameInformation should respond with the short name (8.3 characters) for the file without any path information, if a short name exists for the file.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a query file information request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to the output buffer where the file or directory information is to be returned. This information is stored in one of the following structures:

- FILE_ALL_INFORMATION
- FILE_ATTRIBUTE_TAG_INFORMATION
- FILE_BASIC_INFORMATION
- FILE_COMPRESSION_INFORMATION
- FILE_EA_INFORMATION
- FILE_INTERNAL_INFORMATION
- FILE_NAME_INFORMATION
- FILE_NETWORK_OPEN_INFORMATION
- FILE_POSITION_INFORMATION
- FILE_STANDARD_INFORMATION
- FILE_STREAM_INFORMATION
- FILE_LINKS_INFORMATION

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the **IoStatusBlock** parameter in the [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile). routine.

- **Irp->UserBuffer** is an optional pointer to a caller-supplied output buffer into which the contents of **Irp->AssociatedIrp.SystemBuffer** are copied during I/O completion by the I/O manager. Drivers don't use this buffer to return any data for the request.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_QUERY_INFORMATION and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_QUERY_INFORMATION.

- **IrpSp->Parameters.QueryFile.FileInformationClass** is the type of file information to be queried. This member can be one of the following values.

  | Value | Meaning |
  | ----- | ------- |
  | FileAllInformation | Return a FILE_ALL_INFORMATION structure for the file. |
  | FileAttributeTagInformation | Return a [**FILE_ATTRIBUTE_TAG_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information) structure for the file. |
  | FileBasicInformation | Return a [**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information) structure for the file. |
  | FileCompressionInformation | Return a FILE_COMPRESSION_INFORMATION structure for the file. |
  | FileEaInformation | Return a FILE_EA_INFORMATION structure for the file. |
  | FileInternalInformation | Return a [**FILE_INTERNAL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information) structure for the file. |
  | FileNameInformation | Return a [**FILE_NAME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information) structure for the file. |
  | FileNetworkOpenInformation | Return a single [**FILE_NETWORK_OPEN_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information) structure for the file. |
  | FilePositionInformation | Return a single [**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information) structure for the file. |
  | FileStandardInformation | Return a single [**FILE_STANDARD_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information) structure for the file. |
  | FileStreamInformation | Return a single [**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information) structure for the file. |
  | FileHardLinkInformation | Return a [**FILE_LINKS_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_links_information) structure for the file. |

- **IrpSp->Parameters.QueryFile.Length** is the length, in bytes, of the buffer pointed to by *Irp->AssociatedIrp.SystemBuffer*.

## Remarks

The I/O manager always buffers the IRP_MJ_QUERY_INFORMATION operation. The I/O Manager allocates from non-paged pool memory the **Irp->AssociatedIrp.SystemBuffer** that is used to return the requested file or directory information. As a result, the **Irp->AssociatedIrp.SystemBuffer** returned by the operating system always is a valid address for the length specified in **IrpSp->Parameters.QueryFile.Length**.

The **Irp->AssociatedIrp.UserBuffer** is used internally by the I/O manager and shouldn't be used by file system or file system filter drivers.

## See also

[**FILE_ALIGNMENT_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_alignment_information)

[**FILE_ATTRIBUTE_TAG_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information)

[**FILE_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)

[**FILE_INTERNAL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information)

[**FILE_NAME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information)

[**FILE_NETWORK_OPEN_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)

[**FILE_POSITION_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)

[**FILE_STANDARD_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information)

[**FILE_STREAM_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**FILE_LINKS_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_links_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SET_INFORMATION**](irp-mj-set-information.md)

[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)
