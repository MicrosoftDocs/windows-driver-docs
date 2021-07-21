---
title: IRP_MJ_QUERY_INFORMATION (IFS)
description: IRP\_MJ\_QUERY\_INFORMATION
keywords: ["IRP_MJ_QUERY_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_INFORMATION
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_QUERY\_INFORMATION (IFS)


## When Sent


The IRP\_MJ\_QUERY\_INFORMATION request is sent by the I/O Manager and other operating system components, as well as by other kernel-mode drivers. This request can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **GetFileInformationByHandle** or when a kernel-mode component has called [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile).

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether it represents a user open of a file or directory. If it does, the driver should process the query and complete the IRP. Otherwise, the driver should complete the IRP as appropriate without processing the query.

The types of file and directory information that can be queried are file system-dependent, but generally include the following:

FileAllInformation
FileAlternateNameInformation
FileAttributeTagInformation
FileBasicInformation
FileCompressionInformation
FileEaInformation
FileInternalInformation
FileNameInformation
FileNetworkOpenInformation
FilePositionInformation
FileStandardInformation
FileStreamInformation
FileHardLinkInformation
Although the FileAccessInformation, FileAlignmentInformation, and FileModeInformation information types can also be passed as a parameter to [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile), this information is file-system-independent. Thus **ZwQueryInformationFile** supplies this information directly, without sending an IRP\_MJ\_QUERY\_INFORMATION request to the file system.

For more information about these information types, refer to the See Also links below. For a list of all possible information types, see the FILE\_INFORMATION\_CLASS enumeration in ntifs.h.

## Operation: Network Redirector Drivers


A network redirector driver not based on [RDBSS](./the-rdbss-driver-and-library.md) that receives an IRP\_MJ\_QUERY\_INFORMATION request for FileAllInformation or FileNameInformation, must respond with the full "\\server\\share\\file" path for the file name with a single leading backslash before the server name. This format for name information must be returned for a file accessed as a Universal Naming Convention (UNC) name (*\\\\server\\share\\folder\\filename.txt*, for example) or a file located on a mapped drive (*x:\\folder\\filename.txt*, for example).

For a network mini-redirector driver (a driver that links dynamically with rdbss.sys or that links statically with rdbsslib.lib), an IRP\_MJ\_QUERY\_INFORMATION request for FileNameInformation is handled internally by RDBSS and the correct name information is returned. For a network mini-redirector driver, an IRP\_MJ\_QUERY\_INFORMATION request for FileAllInformation is handled internally by RDBSS for the name information part of the request. The other parts of the FileAllInformation request are sent as separate requests to the network mini-redirector driver to resolve.

A network redirector that receives an IRP\_MJ\_QUERY\_INFORMATION request for FileAlternateNameInformation should respond with the short name (8.3 characters) for the file without any path information, if a short name exists for the file.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the given IRP to get a pointer to its own [**stack location**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a query file information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to the output buffer where the file or directory information is to be returned. This information is stored in one of the following structures:

FILE\_ALL\_INFORMATION

FILE\_ATTRIBUTE\_TAG\_INFORMATION

FILE\_BASIC\_INFORMATION

FILE\_COMPRESSION\_INFORMATION

FILE\_EA\_INFORMATION

FILE\_INTERNAL\_INFORMATION

FILE\_NAME\_INFORMATION

FILE\_NETWORK\_OPEN\_INFORMATION

FILE\_POSITION\_INFORMATION

FILE\_STANDARD\_INFORMATION

FILE\_STREAM\_INFORMATION

FILE\_LINKS\_INFORMATION

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter in the [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile). routine.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*
Optional pointer to a caller-supplied output buffer into which the contents of *Irp-&gt;AssociatedIrp.SystemBuffer* are copied during I/O completion by the I/O manager. Drivers do not use this buffer to return any data for the request.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_QUERY\_INFORMATION and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_QUERY\_INFORMATION.

<a href="" id="irpsp--parameters-queryfile-fileinformationclass"></a>*IrpSp-&gt;Parameters.QueryFile.FileInformationClass*
Type of file information to be queried. This member can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>FileAllInformation</strong></p></td>
<td align="left"><p>Return a FILE_ALL_INFORMATION structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileAttributeTagInformation</strong></p></td>
<td align="left"><p>Return a <a href="/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information" data-raw-source="[&lt;strong&gt;FILE_ATTRIBUTE_TAG_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information)"><strong>FILE_ATTRIBUTE_TAG_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileBasicInformation</strong></p></td>
<td align="left"><p>Return a <a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information" data-raw-source="[&lt;strong&gt;FILE_BASIC_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)"><strong>FILE_BASIC_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileCompressionInformation</strong></p></td>
<td align="left"><p>Return a FILE_COMPRESSION_INFORMATION structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileEaInformation</strong></p></td>
<td align="left"><p>Return a FILE_EA_INFORMATION structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileInternalInformation</strong></p></td>
<td align="left"><p>Return a <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information" data-raw-source="[&lt;strong&gt;FILE_INTERNAL_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information)"><strong>FILE_INTERNAL_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileNameInformation</strong></p></td>
<td align="left"><p>Return a <a href="/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information" data-raw-source="[&lt;strong&gt;FILE_NAME_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information)"><strong>FILE_NAME_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileNetworkOpenInformation</strong></p></td>
<td align="left"><p>Return a single <a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information" data-raw-source="[&lt;strong&gt;FILE_NETWORK_OPEN_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)"><strong>FILE_NETWORK_OPEN_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FilePositionInformation</strong></p></td>
<td align="left"><p>Return a single <a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information" data-raw-source="[&lt;strong&gt;FILE_POSITION_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)"><strong>FILE_POSITION_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileStandardInformation</strong></p></td>
<td align="left"><p>Return a single <a href="/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information" data-raw-source="[&lt;strong&gt;FILE_STANDARD_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information)"><strong>FILE_STANDARD_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileStreamInformation</strong></p></td>
<td align="left"><p>Return a single <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information" data-raw-source="[&lt;strong&gt;FILE_STREAM_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)"><strong>FILE_STREAM_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileHardLinkInformation</strong></p></td>
<td align="left"><p>Return a <a href="/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_links_information" data-raw-source="[&lt;strong&gt;FILE_LINKS_INFORMATION&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_links_information)"><strong>FILE_LINKS_INFORMATION</strong></a> structure for the file.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--parameters-queryfile-length"></a>*IrpSp-&gt;Parameters.QueryFile.Length*
Length, in bytes, of the buffer pointed to by *Irp-&gt;AssociatedIrp.SystemBuffer*.

## Remarks

The IRP\_MJ\_QUERY\_INFORMATION operation is always buffered by the I/O manager. The *Irp-&gt;AssociatedIrp.SystemBuffer* that is used to return the requested file or directory information is allocated by the I/O manager from non-paged pool memory. As a result, the *Irp-&gt;AssociatedIrp.SystemBuffer* returned by the operating system will always be a valid address for the length specified in *IrpSp-&gt;Parameters.QueryFile.Length*.

The *Irp-&gt;AssociatedIrp.UserBuffer* is used internally by the I/O manager and should not be used by file system or file system filter drivers.

## See also


[**FILE\_ALIGNMENT\_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_alignment_information)

[**FILE\_ATTRIBUTE\_TAG\_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_attribute_tag_information)

[**FILE\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_basic_information)

[**FILE\_INTERNAL\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_internal_information)

[**FILE\_NAME\_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_name_information)

[**FILE\_NETWORK\_OPEN\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_network_open_information)

[**FILE\_POSITION\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_position_information)

[**FILE\_STANDARD\_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_standard_information)

[**FILE\_STREAM\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_stream_information)

[**FILE\_LINKS\_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_links_information)

[**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO\_STATUS\_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoCheckEaBufferValidity**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckeabuffervalidity)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md)

[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)

