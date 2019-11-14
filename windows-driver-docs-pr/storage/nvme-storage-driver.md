---
title: NVMe Storage Driver
description: NVMe Storage Driver
ms.assetid: 1c6f78d7-ea00-44d4-95d2-62f5a1c7d568
ms.date: 11/15/2019
ms.localizationpriority: medium
---

# NVMe Storage Driver

**StorNVMe.sys** is the system-supplied driver that provides access to high-speed NVMe devices. It is available in Windows Windows 8.1 (and Windows Server 2012 R2) and later versions.

**StorNVMe.sys** supports and uses many [NVMe specification](https://nvmexpress.org/)-defined features. Feature access is available through the following IOCTLs:

- [IOCTL_SCSI_PASS_THROUGH](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through)

- [IOCTL_STORAGE_PROTOCOL_COMMAND](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)

- [IOCTL_STORAGE_QUERY_PROPERTY](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property)

- [IOCTL_STORAGE_FIRMWARE_DOWNLOAD](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_download)

- [IOCTL_STORAGE_FIRMWARE_ACTIVATE](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_activate)

- [IOCTL_STORAGE_FIRMWARE_GET_INFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_get_info)

- [IOCTL_STORAGE_REINITIALIZE_MEDIA](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reinitialize_media)
