---
title: IRP_MJ_SET_VOLUME_INFORMATION
description: IRP\_MJ\_SET\_VOLUME\_INFORMATION
ms.assetid: 7c317e8b-ffa9-47f7-ac53-23b09873fab9
keywords: ["IRP_MJ_SET_VOLUME_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_VOLUME_INFORMATION
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SET\_VOLUME\_INFORMATION


## When Sent


The IRP\_MJ\_SET\_VOLUME\_INFORMATION request is sent by the I/O Manager. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **SetVolumeLabel**.

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether it represents a user volume open. If it does, the file system driver should set the appropriate volume information and complete the IRP. Otherwise, the file system should complete the IRP as appropriate without setting the volume information.

The types of volume information that can be set are file system-dependent, but generally include one or more of the following:

FileFsControlInformation

FileFsLabelInformation

FileFsObjectIdInformation

For a list of all possible information types, see the FS\_INFORMATION\_CLASS enumeration in ntifs.h.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set volume information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to an input buffer that contains the values of the volume information to be set. This information is stored in one of the following structures:

FILE\_FS\_CONTROL\_INFORMATION

FILE\_FS\_LABEL\_INFORMATION

FILE\_FS\_OBJECTID\_INFORMATION

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_VOLUME\_INFORMATION and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_SET\_VOLUME\_INFORMATION.

<a href="" id="irpsp--parameters-setvolume-fsinformationclass"></a>*IrpSp-&gt;Parameters.SetVolume.FsInformationClass*
Specifies the type of information to be set for the volume. This value can be one of the following:

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
<td align="left"><p><strong>FileFsControlInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258" data-raw-source="[&lt;strong&gt;FILE_FS_CONTROL_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540258)"><strong>FILE_FS_CONTROL_INFORMATION</strong></a> for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsLabelInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540271" data-raw-source="[&lt;strong&gt;FILE_FS_LABEL_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540271)"><strong>FILE_FS_LABEL_INFORMATION</strong></a> for the volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsObjectIdInformation</strong></p></td>
<td align="left"><p>Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274" data-raw-source="[&lt;strong&gt;FILE_FS_OBJECTID_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540274)"><strong>FILE_FS_OBJECTID_INFORMATION</strong></a> for the volume.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="irpsp--parameters-setvolume-length"></a>*IrpSp-&gt;Parameters.SetVolume.Length*
Length, in bytes, of the buffer pointed to by *Irp-&gt;AssociatedIrp.SystemBuffer*.

## See also


[**FILE\_FS\_CONTROL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540258)

[**FILE\_FS\_LABEL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540271)

[**FILE\_FS\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540274)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](irp-mj-query-volume-information.md)

[**ZwQueryVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567070)

[**ZwSetVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567112)

 

 






