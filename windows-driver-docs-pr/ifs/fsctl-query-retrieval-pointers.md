---
title: FSCTL_QUERY_RETRIEVAL_POINTERS control code
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

```cpp
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

 

 






