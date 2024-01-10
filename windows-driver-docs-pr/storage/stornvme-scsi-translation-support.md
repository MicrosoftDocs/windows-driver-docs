---
title: StorNVMe SCSI Translation Support 
description: StorNVMe SCSI Translation Support 
ms.date: 01/09/2024
---

# StorNVMe SCSI Translation Support

The following table lists SCSI commands and the translated NVMe command(s), where applicable. **StorNVMe** on Windows 10 version 1903 and later versions is compliant to SCSI Translation Reference Rev 1.5.

For more information, see [Working with NVMe drives](/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries).

| SCSI Command | Translated NVMe Command |
| ------------ | ----------------------- |
| Format Unit/Sanitize*   | Sanitize                    |
| Inquiry                 | Identify                    |
| Log Sense               | Get Features, Get Log Page  |
| Mode Select (10)        | -                           |
| Mode Sense (10)         | Identify, Get Features      |
| Read (10)               | Read                        |
| Read (16)               | Read                        |
| Read Capacity (10)      | Identify                    |
| Read Capacity (16)      | Identify                    |
| Read Data Buffer 16     | Get Log Page                |
| Report LUNs             | Identify                    |
| Security Protocol In    | Security Receive            |
| Security Protocol Out   | Security Send               |
| Send Diagnostic         | n/a                         |
| Start Stop Unit         | Set Features, Get Features  |
| Synchronize Cache (10)  | Flush                       |
| Test Unit Ready         | -                           |
| Unmap                   | Dataset Management          |
| Verify 10               | Verify                      |
| Verify 16               | Verify                      |
| Write 10                | Write                       |
| Write 16                | Write                       |
| Write Buffer            | Firmware Download, Activate |

* SCSI Format Unit isn't supported as it can result in data loss.

  Sanitize SCSI is translated to Sanitize NVMe command. Details:

  | Sanitize CDB  | NVMe command |
  | ------------  | ------------ |
  | **OperationCode**: SCSIOP_SANITIZE | NVME_ADMIN_COMMAND_SANITIZE (0x86) |
  | Action: BlockErase | BLOCK_ERASE_SANITIZE (2) |
  | Action: CryptoErase | CRYPTO_ERASE_SANITIZE (4) |
  | Immediate (only 0 supported) | |
  | AUSE | AllowUnrestrictedSanitizeExit |

  The Overwrite action isn't supported.
