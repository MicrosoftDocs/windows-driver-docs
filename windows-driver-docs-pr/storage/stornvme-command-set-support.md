---
title: StorNVMe Command Set Support
description: Describes the command set support provided by StorNVMe
keywords:
- commands, opcodes, NVM Express, StorNVMe
ms.date: 12/20/2024
ms.topic: reference
---

# StorNVMe command set support

The tables in this article list:

* Commands and opcodes defined in the NVM Express specifications for the NVMe Admin Command Set.
* All I/O Commands (Base Specification), I/O Commands for the NVM Command Set, and I/O Commands for the Zoned Namespace Command Set.

The tables include the following information:

* *Header Definition* – Indicates that an enumeration for the command is defined in the relevant Windows header file.
* *StorNVMe Supported* – Indicates that the StorNVMe device driver supports the command on Windows 10 version 1903 and later.
* *Driver Int Use* (Driver Internal Use) – Indicates that the StorNVMe driver can internally generate/issue the command.
* *Comments* – Any other relevant information; for example, whether the command can be issued as part of an IOCTL operation. "WinPE Only" indicates that the command is supported only on WinPE editions of Windows.

## Admin commands

| Opcode | NVMe Admin Command       | Header Definition | StorNVMe Supported | Driver Int Use | Comments |
| ------ | ------------------       | ----------------- | ------------------ | -------------- | -------- |
| ```0h```  | ```Delete I/O Submission Queue``` | Yes | Yes | Yes |  |
| ```1h```  | ```Create I/O Submission Queue``` | Yes | Yes | Yes |  |
| ```2h```  | ```Get Log Page```                | Yes | Yes | Yes | [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) |
| ```4h```  | ```Delete I/O Completion Queue``` | Yes | Yes | Yes |  |
| ```5h```  | ```Create I/O Completion Queue``` | Yes | Yes | Yes |  |
| ```6h```  | ```Identify```                    | Yes | Yes | Yes | [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property), [IOCTL_STORAGE_FIRMWARE_GET_INFO](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_get_info)
| ```8h```  | ```Abort```                       | Yes |     |     |  |
| ```9h```  | ```Set Features```                | Yes | Yes | Yes | [IOCTL_STORAGE_SET_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_property). Currently only supports Host Controlled Thermal Management. |
| ```Ah```  | ```Get Features```                | Yes | Yes | Yes | [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) |
| ```Ch```  | ```Asynchronous Event Request```  | Yes | Yes | Yes |  |
| ```Dh```  | ```Namespace Management```        | Yes | Yes |     | WinPE only. [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| ```10h``` | ```Firmware Commit``` (previously ```Firmware Activate```) | Yes | Yes | Yes | [IOCTL_STORAGE_FIRMWARE_ACTIVATE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_activate) |
| ```11h``` | ```Firmware Image Download```     | Yes | Yes | Yes | [IOCTL_STORAGE_FIRMWARE_DOWNLOAD](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_download) |
| ```14h``` | ```Device Self-Test```            | Yes | Yes |     | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| ```15h``` | ```Namespace Attachment```        | Yes | Yes |     | WinPE only. [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| ```18h``` | ```Keep Alive```                  |     |     |     |  |
| ```19h``` | ```Directive Send```              | Yes | Yes | Yes |  |
| ```1Ah``` | ```Directive Receive```           | Yes | Yes | Yes |  |
| ```1Ch``` | ```Virtualization Management```   | Yes |     |     |  |
| ```1Dh``` | ```NVMe-MI Send```                | Yes | Yes |     | WinPE only. [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)
| ```1Eh``` | ```NVMe-MI Receive```             | Yes | Yes |     | WinPE only. [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| ```20h``` | ```Capacity Management```         |     |     |     |  |
| ```24h``` | ```Lockdown```                    |     |     |     |  |
| ```7Ch``` | ```Doorbell Buffer Config```      | Yes |     |     |  |
| ```7Fh``` | ```Fabric Commands```             |     |     |     |  |
| ```80h``` | ```Format NVM```                  | Yes | Yes | Yes | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) for WinPE only. [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) for SCSIOP_SANITIZE. [IOCTL_STORAGE_REINITIALIZE_MEDIA](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_reinitialize_media) for crypto erase only. |
| ```81h``` | ```Security Send```               | Yes | Yes | Yes | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) for SCSIOP_SECURITY_PROTOCOL_OUT |
| ```82h``` | ```Security Receive```            | Yes | Yes | Yes | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) for SCSIOP_SECURITY_PROTOCOL_IN |
| ```84h``` | ```Sanitize```                    | Yes | Yes | Yes | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). From Windows 10, Version 2004 / May 2020 Update, Windows Server Version 2004 (Server Core). WinPE only prior to Windows 11, Windows Server 2022 and only if the user uses IOCTL_STORAGE_PROTOCOL_COMMAND. |
| ```86h``` | ```Get LBA Status```              | Yes |     |     | From Windows 11, Windows Server 2022 |
| ```C0h-FFh``` | Vendor Specific         | N/A | Yes |     | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). Vendor-specific pass-through commands require CSUPP=1 in corresponding Command Supported and Effects Log Page for each vendor-specific command opcode. |

