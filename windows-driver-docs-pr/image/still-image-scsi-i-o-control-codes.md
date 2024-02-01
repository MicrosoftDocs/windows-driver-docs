---
title: Still Image SCSI I/O Control Codes
description: Still image SCSI I/O control codes
ms.date: 05/04/2023
---

# Still image SCSI I/O control codes

The following table lists and describes all of the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

| I/O control code | Description |
|--|--|
| [**IOCTL_SCSISCAN_CMD**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_cmd) | Creates a customized SCSI control descriptor block and sends it to the kernel-mode still image driver for SCSI buses. |
| [**IOCTL_SCSISCAN_GET_INFO**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_get_info) | Returns device information. |
| [**IOCTL_SCSISCAN_LOCKDEVICE**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_lockdevice) | Reserved for use by Microsoft. |
| [**IOCTL_SCSISCAN_SET_TIMEOUT**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_set_timeout) | Modifies the time-out value used by the kernel-mode still image driver for SCSI buses when it accesses a device. |
| [**IOCTL_SCSISCAN_UNLOCKDEVICE**](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_unlockdevice) | Reserved for use by Microsoft. |

These codes are defined in *scsiscan.h*.
