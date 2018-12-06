---
title: FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE.
ms.assetid: 1de62b03-4073-40d6-9094-609431e19e5b
keywords: ["FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT\_PARAMETERS for IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE union


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE.

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    LARGE_INTEGER             FileOffset;
    ULONG                     Length;
    ULONG POINTER_ALIGNMENT   LockKey;
    BOOLEAN POINTER_ALIGNMENT CheckForReadOperation;
  } FastIoCheckIfPossible;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**FastIoCheckIfPossible**  
Structure containing the following members.

**FileOffset**  
Starting byte offset within the cached file.

**Length**  
Length, in bytes, of the data to be read or written.

**LockKey**  
Key value associated with a byte-range lock on the target file. If the range to be read or written overlaps or is a subrange of a nonexclusively locked range within the file, this parameter must be the key for that shared lock. The shared lock must be held by the parent process of the calling thread; otherwise, this parameter is ignored.

**CheckForReadOperation**  
Specifies whether this operation is to check for a read or write operation. It is set to **TRUE** for a read operation and **FALSE** for a write operation.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE operations contains the parameters for a **FastIoCheckIfPossible** operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE is a fast I/O operation.

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


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FsRtlAreThereCurrentFileLocks**](https://msdn.microsoft.com/library/windows/hardware/ff545697)

[**FsRtlCopyRead**](https://msdn.microsoft.com/library/windows/hardware/ff545791)

[**FsRtlCopyWrite**](https://msdn.microsoft.com/library/windows/hardware/ff545797)

 

 






