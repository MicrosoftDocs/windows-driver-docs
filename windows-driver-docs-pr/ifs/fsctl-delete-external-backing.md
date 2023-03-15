---
title: FSCTL_DELETE_EXTERNAL_BACKING control code
description: The FSCTL_DELETE_EXTERNAL_BACKING control code removes the association of a file with an external backing provider, including the Windows Image Format (WIM) provider or compressed file provider.
keywords: ["FSCTL_DELETE_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DELETE_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_DELETE_EXTERNAL_BACKING control code

The **FSCTL_DELETE_EXTERNAL_BACKING** control code removes the association of a file with an external backing provider, including the Windows Image Format (WIM) provider or compressed file provider. As a result of this operation, the entire contents of a backed file are read, decompressed, and written into the file.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

- **FileObject**: [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object of the file for which backing association is deleted. This parameter is required and cannot be NULL.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The handle of the file for which backing association is deleted. This parameter is required and cannot be NULL.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_DELETE_EXTERNAL_BACKING** for this operation.

- **InputBuffer** [in]: None. Set to NULL.

- **InputBufferLength** [in]: Set to 0.

- **OutputBuffer** [out]: None. Set to NULL.

- **OutputBufferLength** [out]: Set to 0.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

| Code | Meaning |
| ---- | ------- |
| STATUS_OBJECT_NOT_EXTERNALLY_BACKED | The file is not externally backed. |
| STATUS_INVALID_DEVICE_REQUEST | The backing service is not present or not started. |
| STATUS_ACCESS_DENIED | The requestor does not have permission to delete the backing associations for the file. |

## Remarks

As a result of the delete operation, the contents of the file are read from the backing source and the entire file is written to the volume.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8.1 Update |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

[**FSCTL_SET_EXTERNAL_BACKING**](fsctl-set-external-backing.md)
