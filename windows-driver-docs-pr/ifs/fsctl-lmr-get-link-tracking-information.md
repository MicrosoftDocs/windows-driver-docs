---
title: FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION control code
description: The FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION control code retrieves the link tracking information for a file.
ms.assetid: 8ddb8aca-4998-47ed-b8c9-39219e342c2c
keywords: ["FSCTL_LMR_GET_LINK_TRACKING_INFORMATION control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_LMR_GET_LINK_TRACKING_INFORMATION
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION control code


The **FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION** control code retrieves the link tracking information for a file.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the remote volume. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A handle for the remote volume. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
A control code for the operation. Use **FSCTL\_LMR\_GET\_LINK\_TRACKING\_INFORMATION** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
None.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Not used.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A **LINK\_TRACKING\_INFORMATION** structure that contains the link tracking information of the file.

``` syntax
typedef struct _LINK_TRACKING_INFORMATION {
  LINK_TRACKING_INFORMATION_TYPE  Type;
  UCHAR  VolumeId[16];
} LINK_TRACKING_INFORMATION, *PLINK_TRACKING_INFORMATION;
```

<a href="" id="type"></a>**Type**  
A **LINK\_TRACKING\_INFORMATION\_TYPE** information enumeration value that specifies the type of file system that the file resides on. If this member holds a value of **DfsLinkTrackingInformation**, the file resides on a distributed file system. If this member holds a value of **NtfsLinkTrackingInformation**, the file resides on an NTFS file system.

<a href="" id="volumeid"></a>**VolumeId**  
An unsigned character array that holds the volume identifier.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function returns the appropriate NTSTATUS error code.

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
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_LMR_GET_LINK_TRACKING_INFORMATION%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




