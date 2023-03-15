---
title: FSCTL_GET_BOOT_AREA_INFO control code
description: The FSCTL_GET_BOOT_AREA_INFO control code retrieves the locations of boot sectors for a volume.
keywords: ["FSCTL_GET_BOOT_AREA_INFO control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_BOOT_AREA_INFO
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_GET_BOOT_AREA_INFO control code

The **FSCTL_GET_BOOT_AREA_INFO** control code retrieves the locations of boot sectors for a volume.

To perform this operation, call the [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) function or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) function with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the volume for which **FSCTL_GET_BOOT_AREA_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A file handle for the volume for which **FSCTL_GET_BOOT_AREA_INFO** will retrieve the boot information. This parameter is required and cannot be **NULL**.

  This handle must be opened with the SE_MANAGE_VOLUME_NAME access rights. For more information, see [File Security and Access Rights](/windows/desktop/FileIO/file-security-and-access-rights).

- **FsControlCode** [in]: A control code for the operation. Use **FSCTL_GET_BOOT_AREA_INFO** for this operation.

- **InputBuffer** [in]: Not used with this operation. Set to **NULL**.

- **InputBufferLength** [in]: Not used with this operation. Set to zero.

- **OutputBuffer** [out]: A pointer to a [**BOOT_AREA_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_boot_area_info) structure, which receives the location of the volume's boot sectors.

- **OutputBufferLength** [out]: The size of the output buffer, in bytes.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns an appropriate NTSTATUS value such as one of the following:

| Code | Meaning |
| ---- | ------- |
| STATUS_SUCCESS | The operation was successful. OutputBuffer contains a pointer to a [**BOOT_AREA_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_boot_area_info) structure. |
| STATUS_INVALID_PARAMETER | A parameter was not valid; for example, the handle used is not a valid volume handle. |
| STATUS_BUFFER_TOO_SMALL | OutputBuffer is not large enough for the result. No information has been written to the buffer. |
| STATUS_ACCESS_DENIED | The user does not have SE_MANAGE_VOLUME access. |

## Remarks

**FSCTL_GET_BOOT_AREA_INFO** control code can be used on FastFAT and exFAT devices. This capability supports the use of BitLocker for devices such as flash drives.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 7 |
| Minimum supported server | Windows Server 2008 R2 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)
