---
title: FSCTL\_QUERY\_RETRIEVAL\_POINTERS control code
description: The FSCTL\_QUERY\_RETRIEVAL\_POINTERS control code retrieves a mapping between virtual cluster numbers (VCN, offsets within the file/stream space) and logical cluster numbers (LCN, offsets within the volume space), starting at the beginning of the file up to the map size specified in InputBuffer.
ms.assetid: 463a5cb9-d4eb-42d6-9103-956b45a5abfb
keywords: ["FSCTL_QUERY_RETRIEVAL_POINTERS control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_QUERY_RETRIEVAL_POINTERS
api_location:
- Ntifs.h
api_type:
- HeaderDef
---

# FSCTL\_QUERY\_RETRIEVAL\_POINTERS control code


The **FSCTL\_QUERY\_RETRIEVAL\_POINTERS** control code retrieves a mapping between virtual cluster numbers (VCN, offsets within the file/stream space) and logical cluster numbers (LCN, offsets within the volume space), starting at the beginning of the file up to the map size specified in *InputBuffer*.

**FSCTL\_QUERY\_RETRIEVAL\_POINTERS** is similar to [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](fsctl-get-retrieval-pointers.md). However, **FSCTL\_QUERY\_RETRIEVAL\_POINTERS** only works in kernel mode on local paging files or the system hives. The paging file is guaranteed to have a one-to-one mapping from the VCN in a volume to the LCN that refer more directly to the underlying physical storage. You must not use **FSCTL\_QUERY\_RETRIEVAL\_POINTERS** with files other than the page file, because they might reside on volumes, such as mirrored volumes, that have one-to-many mappings of VCNs to LCNs.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the paging file or hibernation file. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A file handle for the paging file or hibernation file. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use FSCTL\_GET\_RETRIEVAL\_POINTERS for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A user-supplied buffer that contains a pointer to a quadlet that specifies the map size. The map size is the number of clusters to map.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Length, in bytes, of the input buffer at *InputBuffer*.

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a buffer of paged pool memory that contains an array of elements of the following type:

```
struct {
 LONGLONG  SectorLengthInBytes;
 LONGLONG  StartingLogicalOffsetInBytes;
  } MappingPair;
```

This array of quadlet pairs defines the disk runs of the file. The value of the **SectorLengthInBytes** member in the last element of the array is zero.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
The size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) both return STATUS\_SUCCESS or an appropriate NTSTATUS error value.

Remarks
-------

**ReFS:  **This code is not supported.

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

## See also


[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**FSCTL\_GET\_RETRIEVAL\_POINTERS**](fsctl-get-retrieval-pointers.md)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FSCTL_QUERY_RETRIEVAL_POINTERS%20control%20code%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





