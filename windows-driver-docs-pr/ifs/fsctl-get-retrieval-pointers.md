---
title: FSCTL_GET_RETRIEVAL_POINTERS control code
description: The FSCTL\_GET\_RETRIEVAL\_POINTERS control code retrieves a variably sized data structure that describes the allocation and location on disk of a specific file.
ms.assetid: d77790c8-9fe6-4b36-995e-40a7ea54c18a
keywords: ["FSCTL_GET_RETRIEVAL_POINTERS control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_RETRIEVAL_POINTERS
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_GET\_RETRIEVAL\_POINTERS control code


The **FSCTL\_GET\_RETRIEVAL\_POINTERS** control code retrieves a variably sized data structure that describes the allocation and location on disk of a specific file. The structure describes the mapping between virtual cluster numbers (VCN, offsets within the file/stream space) and logical cluster numbers (LCN, offsets within the volume space).

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

For more information about reparse points and the FSCTL\_GET\_RETRIEVAL\_POINTERS control code, see the Microsoft Windows SDK documentation.

**Parameters**

<a href="" id="fileobject"></a>*FileObject*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. A file object pointer for the alternate stream, file, or directory for which FSCTL\_GET\_RETRIEVAL\_POINTERS retrieves a mapping. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle"></a>*FileHandle*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. A file handle for the alternate stream, file, or directory for which FSCTL\_GET\_RETRIEVAL\_POINTERS retrieves a mapping. If the value in *FileHandle* is the handle for an entire volume, the routine returns a map of the VCNs and extents for the bad clusters file. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode"></a>*FsControlCode*  
The control code for the operation. Use FSCTL\_GET\_RETRIEVAL\_POINTER for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to a STARTING\_VCN\_INPUT\_BUFFER structure that indicates the virtual cluster number (VCN) that marks the beginning of the alternate stream, file, or directory. The STARTING\_VCN\_INPUT\_BUFFER structure is defined as follows:

```cpp
typedef struct {
  LARGE_INTEGER  ;
} STARTING_VCN_INPUT_BUFFER, *PSTARTING_VCN_INPUT_BUFFER;
```

**Members**

<a href="" id="startingvcn"></a>**StartingVcn**  
The VCN at which FSCTL\_GET\_RETRIEVAL\_POINTERS begins enumerating extents and the associated virtual and logical cluster numbers. On the first call to [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with a file system control code of FSCTL\_GET\_RETRIEVAL\_POINTERS, **StartingVcn** should be set to zero.

If *OutputBuffer* is not large enough to hold the entire map of VCNs and extents for the file, the caller must request more map data by using the value returned in the **NextVcn** member of the RETRIEVAL\_POINTERS\_BUFFER structure as the starting VCN.

<a href="" id="inputbufferlength"></a>*InputBufferLength*  
Length, in bytes, of the input buffer at *InputBuffer.*

<a href="" id="outputbuffer"></a>*OutputBuffer*  
A pointer to a variably sized structure of type RETRIEVAL\_POINTERS\_BUFFER that contains an enumeration of the extents on the disk that correspond to the alternate stream, file, or directory:

```cpp
typedef struct RETRIEVAL_POINTERS_BUFFER {
 ULONG  ExtentCount;
  LARGE_INTEGER  StartingVcn;
 struct {
    LARGE_INTEGER  NextVcn;
    LARGE_INTEGER  Lcn;
  } Extents[1];
} RETRIEVAL_POINTERS_BUFFER, *PRETRIEVAL_POINTERS_BUFFER;
```

**Members**

<a href="" id="extentcount"></a>**ExtentCount**  
Count of elements in the **Extents** array.

<a href="" id="startingvcn"></a>**StartingVcn**  
Starting VCN returned by the function call. This is not necessarily the VCN requested by the function call, as the file system driver might round down to the first VCN of the extent in which the requested starting VCN is found.

<a href="" id="extents-"></a>**Extents**   
Array of extents structures. For the number of members in the array, see **ExtentCount**. Each member of the array has the following members.

<a href="" id="nextvcn"></a>**NextVcn**  
The VCN at which the next extent begins. This value minus either **StartingVcn** (for the first **Extents** array member) or the **NextVcn** of the previous member of the array (for all other **Extents** array members) is the length, in clusters, of the current extent.

<a href="" id="lcn"></a>**Lcn**  
The LCN at which the current extent begins on the volume. On NTFS, the value (LONGLONG) -1 indicates either a compression unit that is partially allocated, or an unallocated region of a sparse file.

<a href="" id="outputbufferlength"></a>*OutputBufferLength*  
Size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) both return STATUS\_SUCCESS or an appropriate NTSTATUS error value.

If the VCN / extents map does not fit in *OutputBuffer*, both routines return a value of STATUS\_BUFFER\_OVERFLOW, and the caller must request more map data using the value returned in the **NextVcn** member of the RETRIEVAL\_POINTERS\_BUFFER structure as the starting VCN (**StartingVcn**) in the next call to [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462).

If the value that is specified in **StartingVcn** is beyond the end of the file, STATUS\_END\_OF\_FILE is returned.

Remarks
-------

The **FSCTL\_GET\_RETRIEVAL\_POINTERS** control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

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

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






