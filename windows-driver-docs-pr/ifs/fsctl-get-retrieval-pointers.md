---
title: FSCTL_GET_RETRIEVAL_POINTERS control code
description: The FSCTL_GET_RETRIEVAL_POINTERS control code retrieves a variably sized data structure that describes the allocation and location on disk of a specific file.
keywords: ["FSCTL_GET_RETRIEVAL_POINTERS control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_RETRIEVAL_POINTERS
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_GET_RETRIEVAL_POINTERS control code

The **FSCTL_GET_RETRIEVAL_POINTERS** control code retrieves a variably sized data structure that describes the allocation and location on disk of a specific file. The structure describes the mapping between virtual cluster numbers (VCN, offsets within the file/stream space) and logical cluster numbers (LCN, offsets within the volume space).

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

For more information about reparse points and the FSCTL_GET_RETRIEVAL_POINTERS control code, see the Microsoft Windows SDK documentation.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the alternate stream, file, or directory for which FSCTL_GET_RETRIEVAL_POINTERS retrieves a mapping. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the alternate stream, file, or directory for which FSCTL_GET_RETRIEVAL_POINTERS retrieves a mapping. If the value in *FileHandle* is the handle for an entire volume, the routine returns a map of the VCNs and extents for the bad clusters file. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: The control code for the operation. Use FSCTL_GET_RETRIEVAL_POINTER for this operation.

- **InputBuffer** [in]: A pointer to a [**STARTING_VCN_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-starting_vcn_input_buffer) structure that indicates the virtual cluster number (VCN) that marks the beginning of the alternate stream, file, or directory. **StartingVcn** is the VCN at which FSCTL_GET_RETRIEVAL_POINTERS begins enumerating extents and the associated virtual and logical cluster numbers. On the first call to [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with a file system control code of FSCTL_GET_RETRIEVAL_POINTERS, **StartingVcn** should be set to zero.

  If **OutputBuffer** is not large enough to hold the entire map of VCNs and extents for the file, the caller must request more map data by using the value returned in the **NextVcn** member of the [**RETRIEVAL_POINTERS_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-retrieval_pointers_buffer) structure as the starting VCN.

- **InputBufferLength** [in]: Length, in bytes, of the input buffer at ***InputBuffer**.*

- **OutputBuffer** [out]: A pointer to a variably sized structure of type [**RETRIEVAL_POINTERS_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-retrieval_pointers_buffer) that contains an enumeration of the extents on the disk that correspond to the alternate stream, file, or directory.

- **OutputBufferLength** [out]: Size, in bytes, of the buffer pointed to by the **OutputBuffer** parameter.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) and [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) both return STATUS_SUCCESS or an appropriate NTSTATUS error value.

If the VCN / extents map does not fit in *OutputBuffer*, both routines return a value of STATUS_BUFFER_OVERFLOW, and the caller must request more map data using the value returned in the **NextVcn** member of the RETRIEVAL_POINTERS_BUFFER structure as the starting VCN (**StartingVcn**) in the next call to [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)).

If the value that is specified in **StartingVcn** is beyond the end of the file, STATUS_END_OF_FILE is returned.

## Remarks

The **FSCTL_GET_RETRIEVAL_POINTERS** control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
