---
title: NVMe feature and extended capability support
description: Describes NVMe features supported by StorNVMe
ms.date: 11/19/2021
---

# NVMe feature and extended capability support

The following table lists Features and Extended Capabilities defined in the NVM Express specifications for NVMe devices as follows:

* The columns with specification references indicate the section(s) in the NVM Express specification that describe the Feature or Extended Capability ("Caps"):
  * *NVMe 1.4 (Features)* – NVM Express Revision 1.4, June 10, 2019
  * *NVMe 2.0 (Caps) Base* – NVM Express Base Specification 2.0a, July 23rd, 2021
  * *NVMe 2.0 (Caps) NVM* – NVM Express NVM Command Set Specification 1.0a, July 23rd, 2021
  * *NVMe 2.0 (Caps) ZNS* – Zoned Namespace Command Set Specification 1.1a, July 23rd, 2021
* StorNVMe Supported – Indicates support in the StorNVMe device driver on Windows 10 version 1903 and later.
* Comments – Any additional relevant information; for example, whether supported as part of an IOCTL operation. "WinPE Only" indicates support only in WinPE editions of Windows.

| Feature or Extended Capability | NVMe 1.4 (Features) | NVMe 2.0 (Caps) Base | NVMe 2.0 (Caps) NVM | NVMe 2.0 (Caps) ZNS | StorNVMe Supported | Comments |
| -- | -- | -- | -- | -- | -- | -- |
| Asymmetric Namespace Access Reporting | 8.20 | 8.1 | 5.1 |  |  |  |
| Boot Partitions                       | 8.13 | 8.2 |     |  |  |  |
| Capacity Management                   |      | 8.3 |     |  |  |  |
| Command and Feature Lockdown          |      | 8.4 |     |  |  |  |
| Controller Memory Buffer              |      | 8.5 |     |  |  |  |
| Device Self-test Operations           | 8.11 | 8.6 |     |  | Yes | Available through [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). |
| Directives                            |      | 8.7 |     | 5.2 | Yes | Supports Identify (Directive Type 00h) and Streams (Directive Type 01h) |
| Doorbell Stride for Software Emulation | 8.6 | 8.8 |  |  |  |  |
| End-to-End Data Protection            | 8.3 |  | 5.2 |  |  |  |
| Endurance Groups                      | 8.17 | 3.2.3 |  |  | Yes | May be retrieved through [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) |
| Finish Zone Recommended      |  |  |  | 5.5 | | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| Firmware Update Process      | 8.1 | 3.11 |  |  | Yes | Supports Slot 1 READ-ONLY, multiple slots for Commit/Download. Aligns to controller reported FW Update Granularity. Firmware Activation without Reset supported via Commit Action (CA)  011b of Firmware Commit Admin Command |
| Get LBA Status               | 8.22 |  | 5.8.1 |  |  |  |
| Host Memory Buffer | 8.9 | 8.9 |  |  | Yes |  |
| Host Operation with Asymmetric Namespace Access Reporting (Informative) | 8.21 | 8.10 |  |  |  |  |
| Improving Performance through I/O Size and Alignment Adherence | 8.25 |  | 5.8.2 |  | Yes | Supports Namespace Optimal IO Boundary (NOIOB). Currently does not support NPWG, NPWA, NPDG, NPDA, or NOWS. |
| Metadata Handling | 8.2 |  | 5.8.3 |  |  |  |
| Namespace Management   | 8.12 | 8.11 | 5.3 |  | Yes | WinPE only. Available through [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command) |
| Namespace Write Protection | 8.19 | 8.12 |  |  |  |  |
| NVM Command Set Media and Data Error Handling |  |  | 5.4 |  |  |  |
| NVMe over Fabrics In-band Authentication |  | 8.13 |  |  |  |  |
| Persistent Memory Region |  | 8.14 |  |  |  |  |
| Power Management | 8.4 | 8.15 |  |  | Yes | Supports non-operational power states. Autonomous power state transitions are disabled by default. Runtime D3 transitions are enabled by default for selected platforms in Modern Stand-by. Host controlled thermal management Get/Set features supported through [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property) and [IOCTL_STORAGE_SET_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_set_property). |
| Predictable Latency Mode      | 8.18 | 8.16 |     |     |  |  |
| Read Recovery Level           | 8.16 | 8.17 |     |     |  |  |
| Replay Protected Memory Block | 8.10 | 8.18 |     |     |  |  |
| Reservations                  | 8.8  | 8.19 | 5.5 | 5.1 |  |  |
| Reset Zone Recommended        |      |      |     | 5.4 |  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| Rotational Media              |      | 8.20 |  |  |  |  |
| Sanitize Operations           | 8.15 | 8.21 | 5.6 |  | Yes | [IOCTL_STORAGE_PROTOCOL_COMMAND](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_protocol_command). WinPE only prior to Windows 11, Windows Server 2022 |
| Standard Vendor Specific Command Format | 8.7 | 8.23 |  |  |  |  |
| Streams                       |  |  | 5.7 |  |  |  |
| Submission Queue (SQ) Associations | 8.23 | 8.22 |  |  |  |  |
| Telemetry | 8.14 | 8.24 |  |  | Yes | Supported through [IOCTL_SCSI_PASS_THROUGH](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_scsi_pass_through) using command SCSIOP_READ_DATA_BUFF16 with buffer mode as READ_BUFFER_MODE_ERROR_HISTORY. Also available through StorageAdapterProtocolSpecificProperty and StorageDeviceProtocolSpecificProperty from [IOCTL_STORAGE_QUERY_PROPERTY](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_query_property). For host telemetry, also available through [IOCTL_STORAGE_GET_DEVICE_INTERNAL_LOG](/windows-hardware/drivers/ddi/ntddstor/ni-ntddstor-ioctl_storage_get_device_internal_log) starting with Windows 10, version 2004. |
| Universally Unique Identifiers (UUIDs) for Vendor Specific Information | 8.24 | 8.25 |  |  |  |  |
| Virtualization Enhancements | 8.5 | 8.26 |  |  |  |  |
| Zone Active Excursions |  |  |  | 5.6 |  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |
| Zone Descriptor Extension |  |  |  | 5.3 |  | From Windows 11, Windows Server 2022. Reserved for Microsoft internal use. |

See [Working with NVMe drives](/windows/win32/fileio/working-with-nvme-devices#protocol-specific-queries) for additional information.

*Subject to change. See [Working with NVMe Devices](/windows/win32/fileio/working-with-nvme-devices) for additional information.*
