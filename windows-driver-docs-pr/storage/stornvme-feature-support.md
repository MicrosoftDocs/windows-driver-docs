---
title: NVMe Features Supported by StorNVMe
description: NVMe Features Supported by StorNVMe
ms.assetid: 96b62fbb-bcf3-402d-ba29-0a61dc95c92c
ms.date: 12/12/2019
ms.localizationpriority: medium
---

# NVMe Features Supported by StorNVMe

The following matrix lists NVME features, indicates whether each feature is mandatory or optional, and indicates whether **StorNVMe** supports that feature.

| Feature  | Optional | Mandatory | Supported | Comments |
| :------- | :------: | :-------: | :-------: | :------- |
| Firmware Commit/Download                                       |   | X | X | Supports Slot 1 READ-ONLY, multiple slots. Aligns to controller reported FW Update Granularity |
| Firmware Activation without Reset                              | X |   | X | |
| Metadata Handling                                              | X |   |   | |
| End-to-End Data Protection                                     | X |   |   | |
| Power Management Support                                       |   | X | X | Supports non-operational power states |
| Autonomous Power State Transitions                             | X |   | X | Supports APST, but disabled by default. Can be enabled through registry setting IdlePowerMode=3 |
| D3 Support                                                     | X |   | X | Supports D3 transition, but disabled by default. Can be enabled through registry setting IdlePowerMode=2 |
| Runtime D3 Transitions                                         | X |   | X | Enabled by default for selected platforms in Modern Stand-by |
| Host Controlled Thermal Management                             | X |   | X | Get Feature through IOCTL_STORAGE_QUERY_PROPERTY and Set feature through IOCTL_STORAGE_SET_PROPERTY |
| Virtualization Enhancements                                    | X |   |   | |
| Doorbell Stride for Software Emulation                         |   | X |   | |
| Standard Vendor Specific Command Format                        |   | X |   | |
| Reservations                                                   | X |   |   | |
| Host Memory Buffer Support                                     | X |   | X | |
| Replay Protected Memory Block Support                          | X |   |   | |
| Device Self-Test                                               | X |   | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND |
| Namespace Management/Attachment Command support                  | X |   | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Boot Partitions                                                | X |   |   | |
| Telemetry Host/Controller Initiated Log Page Support           | X |   | X | Supported through IOCTL_SCSI_PASS_THROUGH using command SCSIOP_READ_DATA_BUFF16 with buffer mode as READ_BUFFER_MODE_ERROR_HISTORY |
| Sanitize Operations                                            | X |   |   | |
| Read Recovery Level                                            | X |   |   | |
| Endurance Groups                                               | X |   | X | Information can be retrieved through IOCTL_STORAGE_QUERY_PROPERTY |
| Predictable Latency Mode                                       | X |   |   | |
| Namespace Write Protection                                     | X |   |   | |
| Asymmetric Namespace Access Reporting                          | X |   |   | |
| Get LBA Status                                                 | X |   |   | |
| SQ Associations                                                | X |   |   | |
| UUIDs for Vendor Specific Information                          | X |   |   | |
| Namespace Optimal IO boundary                                  | X |   | X | |
| Improving Performance through I/O Size and Alignment Adherence | X |   |   | Currently doesn't support NPWG, NPWA, NPDG, NPDA, and NOWS |
| Directives                                                     | X |   | X | Supports Stream and Identify directive |
|                                                                |   |   |   | |
| Version Compliance                                             |   | X | X | Compliance of version <= 1.4 |
| Recommended Arbitration Burst                                  |   | X | X | User could set any value apart from controller reported value through registry key ArbitrationBurst |
| Controller Multi-path IO                                       | X |   |   | |
| Namespace sharing capabilities                                 | X |   |   | |
| Maximum Data Transfer Size Support                             | X |   | X | |
| Runtime D3 latency                                             | X |   | X | |
| Namespace Attribute Notices event                              | X |   | X | Log the event and trigger namespace reenumeration based on change log |
| Firmware Activation Notices event                              | X |   | X | Log the event and read the log page |
| Endurance Group Event Aggregate Log Page notices event         | X |   |   | |
| Controller Attributes                                          | X |   | X | Non-operational Power State Permissive Mode and NVM Sets are checked and used |
| NVM Sets                                                       | X |   | X | |
| FRU Globally Unique Identifier                                 | X |   |   | |
| Security Send/Security Receive Support                         | X |   | X | |
| Format NVM Support                                             | X |   | X | Supported through SCSI sanitize |
| NVMe-MI Send and NVMe-MI Receive                               | X |   | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Doorbell Buffer Config Support                                 | X |   |   | |
| Abort Command Support with Specified Limits                    |   | X |   | |
| Asynchronous Event Request Support                             |   | X | X | Supports limited to event count of 4 |
| SMART Log Page Support                                         | X |   | X | Supports log page per Namespace |
| Command Supported and Effects Log Page Support                 | X |   | X | Checked for vendor specific command execution |
| Extended Data for Log Page                                     | X |   | X | Supported through IOCTL_STORAGE_QUERY_PROPERTY |
| Persistent Event Log Support                                   | X |   |   | |
| Firmware Activation maximum time support                       | X |   |   | Currently not supported even though firmware activation without reset is supported |
| Firmware Update Granularity                                    | X |   | X | |
| Keep Alive Support                                             | X |   |   | |
| Temperature Report                                             |   | X | X | WCTEMP and CCTEMP. Accessible though IOCTL_STORAGE_QUERY_PROPERTY |
| Multiple Namespaces                                            | X |   | X | Supports runtime enumeration of namespaces |
| Compare Command                                                | X |   | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Write Uncorrectable Command                                    | X |   |   | |
| Dataset Management Command                                     | X |   | X | |
| Write Zeroes                                                   | X |   |   | |
| Set Features Save Option                                       | X |   | X | Currently only used for VWC persistent setting |
| Timestamp                                                      | X |   | X | |
| Verify Command                                                 | X |   |   | |
| Fused Operations (Compare and Write)                           | X |   |   | |
| Volatile Write Cache                                           | X |   | X | |
| Atomic Write Unit Normal                                       | X |   |   | |
| NVMe Qualified Names                                           | X |   |   | |
| Namespace Thinprovisioning                                     | X |   | X | |
| NVMe Boot                                                      |   | X | X | |
| Controller Fatal Status Condition                              | X |   | X | Log the event and continue with controller re-initialization |
