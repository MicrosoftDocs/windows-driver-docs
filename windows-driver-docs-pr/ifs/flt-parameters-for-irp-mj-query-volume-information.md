---
title: FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_QUERY\_VOLUME\_INFORMATION.
ms.assetid: fc790885-a378-40dc-829d-94e75a7c6f13
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_QUERY\_VOLUME\_INFORMATION union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](irp-mj-query-volume-information.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                  Length;
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
  } QueryVolumeInformation;
  PVOID  VolumeBuffer;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**QueryVolumeInformation**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer at **VolumeBuffer**.

**FsInformationClass**  
Type of volume information that the file system returns. One of the following:

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
<td align="left"><a href="" id="filefsattributeinformation"></a>
<strong>FileFsAttributeInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540287" data-raw-source="[&lt;strong&gt;FILE_FS_VOLUME_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540287)"><strong>FILE_FS_VOLUME_INFORMATION</strong></a> that contains information about the volume, such as the volume label, serial number, and creation time.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefscontrolinformation"></a>
<strong>FileFsControlInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258" data-raw-source="[&lt;strong&gt;FILE_FS_CONTROL_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540258)"><strong>FILE_FS_CONTROL_INFORMATION</strong></a> structure that contains file system control information about the volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefsdeviceinformation"></a>
<strong>FileFsDeviceInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545788" data-raw-source="[&lt;strong&gt;FILE_FS_DEVICE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545788)"><strong>FILE_FS_DEVICE_INFORMATION</strong></a> structure that contains device information for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsdriverpathinformation"></a>
<strong>FileFsDriverPathInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540262" data-raw-source="[&lt;strong&gt;FILE_FS_DRIVER_PATH_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540262)"><strong>FILE_FS_DRIVER_PATH_INFORMATION</strong></a> structure that contains information about whether a specified driver is in the I/O path for the volume. The originator of the IRP_MJ_QUERY_VOLUME_INFORMATION request must store the name of the driver into the FILE_FS_DRIVER_PATH_INFORMATION structure before sending the IRP to the file system volume device stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefsfullsizeinformation"></a>
<strong>FileFsFullSizeInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540267" data-raw-source="[&lt;strong&gt;FILE_FS_FULL_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540267)"><strong>FILE_FS_FULL_SIZE_INFORMATION</strong></a> structure that contains information about the total amount of space available on the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsobjectidinformation"></a>
<strong>FileFsObjectIdInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274" data-raw-source="[&lt;strong&gt;FILE_FS_OBJECTID_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540274)"><strong>FILE_FS_OBJECTID_INFORMATION</strong></a> structure that contains file-system-specific object ID information for the volume. Note that this is not the same as the (globally unique identifier [GUID]-based) unique volume name that the operating system assigns.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefssizeinformation"></a>
<strong>FileFsSizeInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540282" data-raw-source="[&lt;strong&gt;FILE_FS_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540282)"><strong>FILE_FS_SIZE_INFORMATION</strong></a> structure that contains information about the amount of space on the volume that is available to the user associated with the thread that originated the IRP_MJ_QUERY_VOLUME_INFORMATION request.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsvolumeinformation"></a>
<strong>FileFsVolumeInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540287" data-raw-source="[&lt;strong&gt;FILE_FS_VOLUME_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540287)"><strong>FILE_FS_VOLUME_INFORMATION</strong></a> that contains information about the volume, such as the volume label, serial number, and creation time.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefssectorsizeinformation"></a>
<strong>FileFsSectorSizeInformation</strong></td>
<td align="left"><p>Return a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540262" data-raw-source="[&lt;strong&gt;FILE_FS_SECTOR_SIZE_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540262)"><strong>FILE_FS_SECTOR_SIZE_INFORMATION</strong></a> structure that contains information about the physical and logical sector sizes of a volume.</p></td>
</tr>
</tbody>
</table>

 

**VolumeBuffer**  
Pointer to the output buffer where the volume information is to be returned.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_QUERY\_VOLUME\_INFORMATION operations contains the parameters for an IRP-based query-volume-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_QUERY\_VOLUME\_INFORMATION is an IRP-based operation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

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

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**ZwQueryVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567070)

 

 






