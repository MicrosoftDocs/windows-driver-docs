---
title: NVMe Features Supported by StorNVMe
description: NVMe Features Supported by StorNVMe
ms.assetid: 96b62fbb-bcf3-402d-ba29-0a61dc95c92c
ms.date: 01/13/2020
ms.localizationpriority: medium
---

# NVMe Features Supported by StorNVMe

The following matrix lists NVME features and indicates the support provided by **StorNVMe** on Windows 10 version 1903 and later versions.

| Feature  | Supported | Comments |
| :------- | :-------: | :------- |
| Firmware Update Process                                        | X |  Supports Slot 1 READ-ONLY, multiple slots for Commit/Download. Aligns to controller reported FW Update Granularity. |
| Firmware Activation without Reset                              | X | |
| Metadata Handling                                              |   | |
| End-to-End Data Protection                                     |   | |
| Power Management                                               | X | Supports non-operational power states. Autonomous power state transitions are disabled by default. Runtime D3 transitions are enabled by default for selected platforms in Modern Stand-by. Host controlled thermal management Get and Set features supported through IOCTL_STORAGE_QUERY_PROPERTY and IOCTL_STORAGE_SET_PROPERTY, respectively. |
| Virtualization Enhancements                                    |   | |
| Doorbell Stride for Software Emulation                         |   | |
| Standard Vendor Specific Command Format                        |   | |
| Reservations                                                   |   | |
| Host Memory Buffer                                             | X | |
| Replay Protected Memory Block                                  |   | |
| Device Self-test Operations                                    | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND |
| Namespace Management                                           | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Boot Partitions                                                |   | |
| Telemetry                                                      | X | Supported through IOCTL_SCSI_PASS_THROUGH using command SCSIOP_READ_DATA_BUFF16 with buffer mode as READ_BUFFER_MODE_ERROR_HISTORY |
| Sanitize Operations                                            |   | |
| Read Recovery Level                                            |   | |
| Endurance Groups                                               | X | Information can be retrieved through IOCTL_STORAGE_QUERY_PROPERTY |
| Predictable Latency Mode                                       |   | |
| Namespace Write Protection                                     |   | |
| Asymmetric Namespace Access Reporting                          |   | |
| Get LBA Status                                                 |   | |
| SQ Associations                                                |   | |
| UUIDs for Vendor Specific Information                          |   | |
| Improving Performance through I/O Size and Alignment Adherence | X | Supports Namespace Optimal IO Boundary (NOIOB). Currently doesn't support NPWG, NPWA, NPDG, NPDA, and NOWS |

<!---  Everything commented out was provided by Vishal but is not in NVME Spec Section 8

| Directives                                                     | X | Supports Stream and Identify directive |
|                                                                |   | |
| Version Compliance                                             | X | Compliance of version <= 1.4 |
| Recommended Arbitration Burst                                  | X | User could set any value apart from controller reported value through registry key ArbitrationBurst |
| Controller Multi-path IO                                       |   | |
| Namespace sharing capabilities                                 |   | |
| Maximum Data Transfer Size Support                             | X | |
| Runtime D3 latency                                             | X | |
| Namespace Attribute Notices event                              | X | Log the event and trigger namespace reenumeration based on change log |
| Firmware Activation Notices event                              | X | Log the event and read the log page |
| Endurance Group Event Aggregate Log Page notices event         |   | |
| Controller Attributes                                          | X | Non-operational Power State Permissive Mode and NVM Sets are checked and used |
| NVM Sets                                                       | X | |
| FRU Globally Unique Identifier                                 |   | |
| Security Send/Security Receive Support                         | X | |
| Format NVM Support                                             | X | Supported through SCSI sanitize |
| NVMe-MI Send and NVMe-MI Receive                               | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Doorbell Buffer Config Support                                 |   | |
| Abort Command Support with Specified Limits                    |   | |
| Asynchronous Event Request Support                             | X | Supports limited to event count of 4 |
| SMART Log Page Support                                         | X | Supports log page per Namespace |
| Command Supported and Effects Log Page Support                 | X | Checked for vendor specific command execution |
| Extended Data for Log Page                                     | X | Supported through IOCTL_STORAGE_QUERY_PROPERTY |
| Persistent Event Log Support                                   |   | |
| Firmware Activation maximum time support                       |   | Currently not supported even though firmware activation without reset is supported |
| Firmware Update Granularity                                    | X | |
| Keep Alive Support                                             |   | |
| Temperature Report                                             | X | WCTEMP and CCTEMP. Accessible though IOCTL_STORAGE_QUERY_PROPERTY |
| Multiple Namespaces                                            | X | Supports runtime enumeration of namespaces |
| Compare Command                                                | X | Supported through IOCTL_STORAGE_PROTOCOL_COMMAND in WinPE mode |
| Write Uncorrectable Command                                    |   | |
| Dataset Management Command                                     | X | |
| Write Zeroes                                                   |   | |
| Set Features Save Option                                       | X | Currently only used for VWC persistent setting |
| Timestamp                                                      | X | |
| Verify Command                                                 |   | |
| Fused Operations (Compare and Write)                           |   | |
| Volatile Write Cache                                           | X | |
| Atomic Write Unit Normal                                       |   | |
| NVMe Qualified Names                                           |   | |
| Namespace Thinprovisioning                                     | X | |
| NVMe Boot                                                      | X | |
| Controller Fatal Status Condition                              | X | Log the event and continue with controller re-initialization |
--->
