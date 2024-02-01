---
title: FSCTL_REQUEST_OPLOCK Control Code
description: The FSCTL_REQUEST_OPLOCK control code requests an opportunistic lock (oplock) on a file, or acknowledges that an oplock break has occurred.
keywords: ["FSCTL_REQUEST_OPLOCK control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_REQUEST_OPLOCK
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_REQUEST_OPLOCK control code

The **FSCTL_REQUEST_OPLOCK** control code requests an opportunistic lock (oplock) on a file, or acknowledges that an oplock break has occurred.

For more information about opportunistic locks, see [Opportunistic Locks](/windows/desktop/FileIO/opportunistic-locks) in the Windows Desktop documentation. For more information about user mode OPLOCK controls, see [File Management Control Codes](/windows/desktop/FileIO/file-management-control-codes) in the Windows Desktop documentation.

To process this control code, a file system or filter driver calls [**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex) with the following parameters.

## Parameters

- **Oplock**: Opaque oplock object pointer for the file.

- **Irp**: A pointer to the IRP for an IRP_MJ_FILE_SYSTEM_CONTROL FSCTL request. The **FsControlCode** parameter for the operation must be FSCTL_REQUEST_OPLOCK.

- **OpenCount**: The number of user handles for the file if the request is for an exclusive oplock. If the request is for an oplock that can be shared, *OpenCount* is zero if no byte-range locks exist on the file. Otherwise, **OpenCount** is nonzero. The caller can call the [**FsRtlOplockIsSharedRequest**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockissharedrequest) routine on the IRP to determine if the request is for an oplock that can be shared.

- **Flags**: A bitmask for the associated oplock operations. A file system or filter driver sets bits to specify the behavior of [**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex). The *Flags* parameter has the following options:

  | Value | Meaning |
  | ----- | ------- |
  | OPLOCK_FSCTRL_FLAG_ALL_KEYS_MATCH (0x00000001) | Specifies that the file system has verified that all opportunistic lock keys match on any handle that is currently open. By specifying this flag, the oplock package can grant an oplock of level RW or RWH when more than one open handle to the file exists. For more information about oplock types, see [Overview](./oplock-overview.md). |

## Status block

[**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex) returns one of the following NTSTATUS values for this operation:

| Code | Meaning |
| ---- | ------- |
| STATUS_PENDING | The oplock was granted. This is a success code. |
| STATUS_CANCELLED | The IRP was canceled before the FSCTL_REQUEST_OPLOCK operation was completed. This is an error code. |
| STATUS_OPLOCK_NOT_GRANTED | The oplock could not be granted. This is an error code. |

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FsRtlOplockFsctrlEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockfsctrlex)

[**FsRtlOplockIsSharedRequest**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtloplockissharedrequest)

[**IRP_MJ_FILE_SYSTEM_CONTROL**](irp-mj-file-system-control.md)
