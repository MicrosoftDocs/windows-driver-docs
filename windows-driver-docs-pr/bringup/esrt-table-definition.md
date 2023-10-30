---
title: ESRT table definition
description: The pointer to the ESRT table is identified via its corresponding GUID in the EFI_CONFIGURATION_TABLE.
ms.date: 03/23/2023
---

# ESRT table definition

The pointer to the ESRT table is identified via its corresponding GUID in the EFI_CONFIGURATION_TABLE.

```cpp
#define EFI_SYSTEM_RESOURCE_TABLE_GUID   \
{ 0xb122a263, 0x3661, 0x4f68,  0x99, 0x29, 0x78, 0xf8, 0xb0, 0xd6, 0x21, 0x80  }
```

The following table describes the format of the ESRT table and the firmware resource entries contained in the table.

| Field | Array value | Byte length | Byte offset | Description |
|--|--|--|--|--|
| Firmware Resource Count |  | 4 | 0 | The number of firmware resource entries in the ESRT. Must not be zero. |
| Firmware Resource Maximum |  | 4 | 4 | The maximum number of resource array entries that can be added without reallocating the table. Must be greater than or equal to Firmware Resource Count. |
| Firmware Resource Version |  | 8 | 8 | The firmware resource entry version. This value should be set to 1 |
| Firmware Resource Entry Array |  |  |  | Firmware Resource Entry 0 |
|  | Firmware Class | 16 | 16 | A GUID that identifies a firmware component that can be updated via update capsule. This GUID will be passed into the UEFI update capsule run-time service as the update capsule header's CapsuleGuid parameter during update. |
|  | Firmware Type | 4 | 32 | One of the following values that identifies the type of firmware resource:<br><br>0: Unknown<br><br>1: System firmware<br><br>2: Device firmware<br><br>3: UEFI driver |
|  | Firmware Version | 4 | 36 | The current firmware version, where a larger number represents a newer release. The format of this value is not defined, but should incorporate version major and minor numbers. The recommended format is first word is major and second word is minor version numbers. |
|  | Lowest Supported Firmware Version | 4 | 40 | The lowest firmware resource version to which a firmware resource can be rolled back for the given system/device. If a security related fix is available in this firmware version, then the least compatible version should be equal to the current firmware version. |
|  | Capsule Flags | 4 | 44 | Flags that will be passed into the UEFI update capsule run-time service in bits 0 – 15 of the update capsule header's Flags field (the OS is responsible to configure bits 16 – 31 of Flags as defined by section 7.5.3 of the UEFI specification). |
|  | Last Attempt Version | 4 | 48 | The last firmware version for which an update was attempted. This value uses the same format as Firmware Version. |
|  | Last Attempt Status | 4 | 52 | One of the following values that describes the status of the last firmware update attempt:<br><br>0: Success<br><br>1: Unsuccessful<br><br>2: Insufficient resources<br><br>3: Incorrect version<br><br>4: Invalid image format<br><br>5: Authentication error<br><br>6: Power event - AC not connected<br><br>7: Power event - Insufficient battery |
| ... |  |  |  | Firmware Resource Entry 1 |

Core UEFI firmware should allocate and populate an ESRT configuration table containing one system resource entry for itself (system firmware). For illustrative purposes, in this guide core firmware will also create one additional entry representing a device that supports device firmware update using the firmware update package mechanism.

There must always be exactly one entry describing system firmware. This entry is used to target a system firmware update. If an implementation performs system and device firmware updates as a single, monolithic operation, the system firmware entry must be used to target the update. In all other cases, device firmware updates are targeted by an ESRT entry describing device firmware.

The first step then is to generate GUIDs to represent these two firmware resources, i.e., {SYSTEM_FIRMWARE} and {DEVICE_FIRMWARE}. Table 2 shows an example of a table definition. This example assumes both firmware versions are currently version 1 (Firmware Version == 1).

| Field | Array value | Value | Comment |
|--|--|--|--|
| Firmware Resource Count |  | 2 | This table contains two firmware resource entries. |
| Firmware Resource Maximum |  | 2 | This table allocation contains enough space to describe a maximum of two resources. |
| Firmware Resource Version |  | 1 | The firmware resource entry format version this table uses is 1. |
| Firmware Resource Entry Array |  | Firmware resource entry 0 |  |
|  | Firmware Class | (SYSTEM_FIRMWARE) | This GUID identifies the system firmware for update via PnP. |
|  | Firmware Type | 1 | System firmware type is 1. |
|  | Firmware Version | 1 | The current system firmware version is 1. |
|  | Lowest Supported Firmware Version | 1 | The lowest supported firmware version is 1, so firmware cannot be rolled back to a version earlier than version 1. |
|  | Capsule Flags | 0 | System firmware doesn't define any private capsule update flags. |
|  | Last Attempt Version | 1 | The last system firmware version for which an update was attempted was version 1. |
|  | Last Attempt Status | 0 | The last system firmware update attempt was successful. |
|  |  | Firmware resource entry 1 |  |
|  | Firmware Class | (DEVICE_FIRMWARE) | This GUID identifies the device firmware for update via PnP. |
|  | Firmware Type | 2 | Device firmware type is 2. |
|  | Firmware Version | 1 | The current device firmware version is 1. |
|  | Lowest Supported Firmware Version | 1 | The lowest supported firmware version is 1, so firmware cannot be rolled-back to a version earlier than version 1. |
|  | Capsule Flags | 0x8010 | Device firmware defines private capsule update flags (0x8010). |
|  | Last Attempt Version | 1 | The last device firmware version for which an update was attempted is version 1 |
|  | Last Attempt Status | 0 | The last device firmware update attempt was successful. |

The above ESRT example is used elsewhere in this documentation to walk through the firmware update process and describe Windows support for the update process as well as a supporting firmware implementation.

## Related topics

[Plug and play device](plug-and-play-device.md)  

[Authoring an update driver package](authoring-an-update-driver-package.md)  

[Processing updates](processing-updates.md)  

[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  

[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  

[Firmware update status](firmware-update-status.md)  
