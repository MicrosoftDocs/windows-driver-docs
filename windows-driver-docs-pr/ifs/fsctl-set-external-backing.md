---
title: FSCTL\_SET\_EXTERNAL\_BACKING control code
description: The FSCTL\_SET\_EXTERNAL\_BACKING control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider.
ms.assetid: 5CB9FD4D-AF29-4438-B0B5-49871102968A
keywords: ["FSCTL_SET_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_SET\_EXTERNAL\_BACKING control code


The **FSCTL\_SET\_EXTERNAL\_BACKING** control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider. Content for externally backed files may be sourced on volumes other than on volume where the file resides.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the file for which backing is set. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the file for which backing is set. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_SET\_EXTERNAL\_BACKING** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which contains [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by the provider data. For WIM backed files, **WOF\_EXTERNAL\_INFO** is followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Size of the data provided in the *InputBuffer*.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
None. Set to NULL.

<a href="" id="outputbufferlength--in-"></a>*OutputBufferLength \[in\]*  
Set to 0.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate NTSTATUS values is returned.

Remarks
-------

When the backing provider for the data source added is the WIM provider, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF\_EXTERNAL\_INFO**) + **sizeof**(**WIM\_PROVIDER\_EXTERNAL\_INFO**).

Individually compressed files offer good compression for data which will not be modified, including executable files. If these are opened for write the file will be transparently decompressed. To specify an individually compressed file,, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**](https://msdn.microsoft.com/library/windows/hardware/mt426732) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF\_EXTERNAL\_INFO**) + **sizeof**(**FILE\_PROVIDER\_EXTERNAL\_INFO\_V1**). Individual compressed files are available starting with Windows 10.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting with Windows 8.1 Update.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

[**FSCTL\_DELETE\_EXTERNAL\_BACKING**](fsctl-delete-external-backing.md)

[**FSCTL\_GET\_EXTERNAL\_BACKING**](fsctl-get-external-backing.md)

[**WIM\_PROVIDER\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632448)

[**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_SET_EXTERNAL_BACKING%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