## I/O commands

The next table includes the following information for NVM Express I/O commands:

* *NVMe Spec*: indicates the NVM Express specification that defines the I/O command:
  * A = All I/O Command Sets, NVM Express Base Specification 2.0a, July 23, 2021
  * N = NVM Command Set, NVM Express NVM Command Set Specification 1.0a, July 23, 2021
  * Z = Zoned Namespace Command Set I/O Commands, Zoned Namespace Command Set Specification 1.1a, July 23, 2021

| Opcode | NVMe I/O Command | Header Definition | StorNVMe Supported | Driver Int Use | NVMe Spec | Comments |
| ------ | ---------------- | ----------------- | ------------------ | -------------- | --------- | -------- |
| ```0h```  | ```Flush```  | Yes  | Yes  | Yes  | A,N,Z  | SCSIOP_SYNCHRONIZE_CACHE for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| ```1h```  | ```Write```  | Yes  | Yes  | Yes  | N,Z  | SCSIOP_WRITE/SCSIOP_WRITE16 for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| ```2h```  | ```Read```   | Yes  | Yes  | Yes  | N,Z  | SCSIOP_READ/SCSIOP_READ16 for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| ```4h```  | ```Write Uncorrectable```  | Yes  |   |   | N,Z  | |
| ```5h```  | ```Compare```  | Yes  | Yes  |   | N,Z  | WinPE only. [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| ```8h```  | ```Write Zeroes```  | Yes  |   |   | N,Z  | |
| ```9h```  | ```Dataset Management```  | Yes  | Yes  |   | N,Z  | Only TRIM (Deallocate). SCSIOP_UNMAP for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| ```Ch```  | ```Verify```  | Yes  |   |   | N,Z  | |
| ```Dh```  | ```Reservation Register```  | Yes  |   |   | A,N,Z  | From Windows 11, Windows Server 2022. |
| ```Eh```  | ```Reservation Report```    | Yes  |   |   | A,N,Z  | From Windows 11, Windows Server 2022. |
| ```11h``` | ```Reservation Acquire```   | Yes  |   |   | A,N,Z  | From Windows 11, Windows Server 2022. |
| ```15h``` | ```Reservation Release```   | Yes  |   |   | A,N,Z  | From Windows 11, Windows Server 2022. |
| ```19h``` | ```Copy```  | Yes  |   |   | N,Z  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| ```79h``` | ```Zone Management Send```     | Yes  | Yes  |   | Z  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| ```7Ah``` | ```Zone Management Receive```  | Yes  | Yes  |   | Z  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| ```7Dh``` | ```Zone Append```              | Yes  | Yes  |   | Z  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| ```80h-FFh``` | Vendor Specific  | N/A  | Yes  |   | A,N,Z  | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). Vendor-specific pass-through commands require CSUPP=1 in corresponding Command Supported and Effects Log Page for each vendor-specific command opcode. |

*Subject to change. For more information, see [Working with NVMe drives](/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries).*
