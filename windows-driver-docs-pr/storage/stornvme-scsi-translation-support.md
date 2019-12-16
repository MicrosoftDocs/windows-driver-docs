---
title: StorNVMe SCSI Translation Support 
description: StorNVMe SCSI Translation Support 
ms.assetid: cd903ef8-9528-46a5-a276-06cf2fff2b88
ms.date: 12/12/2019
ms.localizationpriority: medium
---

# StorNVMe SCSI Translation Support

The following table lists SCSI commands and the translated NVMe command(s), where applicable. **StorNVMe** is compliant to SCSI Translation Reference Rev 1.5.

| SCSI Command | NVMe Command | Comments |
| ------------ | ------------ | -------- |
| Compare and Write*      | Compare and Write           |
| Format Unit/Sanitize    | Format NVM                  |
| Inquiry                 | Identify                    |
| Log Sense               | Get Features, Get Log Page  |
| Mode Select (6)*        | -                           |
| Mode Select (10)        | -                           |
| Mode Sense (6)*         | Identify, Get Features      |
| Mode Sense (10)         | Identify, Get Features      |
| Read (6)*               | Read                        |
| Read (10)               | Read                        |
| Read (12)*              | Read                        |
| Read (16)               | Read                        |
| Read Capacity (10)      | Identify                    |
| Read Capacity (16)      | Identify                    |
| Report LUNs             | Identify                    |
| Request Sense*          | -                           |
| Security Protocol In    | Security Receive            |
| Security Protocol Out   | Security Send               |
| Send Diagnostic         | n/a                         |
| Start Stop Unit         | Set Features, Get Features  |
| Synchronize Cache (10)  | Flush                       |
| Synchronize Cache (16)* | Flush                       |
| Test Unit Ready         | -                           |
| Unmap                   | Dataset Management          |
| Verify 10               | Verify                      |
| Verify 12*              | Verify                      |
| Verify 16               | Verify                      |
| Write Long 10*          | Write Uncorrectable         |
| Write Long 16*          | Write Uncorrectable         |
| Write 6*                | Write                       |
| Write 10                | Write                       |
| Write 12*               | Write                       |
| Write 16                | Write                       |
| Write Buffer            | Firmware Download, Activate |

\* *SCSI commands with asterisks have translatable NVMe command(s); however, *StorNVMe* currently does not support the translation.*
