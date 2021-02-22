---
title: StorNVMe command set support
description: Describes the command set support provided by StoreNVMe
ms.date: 08/07/2020
ms.localizationpriority: medium
---

# StorNVMe command set support

The matrices below list the NVMe *Admin* and *NVM* command sets and associated opcodes, and indicate the support provided by **StorNVMe** on Windows 10 version 1903 and later.  

See [Working with NVMe drives](/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries) for additional information.

## Admin Command Set Support

| Opcode  | NVMe Command                | StorNVMe Support      | Comments |
| ------  | --------------------------  | --------------------- | -------- |
| 0       | Delete I/O Submission Queue | Internal Driver Usage |    |
| 1       | Create I/O Submission Queue | Internal Driver Usage |    |
| 2       | Get Log Page                | Internal Driver Usage; [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) |   |
| 4       | Delete I/O Completion Queue | Internal Driver Usage |   |
| 5       | Create I/O Completion Queue | Internal Driver Usage |
| 6       | Identify                    | Internal Driver Usage; [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property), IOCTL_STORAGE_FIRMWARE_GET_INFO |   |
| 8       | Abort                       |   | Currently not supported |
| 9       | Set Features                | Internal Driver Usage; [IOCTL_STORAGE_SET_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_property) | Only enabled for Host Controlled Thermal Management Set Features for [IOCTL_STORAGE_SET_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_property) |
| Ah      | Get Features                | Internal Driver Usage; [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) |   |
| Ch      | Asynchronous Event Request  | Internal Driver Usage |   |   |
| Dh      | Namespace Management        | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 10h     | Firmware Commit             | [IOCTL_STORAGE_FIRMWARE_ACTIVATE](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_activate) | |
| 11h     | Firmware Image Download     | [IOCTL_STORAGE_FIRMWARE_DOWNLOAD](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_firmware_download) | |
| 14h     | Device Self-Test            | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command)  | |
| 15h     | Namespace Attachment        | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 19h     | Directive Send              | Internal Driver Usage |   |
| 1Ah     | Directive Receive           | Internal Driver Usage |   |
| 1Ch     | Virtualization Management   |   | Currently not supported |
| 1Dh     | NVMe-MI Send                | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 1Eh     | NVMe-MI Receive             | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 7Ch     | Doorbell Buffer Config      |   | Currently not supported |
| 80h     | Format NVM                  | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through), [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command), IOCTL_STORAGE_REINITIALIZE_MEDIA | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). SCSIOP_SANITIZE for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through). IOCTL_STORAGE_REINITIALIZE_MEDIA only supports crypto erase. |
| 81h     | Security Send               | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | SCSIOP_SECURITY_PROTOCOL_OUT for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| 82h     | Security Receive            | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | SCSIOP_SECURITY_PROTOCOL_IN for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| 84h     | Sanitize                    | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 86h     | Get LBA Status              |   | Currently not supported |
| C0h-FFh | Vendor Specific             | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Vendor-specific pass-through commands. Requires controller to support command effects log and command effect data of vendor command should report as supported. |

## NVM Command Set Support

| Opcode  | NVMe Command                | StorNVMe Support      | Comments |
| ------  | --------------------------  | --------------------- | -------- |
| 0       | Flush                       | Internal Driver Usage, [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | SCSIOP_SYNCHRONIZE_CACHE for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| 1       | Write                       | Internal Driver Usage, [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | SCSIOP_WRITE/SCSIOP_WRITE16 for  [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| 2       | Read                        | Internal Driver Usage, [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | SCSIOP_READ/SCSIOP_READ16 for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| 4       | Write Uncorrectable         |   | Currently not supported |
| 5       | Compare                     | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Only enabled in Win PE mode for [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| 8       | Write Zeroes                |   | Currently not supported |
| 9       | Dataset Management          | [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) | Only TRIM (Deallocate); SCSIOP_UNMAP for [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) |
| Ch      | Verify                      |   | Currently not supported |
| Dh      | Reservation Register        |   | Currently not supported |
| Eh      | Reservation Report          |   | Currently not supported |
| 11h     | Reservation Acquire         |   | Currently not supported |
| 15h     | Reservation Release         |   | Currently not supported |
| 80h-FFh | Vendor Specific             | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) | Vendor-specific pass-through commands. Requires controller to support command effects log and command effect data of vendor command should report as supported. |
