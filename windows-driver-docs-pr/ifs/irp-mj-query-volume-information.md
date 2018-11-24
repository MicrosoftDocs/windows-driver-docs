---
title: IRP_MJ_QUERY_VOLUME_INFORMATION
description: IRP\_MJ\_QUERY\_VOLUME\_INFORMATION
ms.assetid: 1e762c75-70bd-4397-b244-df97b317b3bf
keywords: ["IRP_MJ_QUERY_VOLUME_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_VOLUME_INFORMATION
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_QUERY\_VOLUME\_INFORMATION


## When Sent


The **IRP\_MJ\_QUERY\_VOLUME\_INFORMATION** request is sent by the I/O Manager. It can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **GetDiskFreeSpace** or **GetFileType**.

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine whether the target device object is the file system's control device object. If it is, and if the request has been issued on a handle that is a volume open (or an open of an object on the volume), the file system driver should process the request and complete the IRP.

Otherwise, the file system driver should fail the query and complete the IRP.

The types of volume information that can be queried are file-system-dependent, but generally include the following:

FileFsAttributeInformation

FileFsDeviceInformation

FileFsSizeInformation

FileFsVolumeInformation

For a list of all possible information types, see *IrpSp-&gt;Parameters.QueryVolume.FsInformationClass* below.

## Operation: Network Redirect Drivers


A network redirector that receives a request for FileFsDeviceInformation, must include FILE\_REMOTE\_DEVICE as one of the options for the **DeviceCharacteristics** member of the [**FILE\_FS\_DEVICE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545788) structure returned.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a query volume information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied output buffer where the volume information is to be returned. This information is stored in one of the following structures:

FILE\_FS\_ATTRIBUTE\_INFORMATION

FILE\_FS\_CONTROL\_INFORMATION

FILE\_FS\_DEVICE\_INFORMATION

FILE\_FS\_DRIVER\_PATH\_INFORMATION

FILE\_FS\_FULL\_SIZE\_INFORMATION

FILE\_FS\_OBJECTID\_INFORMATION

FILE\_FS\_SIZE\_INFORMATION

FILE\_FS\_VOLUME\_FLAGS\_INFORMATION

FILE\_FS\_VOLUME\_INFORMATION

FILE\_FS\_SECTOR\_SIZE\_INFORMATION

The FileFsVolumeFlagsInformation class and the associated [**FILE\_FS\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540287) structure are available on Windows Vista and later versions.

<a href="" id="------irp--iostatus"></a> *Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="------irp--userbuffer"></a> *Irp-&gt;UserBuffer*
Optional pointer to a caller-supplied output buffer into which the contents of *Irp-&gt;AssociatedIrp.SystemBuffer* are copied during I/O completion by the I/O manager. Drivers do not use this buffer to return any data for the request.

<a href="" id="------irpsp--fileobject"></a> *IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of **IRP\_MJ\_QUERY\_VOLUME\_INFORMATION** and should not be used.

<a href="" id="------irpsp--majorfunction"></a> *IrpSp-&gt;MajorFunction*
Specifies **IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**.

<a href="" id="------irpsp--parameters-queryvolume-fsinformationclass"></a> *IrpSp-&gt;Parameters.QueryVolume.FsInformationClass*
Specifies the type of volume information to be returned by the file system. This member can be one of the following:

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
<td align="left"><p><strong>FileFsAttributeInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540251" data-raw-source="[&lt;strong&gt;FILE_FS_ATTRIBUTE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540251)"><strong>FILE_FS_ATTRIBUTE_INFORMATION</strong></a> structure that contains attribute information about the file system responsible for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsControlInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258" data-raw-source="[&lt;strong&gt;FILE_FS_CONTROL_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540258)"><strong>FILE_FS_CONTROL_INFORMATION</strong></a> structure that contains file system control information about the volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsDeviceInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545788" data-raw-source="[&lt;strong&gt;FILE_FS_DEVICE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545788)"><strong>FILE_FS_DEVICE_INFORMATION</strong></a> structure that contains device information for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsDriverPathInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540262" data-raw-source="[&lt;strong&gt;FILE_FS_DRIVER_PATH_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540262)"><strong>FILE_FS_DRIVER_PATH_INFORMATION</strong></a> structure that contains information about whether a specified driver is in the I/O path for the volume. The originator of the <strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong> request must store the name of the driver into the <strong>FILE_FS_DRIVER_PATH_INFORMATION</strong> structure before sending the IRP to the file system volume device stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsFullSizeInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540267" data-raw-source="[&lt;strong&gt;FILE_FS_FULL_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540267)"><strong>FILE_FS_FULL_SIZE_INFORMATION</strong></a> structure that contains information about the total amount of space available on the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsObjectIdInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274" data-raw-source="[&lt;strong&gt;FILE_FS_OBJECTID_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540274)"><strong>FILE_FS_OBJECTID_INFORMATION</strong></a> structure that contains file-system-specific object ID information for the volume. Note that this is not the same as the (GUID-based) unique volume name that is assigned by the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsSizeInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540282" data-raw-source="[&lt;strong&gt;FILE_FS_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540282)"><strong>FILE_FS_SIZE_INFORMATION</strong></a> structure containing information about the amount of space on the volume that is available to the user associated with the thread which originated the <strong>IRP_MJ_QUERY_VOLUME_INFORMATION</strong> request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsVolumeInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540287" data-raw-source="[&lt;strong&gt;FILE_FS_VOLUME_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540287)"><strong>FILE_FS_VOLUME_INFORMATION</strong></a> that contains information about the volume such as the volume label, serial number, and creation time.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsSectorSizeInformation</strong></p></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406395" data-raw-source="[&lt;strong&gt;FILE_FS_SECTOR_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406395)"><strong>FILE_FS_SECTOR_SIZE_INFORMATION</strong></a> structure that contains information about the physical and logical sector sizes of a volume.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="------irpsp--parameters-queryvolume-length"></a> *IrpSp-&gt;Parameters.QueryVolume.Length*
Length, in bytes, of the buffer pointed to by *Irp-&gt;UserBuffer*. On return, this variable receives the number of bytes written to the buffer.

## See also


[**FILE\_FS\_ATTRIBUTE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540251)

[**FILE\_FS\_CONTROL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540258)

[**FILE\_FS\_DEVICE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545788)

[**FILE\_FS\_DRIVER\_PATH\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540262)

[**FILE\_FS\_FULL\_SIZE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540267)

[**FILE\_FS\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540274)

**FILE\_FS\_SECTOR\_SIZE\_INFORMATION**
[**FILE\_FS\_SIZE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540282)

[**FILE\_FS\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540287)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](irp-mj-set-volume-information.md)

[**ZwQueryVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567070)

[**ZwSetVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567112)

 

 






