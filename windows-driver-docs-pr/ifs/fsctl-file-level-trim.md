---
title: FSCTL_FILE_LEVEL_TRIM Control Code
description: The FSCTL_FILE_LEVEL_TRIM control code provides a method to trim data ranges with in a file.
keywords: ["FSCTL_FILE_LEVEL_TRIM control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_FILE_LEVEL_TRIM
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_FILE_LEVEL_TRIM control code

The **FSCTL_FILE_LEVEL_TRIM** control code provides a method to trim data ranges with in a file. The file trim ranges are translated to the underlying storage device allowing it to optimize its resource organization to improve access performance. An **FSCTL_FILE_LEVEL_TRIM** request allows a virtual disk file to remain allocated at a fixed size while trimming physical storage to correspond to data ranges freed on the virtual disk.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file object pointer to the file which has the data to be trimmed. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle of the file which has the data to be trimmed. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use **FSCTL_FILE_LEVEL_TRIM** for this operation.

- **InputBuffer** [in]: A pointer to a [**FILE_LEVEL_TRIM**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim) structure which contains an array of trim ranges for the file.

- **InputBufferLength** [in]: Size, in bytes, of the buffer pointed to by the *InputBuffer* parameter. This value must be at least sizeof([**FILE_LEVEL_TRIM**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim)).

- **OutputBuffer** [out]: A pointer to an optional [**FILE_LEVEL_TRIM_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim) structure which receives the result of the trim operation.

- **OutputBufferLength** [out]: Size, in bytes, of the buffer pointed to by the *OutputBuffer* parameter. This value must be at least **sizeof**([**FILE_LEVEL_TRIM_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim)) if **FILE_LEVEL_TRIM_OUTPUT** is included in *OutputBuffer*. Otherwise, this is set to 0.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or possibly one of the following values.

| Code | Meaning |
| ---- | ------- |
| STATUS_INVALID_PARAMETER | The file to trim is either compressed or encrypted, the input or output buffer length is invalid, or, no trim ranges are specified. |
| STATUS_INSUFFICIENT_RESOURCES | An internal resource allocation failed. |
| STATUS_FILE_LOCK_CONFLICT | A trim range is part of a previously locked byte range. |
| STATUS_VOLUME_DISMOUNTED | The volume where the file resides is not mounted. |
| STATUS_PURGE_FAILED | A cache purge failed for a trim range. |
| STATUS_NO_RANGES_PROCESSED | No ranges in the trim range array were processed. |

## Remarks

Performing trim on certain storage devices can significantly improve their future write performance. Trim also returns resources to the allocation pool in storage systems that are thinly provisioned. When files are deleted on a virtual disk, the size of the virtual disk file itself is not changed. The data ranges freed on the virtual disk are not trimmed on the physical storage where the virtual disk file resides. A virtual disk device can notify the file system that certain data ranges in a virtual disk file can be trimmed on the physical storage device with an **FSCTL_FILE_LEVEL_TRIM** request. The file system will then issue a trim request to the physical storage. An **FSCTL_FILE_LEVEL_TRIM** request could also be issued by service applications managing database or memory swap files.

The **FSCTL_FILE_LEVEL_TRIM** control code will attempt to trim the selected byte ranges of a file from a storage device. The byte ranges are contained in the **Ranges** array in the [**FILE_LEVEL_TRIM**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim) structure. Included in the **Ranges** array are one or more [**FILE_LEVEL_TRIM_RANGE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim_range) structures.

Including overlapping ranges in the range array is not necessarily an error condition. This is dependant on how extent processing is handled by the underlying storage.

Trimmed ranges are purged as pages from the file system cache. In order to match the cache page size, a trim range's length is adjusted down to a multiple of **PAGE_SIZE**. Also, if a trim range offset does not begin at a page boundary, it is aligned to the next page boundary. With these constraints, trim range lengths will reduce when their offsets are not page aligned or lengths are not a page size multiple. A trim range length may reduce to 0 if the original length is less than two pages and the offset is not page aligned.

If a trim range is specified or page adjusted beyond the end-of-file (EOF), the range is ignored. However, a range offset aligned before EOF but having a length extending past EOF will be adjusted to a page size multiple <= EOF.

File level trim is not supported for compressed or encrypted files (files with **ATTRIBUTE_FLAG_COMPRESSION_MASK** or **ATTRIBUTE_FLAG_ENCRYPTED** attributes set).

A file trim is performed outside of any transaction. The trim operation cannot be rolled back.

With sparse files (files with the **ATTRIBUTE_FLAG_SPARSE** attribute set), a trim range in an unallocated portion of the file is ignored.

When included in *OutputBuffer*, the **NumRangesProcessed** member of the [**FILE_LEVEL_TRIM_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim_output) will indicate the number of trim ranges successfully processed. If an error occurs during the processing of the trim ranges, **NumRangesProcessed** will specify the starting index of the remaining unprocessed ranges, ending at the **NumRanges** member of [**FILE_LEVEL_TRIM**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim) - 1.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FILE_LEVEL_TRIM**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim)

[**FILE_LEVEL_TRIM_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim_output)

[**FILE_LEVEL_TRIM_RANGE**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_level_trim_range)

[**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile)

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
