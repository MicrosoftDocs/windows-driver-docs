---
title: Firmware update status
description: At this point it is expected that all firmware updates will be applied, and the results of all updates reflected in the ESRT on the subsequent invocation of the Windows OS loader.
ms.assetid: 988B1E95-2268-4B4F-B0C6-3C965FCD1B1C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Firmware update status


At this point it is expected that all firmware updates will be applied, and the results of all updates reflected in the ESRT on the subsequent invocation of the Windows OS loader. Referring back to the ESRT example in [ESRT table definition](esrt-table-definition.md) and the firmware resource update driver package INF example in [Authoring an update driver package](authoring-an-update-driver-package.md), if version 2 of firmware.bin was successfully applied by firmware, then the new ESRT table would reflect this. Notice that the only difference in the table is that the Firmware Version and Last Attempt Version fields for the system firmware resource entry have changed to reflect the successfully applied new firmware version.

| Field                               | Value                     | Comment                                                                                                                                                                                                              |
|-------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firmware Resource Count             | 2                         | This table contains two firmware resource entries.                                                                                                                                                                   |
| Firmware Resource Maximum           | 2                         | This table allocation contains enough space to describe a maximum of two resources.                                                                                                                                  |
| Firmware Resource Version           | 1                         | The firmware resource entry format version this table uses is 1.                                                                                                                                                     |
| Firmware Resource Entry Array       | Firmware resource entry 0 |                                                                                                                                                                                                                      |
|   Firmware Class                    | (SYSTEM\_FIRMWARE)        | This GUID identifies the system firmware for update via PnP.                                                                                                                                                         |
|   Firmware Type                     | 1                         | System firmware type is 1.                                                                                                                                                                                           |
|   Firmware Version                  | 2                         | The current system firmware version is 2.                                                                                                                                                                            |
|   Lowest Supported Firmware Version | 2                         | Change the lowest supported firmware version to 2, so that the firmware cannot be rolled-back to a version earlier than version 2. This value is typically changed when the firmware update contains security fixes. |
|   Capsule Flags                     | 0                         | System firmware doesn’t define any private capsule update flags.                                                                                                                                                     |
|   Last Attempt Version              | 2                         | The last system firmware version for which an update was attempted was 2                                                                                                                                             |
|   Last Attempt Status               | 0                         | The last system firmware update attempt was successful.                                                                                                                                                              |
|                                     | Firmware resource entry 1 |                                                                                                                                                                                                                      |
|   Firmware Class                    | (DEVICE\_FIRMWARE)        | This GUID identifies the device firmware for update via PnP.                                                                                                                                                         |
|   Firmware Type                     | 2                         | Device firmware type is 2.                                                                                                                                                                                           |
|   Firmware Version                  | 1                         | The current device firmware version is 1.                                                                                                                                                                            |
|   Lowest Supported Firmware Version | 1                         | Keep the lowest supported firmware version as 1. The firmware can be rolled-back to version 1 if necessary.                                                                                                          |
|   Capsule Flags                     | 0x8010                    | Device firmware defines private capsule update flags (0x8010).                                                                                                                                                       |
|   Last Attempt Version              | 1                         | The last device firmware version for which an update was attempted is 1.                                                                                                                                             |
|   Last Attempt Status               | 0                         | The last device firmware update attempt was successful.                                                                                                                                                              |

 

If the firmware cannot successfully apply an update, then the Firmware Version, Last Attempt Version and Last Attempt Status entries in the ESRT will reflect the failed update attempt. For example, if the system is attempting to update version 1 of the firmware to version 2, and fails to successfully apply the update, then the Firmware Version = 1, Last Attempt Version = 2, and Last Attempt Status != 0. (I.e. the Last Attempt Status is set to the appropriate non-zero error code indicating the reason failure occurred. For the list of valid error codes for this entry, see [ESRT table definition](esrt-table-definition.md).

Although the standard update policy enforces that firmware versions can only increase, this policy can be disabled for test purposes via the Policy setting as described in the "Rolling back firmware updates" section below.

## System reset


A system reset allows end-users to revert their systems back to factory settings. It achieves this by re-installing the Windows image pre-loaded on to a system during the manufacturing process. The entire OS, including drivers and applications, will be reinstalled.

**Note**  Due to security requirements which prevent firmware rollback across security boundaries, system reset is unable to roll back firmware versions to match the original firmware deployed in the factory. This means that all versions of firmware must be backwards compatible with all driver and operating system versions shipped on that platform. If firmware is not compatible, this could result in a user returning their system to the manufacturer.

 

## Rolling back firmware updates


In some cases it may be necessary to rollback a firmware update for example during update testing. Each ESRT reported firmware resource has an entry in the following registry key: HKLM\\SYSTEM\\CurrentControlSet\\Control\\FirmwareResources.

The entry is a key with the Name equal to the GUID used to report the resource in the ESRT. To allow a firmware rollback, create a REG\_DWORD value called Policy and set the value to 1. A given firmware resource can only be rolled back to its respective Lowest Supported Firmware Version, as specified in the ESRT. This is to prevent firmware rollbacks beyond the point at which a critical security fix has been made to the firmware. If the firmware version you are rolling back to meets these conditions the OS loader will update to an older version.

## Related topics
[ESRT table definition](esrt-table-definition.md)  
[Plug and play device](plug-and-play-device.md)  
[Authoring an update driver package](authoring-an-update-driver-package.md)  
[Processing updates](processing-updates.md)  
[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  
[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  



