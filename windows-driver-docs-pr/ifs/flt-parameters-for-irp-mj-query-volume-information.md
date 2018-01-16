---
title: FLT\_PARAMETERS for IRP\_MJ\_QUERY\_VOLUME\_INFORMATION union
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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Return a [<strong>FILE_FS_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540287) that contains information about the volume, such as the volume label, serial number, and creation time.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefscontrolinformation"></a>
<strong>FileFsControlInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_CONTROL_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540258) structure that contains file system control information about the volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefsdeviceinformation"></a>
<strong>FileFsDeviceInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_DEVICE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545788) structure that contains device information for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsdriverpathinformation"></a>
<strong>FileFsDriverPathInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_DRIVER_PATH_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540262) structure that contains information about whether a specified driver is in the I/O path for the volume. The originator of the IRP_MJ_QUERY_VOLUME_INFORMATION request must store the name of the driver into the FILE_FS_DRIVER_PATH_INFORMATION structure before sending the IRP to the file system volume device stack.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefsfullsizeinformation"></a>
<strong>FileFsFullSizeInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_FULL_SIZE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540267) structure that contains information about the total amount of space available on the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsobjectidinformation"></a>
<strong>FileFsObjectIdInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_OBJECTID_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540274) structure that contains file-system-specific object ID information for the volume. Note that this is not the same as the (globally unique identifier [GUID]-based) unique volume name that the operating system assigns.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefssizeinformation"></a>
<strong>FileFsSizeInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_SIZE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540282) structure that contains information about the amount of space on the volume that is available to the user associated with the thread that originated the IRP_MJ_QUERY_VOLUME_INFORMATION request.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="" id="filefsvolumeinformation"></a>
<strong>FileFsVolumeInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_VOLUME_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540287) that contains information about the volume, such as the volume label, serial number, and creation time.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="" id="filefssectorsizeinformation"></a>
<strong>FileFsSectorSizeInformation</strong></td>
<td align="left"><p>Return a [<strong>FILE_FS_SECTOR_SIZE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540262) structure that contains information about the physical and logical sector sizes of a volume.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_QUERY_VOLUME_INFORMATION%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





