---
title: FLT_PARAMETERS for IRP_MJ_FAST_IO_CHECK_IF_POSSIBLE union
description: The following union component is used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE.
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


The following union component is used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE.

## Syntax

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

## Members

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

## Remarks

The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE operations contains the parameters for a **FastIoCheckIfPossible** operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT\_IO\_PARAMETER\_BLOCK structure.

IRP\_MJ\_FAST\_IO\_CHECK\_IF\_POSSIBLE is a fast I/O operation.

## Requirements

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


[**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT\_IS\_FASTIO\_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT\_IS\_IRP\_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FsRtlAreThereCurrentFileLocks**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlaretherecurrentfilelocks)

[**FsRtlCopyRead**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopyread)

[**FsRtlCopyWrite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlcopywrite)

 

