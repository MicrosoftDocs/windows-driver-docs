---
title: StorNVMe Command Set Support
description: StorNVMe Command Set Support
ms.assetid: c0bcee11-ea66-4726-99a2-ad18256cf616
ms.date: 05/12/2020
ms.localizationpriority: medium
---

# StorNVMe Command Set Support

The matrices below list the NVMe *Admin* and *NVM* command sets and associated opcodes, and indicate the support provided by **StorNVMe** on Windows 10 version 1903 and later.  

See [Working with NVMe drives](https://docs.microsoft.com/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries) for additional information.

## Admin Command Set Support

| Opcode  | NVMe Command                | StorNVMe Support      | Comments |
| ------  | --------------------------  | --------------------- | -------- |
| 0       | Delete I/O Submission Queue | Internal Driver Usage |    |
| 1       | Create I/O Submission Queue | Internal Driver Usage |    |
| 2       | Get Log Page                | Internal Driver Usage; IOCTL_STORAGE_QUERY_PROPERTY |   |
| 4       | Delete I/O Completion Queue | Internal Driver Usage |   |
| 5       | Create I/O Completion Queue | Internal Driver Usage |
| 6       | Identify                    | Internal Driver Usage; IOCTL_STORAGE_QUERY_PROPERTY, IOCTL_STORAGE_FIRMWARE_GET_INFO |   |
| 8       | Abort                       |   | Currently not supported |
| 9       | Set Features                | Internal Driver Usage; IOCTL_STORAGE_SET_PROPERTY | Only enabled for Host Controlled Thermal Management Set Features for IOCTL_STORAGE_SET_PROPERTY |
| Ah      | Get Features                | Internal Driver Usage; IOCTL_STORAGE_QUERY_PROPERTY |   |
| Ch      | Asynchronous Event Request  | Internal Driver Usage |   |   |
| Dh      | Namespace Management        | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 10h     | Firmware Commit             | IOCTL_STORAGE_FIRMWARE_ACTIVATE | |
| 11h     | Firmware Image Download     | IOCTL_STORAGE_FIRMWARE_DOWNLOAD | |
| 14h     | Device Self-Test            | IOCTL_STORAGE_PROTOCOL_COMMAND  | |
| 15h     | Namespace Attachment        | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 19h     | Directive Send              | Internal Driver Usage |   |
| 1Ah     | Directive Receive           | Internal Driver Usage |   |
| 1Ch     | Virtualization Management   |   | Currently not supported |
| 1Dh     | NVMe-MI Send                | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 1Eh     | NVMe-MI Receive             | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 7Ch     | Doorbell Buffer Config      |   | Currently not supported |
| 80h     | Format NVM                  | IOCTL_SCSI_PASS_THROUGH, IOCTL_STORAGE_PROTOCOL_COMMAND, IOCTL_STORAGE_REINITIALIZE_MEDIA | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND. SCSIOP_SANITIZE for IOCTL_SCSI_PASS_THROUGH. IOCTL_STORAGE_REINITIALIZE_MEDIA only supports crypto erase. |
| 81h     | Security Send               | IOCTL_SCSI_PASS_THROUGH | SCSIOP_SECURITY_PROTOCOL_OUT for IOCTL_SCSI_PASS_THROUGH |
| 82h     | Security Receive            | IOCTL_SCSI_PASS_THROUGH | SCSIOP_SECURITY_PROTOCOL_IN for IOCTL_SCSI_PASS_THROUGH |
| 84h     | Sanitize                    | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 86h     | Get LBA Status              |   | Currently not supported |
| C0h-FFh | Vendor Specific             | IOCTL_STORAGE_PROTOCOL_COMMAND | Vendor-specific pass-through commands. Requires controller to support command effects log and command effect data of vendor command should report as supported. |

## NVM Command Set Support

| Opcode  | NVMe Command                | StorNVMe Support      | Comments |
| ------  | --------------------------  | --------------------- | -------- |
| 0       | Flush                       | Internal Driver Usage, IOCTL_SCSI_PASS_THROUGH | SCSIOP_SYNCHRONIZE_CACHE for IOCTL_SCSI_PASS_THROUGH |
| 1       | Write                       | Internal Driver Usage, IOCTL_SCSI_PASS_THROUGH | SCSIOP_WRITE/SCSIOP_WRITE16 for  IOCTL_SCSI_PASS_THROUGH |
| 2       | Read                        | Internal Driver Usage, IOCTL_SCSI_PASS_THROUGH | SCSIOP_READ/SCSIOP_READ16 for IOCTL_SCSI_PASS_THROUGH |
| 4       | Write Uncorrectable         |   | Currently not supported |
| 5       | Compare                     | IOCTL_STORAGE_PROTOCOL_COMMAND | Only enabled in Win PE mode for IOCTL_STORAGE_PROTOCOL_COMMAND |
| 8       | Write Zeroes                |   | Currently not supported |
| 9       | Dataset Management          | IOCTL_SCSI_PASS_THROUGH | Only TRIM (Deallocate); SCSIOP_UNMAP for IOCTL_SCSI_PASS_THROUGH |
| Ch      | Verify                      |   | Currently not supported |
| Dh      | Reservation Register        |   | Currently not supported |
| Eh      | Reservation Report          |   | Currently not supported |
| 11h     | Reservation Acquire         |   | Currently not supported |
| 15h     | Reservation Release         |   | Currently not supported |
| 80h-FFh | Vendor Specific             | IOCTL_STORAGE_PROTOCOL_COMMAND | Vendor-specific pass-through commands. Requires controller to support command effects log and command effect data of vendor command should report as supported. |
