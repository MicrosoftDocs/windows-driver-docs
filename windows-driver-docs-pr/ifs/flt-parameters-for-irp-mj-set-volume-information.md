---
title: FLT\_PARAMETERS for IRP\_MJ\_SET\_VOLUME\_INFORMATION union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_SET\_VOLUME\_INFORMATION.
ms.assetid: 316ce14c-02ea-45ab-8a2f-1b096f631d23
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_VOLUME_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
---

# FLT\_PARAMETERS for IRP\_MJ\_SET\_VOLUME\_INFORMATION union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](irp-mj-set-volume-information.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                  Length;
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
    PVOID                                  VolumeBuffer;
  } SetVolumeInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**SetVolumeInformation**  
Structure containing the following members.

**Length**  
Length, in bytes, of the buffer at **VolumeBuffer**.

**FsInformationClass**  
Type of information to be set for the volume. One of the following:

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
<td align="left"><p>Set [<strong>FILE_FS_CONTROL_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540258) for the volume.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>FileFsLabelInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_FS_LABEL_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540271) for the volume.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>FileFsObjectIdInformation</strong></p></td>
<td align="left"><p>Set [<strong>FILE_FS_OBJECTID_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540274) for the volume.</p></td>
</tr>
</tbody>
</table>

 

**VolumeBuffer**  
Pointer to the input buffer that contains the values of the volume information to be set.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](irp-mj-set-volume-information.md) operations contains the parameters for a set-volume-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_SET\_VOLUME\_INFORMATION is an IRP-based operation.

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


[**FILE\_FS\_CONTROL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540258)

[**FILE\_FS\_LABEL\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540271)

[**FILE\_FS\_OBJECTID\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540274)

[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](irp-mj-set-volume-information.md)

[**ZwSetVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567112)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_SET_VOLUME_INFORMATION%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





