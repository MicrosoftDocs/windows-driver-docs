---
title: FSCTL_IS_PATHNAME_VALID control code
description: The FSCTL_IS_PATHNAME_VALID control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on).
keywords: ["FSCTL_IS_PATHNAME_VALID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_IS_PATHNAME_VALID
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_IS_PATHNAME_VALID control code

The **FSCTL_IS_PATHNAME_VALID** control code performs static analysis of the supplied pathname and returns a status value that indicates whether the pathname is well formed (for example, no illegal characters, acceptable path length, and so on). Because this analysis does not consider the content of the volume, it sometimes gives "false positives." In other words, the analysis might indicate that the pathname is well formed, even when it is not. Negative results are more reliable, but are not guaranteed to be correct.

This control code is not supported with fast FAT file systems, and it is not a meaningful operation in NTFS or UDFS. NTFS and UDFS support such a wide variety of codesets that any string is potentially a valid pathname.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. Not used.

- **FileHandle** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. Not used.

- **FsControlCode** [in]: The control code for the operation. Use FSCTL_IS_PATHNAME_VALID for this operation.

- **InputBuffer** [in]: A buffer that contains the NULL-terminated pathname string to check.

- **InputBufferLength** [in]: The length, in bytes, of the pathname.

- **OutputBuffer** [out]: Not used.

- **OutputBufferLength** [out]: Not used.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the pathname is well formed. Otherwise, the routine that is used returns the appropriate NTSTATUS error code.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |
