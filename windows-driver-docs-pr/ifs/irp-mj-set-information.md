---
title: IRP\_MJ\_SET\_INFORMATION
description: IRP\_MJ\_SET\_INFORMATION
ms.assetid: cc1b539c-8d39-4f4d-93b1-ce9fcdb8c555
keywords: ["IRP_MJ_SET_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_INFORMATION
api_type:
- NA
---

# IRP\_MJ\_SET\_INFORMATION


## When Sent


The IRP\_MJ\_SET\_INFORMATION request is sent by the I/O Manager and other operating system components, as well as other kernel-mode drivers. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **SetEndOfFile** or when a kernel-mode component has called [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096).

## <a href="" id="operation-fsd"></a>Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether it represents a user file or directory open. If it does, the file system driver should process the request as appropriate and complete the IRP.

The following types of information can be set on files and directories:

FileBasicInformation

FileDispositionInformation

FileLinkInformation (for file systems that allow cycles to be created in the directory hierarchy)

FilePositionInformation

FileRenameInformation

The following types of information can be set only on files:

FileAllocationInformation

FileEndOfFileInformation

FileLinkInformation (for file systems, such as NTFS, that do not allow cycles to be created in the directory hierarchy)

FileValidDataLengthInformation

## <a href="" id="operation-filter"></a>Operation: File System Filter Drivers


The filter driver must pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set file information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to an input buffer that contains the file or directory information to be set. This information is stored in one of the following structures:

[**FILE\_ALLOCATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540232)

[**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762)

[**FILE\_DISPOSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545765)

[**FILE\_END\_OF\_FILE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545780)

[**FILE\_LINK\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540324)

[**FILE\_POSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545848)

[**FILE\_RENAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540344)

[**FILE\_VALID\_DATA\_LENGTH\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545873)

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter to [**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096).

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_INFORMATION and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_SET\_INFORMATION.

<a href="" id="irpsp--parameters-setfile-advanceonly"></a>*IrpSp-&gt;Parameters.SetFile.AdvanceOnly*
A flag for end-of-file operations. This determines the use of the **EndOfFile** member [**FILE\_END\_OF\_FILE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545780) structure when **FileInformationClass** == **FileEndOfFileInformation**. If **TRUE**, a new valid data length for the file will be set from **EndOfFile** only if it increases the current valid data length. If **FALSE**, a new file size is set from **EndOfFile**.

<a href="" id="irpsp--parameters-setfile-clustercount"></a>*IrpSp-&gt;Parameters.SetFile.ClusterCount*
Reserved for system use.

<a href="" id="irpsp--parameters-setfile-deletehandle"></a>*IrpSp-&gt;Parameters.SetFile.DeleteHandle*
Reserved for system use.

<a href="" id="irpsp--parameters-setfile-fileinformationclass"></a>*IrpSp-&gt;Parameters.SetFile.FileInformationClass*
Specifies the type of information to be set for the file. One of the following:

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
<td align="left"><p><strong>FileAllocationInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_ALLOCATION_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540232) for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileBasicInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_BASIC_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545762) for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileDispositionInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_DISPOSITION_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545765) for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileEndOfFileInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_END_OF_FILE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545780) for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileLinkInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_LINK_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540324) for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FilePositionInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_POSITION_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545848) for the file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileRenameInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_RENAME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540344) for the file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileValidDataLengthInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_VALID_DATA_LENGTH_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545873) for the file.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--parameters-setfile-fileobject"></a>*IrpSp-&gt;Parameters.SetFile.FileObject*
For rename or link operations. If *Irp-&gt;AssociatedIrp.SystemBuffer-&gt;FileName* contains a fully qualified file name, or if *Irp-&gt;AssociatedIrp.SystemBuffer-&gt;RootDirectory* is non-**NULL**, this member is a file object pointer for the parent directory of the file that is the target of the operation. Otherwise it is **NULL**.

<a href="" id="irpsp--parameters-setfile-length"></a>*IrpSp-&gt;Parameters.SetFile.Length*
Length, in bytes, of the buffer pointed to by *Irp-&gt;AssociatedIrp.SystemBuffer*.

<a href="" id="irpsp--parameters-setfile-replaceifexists"></a>*IrpSp-&gt;Parameters.SetFile.ReplaceIfExists*
Set to **TRUE** to specify that if a file with the same name already exists, it should be replaced with the given file. Set to **FALSE** if the rename operation should fail if a file with the given name already exists.

Remarks
-------

The **AdvanceOnly** member is set to **TRUE** by the cache manager to notify the file system to advance the current valid data length on the disk to the new valid data length in **EndOfFile**. If **AdvanceOnly** is **FALSE**, a new file size, in the **EndOfFile** member, is being set which can be larger or smaller than the current file size.

## See also


[**FILE\_ALLOCATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540232)

[**FILE\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545762)

[**FILE\_DISPOSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545765)

[**FILE\_END\_OF\_FILE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545780)

[**FILE\_LINK\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540324)

[**FILE\_POSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545848)

[**FILE\_RENAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540344)

[**FILE\_VALID\_DATA\_LENGTH\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545873)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20IRP_MJ_SET_INFORMATION%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





