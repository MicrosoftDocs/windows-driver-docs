---
title: Still Image SCSI I/O Structures
description: Still image SCSI I/O structures
ms.date: 05/04/2023
---

# Still image SCSI I/O structures

The following table lists and describes all of the structures associated with the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

| Structure | Description |
|--|--|
| [**SCSISCAN_CMD**](/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_cmd) | Used as a parameter to [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), when the specified I/O control code is [**IOCTL_SCSISCAN_CMD**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_cmd). |
| [**SCSISCAN_INFO**](/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_info) | Used as a parameter to "[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol), when the specified I/O control code is "[**IOCTL_SCSISCAN_GET_INFO**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_get_info). |

These structures are defined in *scsiscan.h*.
