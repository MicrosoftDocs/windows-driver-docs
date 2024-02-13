---
title: FSCTL_DISMOUNT_VOLUME Control Code
description: The FSCTL_DISMOUNT_VOLUME control code attempts to dismount a volume regardless of whether the volume is in use.
keywords: ["FSCTL_DISMOUNT_VOLUME control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_DISMOUNT_VOLUME
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_DISMOUNT_VOLUME control code

The **FSCTL_DISMOUNT_VOLUME** control code attempts to dismount a volume regardless of whether the volume is in use.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

- **FileObject**: [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object specifying the volume to be dismounted. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle of the volume to be dismounted. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: Control code for the operation. Use **FSCTL_DISMOUNT_VOLUME** for this operation.

- **InputBuffer** [in]: None. Set to NULL.

- **InputBufferLength** [in]: Set to 0.

- **OutputBuffer** [out]: None. Set to NULL.

- **OutputBufferLength** [out]: Set to 0.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS or an appropriate NTSTATUS value.

## Remarks

The **FSCTL_DISMOUNT_VOLUME** control code will attempt to dismount a volume regardless of whether any other processes are using the volume, which can have unpredictable results for those processes if they do not hold a lock on the volume. For information about locking a volume, see [**FSCTL_LOCK_VOLUME**](/windows/win32/api/winioctl/ni-winioctl-fsctl_lock_volume).

The operating system does not detect unmounted volumes. If an attempt is made to access an unmounted volume, the operating system then tries to mount the volume. For example, a call to [**GetLogicalDrives**](/windows/win32/api/fileapi/nf-fileapi-getlogicaldrives) triggers the operating system to mount unmounted volumes.

The **FileHandle** handle passed to [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) must be a handle to a volume, opened for direct access. To retrieve a volume handle, call [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) with the *ObjectAttributes* parameter set to an *ObjectName* of the following form: *\\\\.\\X:* where *X* is a drive letter of the volume, floppy disk drive, or CD-ROM drive. The application must also specify the FILE_SHARE_READ and FILE_SHARE_WRITE flags in the *ShareAccess* parameter of **ZwCreateFile**.

If the specified volume is a system volume or contains a page file, the operation fails.

If the specified volume is locked by another process, the operation fails.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltCreateFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefile)

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
