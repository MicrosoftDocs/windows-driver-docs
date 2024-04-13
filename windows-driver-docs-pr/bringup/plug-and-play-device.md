---
title: Plug and Play Device
description: The presence of an ESRT configuration table will direct Windows to enumerate a separate PnP device instance for each firmware resource.
ms.date: 03/23/2023
---

# Plug and play device

The presence of an ESRT configuration table will direct Windows to enumerate a separate PnP device instance for each firmware resource. For driver matching purposes, a firmware resource device is uniquely identified by its hardware IDs, which embed the Firmware ID GUID. Referring to the ESRT example in [ESRT table definition](esrt-table-definition.md), the corresponding device instances are enumerated.

| Device instance ID | Hardware ID |
|--|--|
| UEFI\RES_{SYSTEM_FIRMWARE}\0 | UEFI\RES_{SYSTEM_FIRMWARE}&REV_1, UEFI\RES_{SYSTEM_FIRMWARE} |
| UEFI\RES_{DEVICE_FIRMWARE}\0 | UEFI\RES_{DEVICE_FIRMWARE}&REV_1, UEFI\RES_{DEVICE_FIRMWARE} |

Notice that two hardware IDs are reported by each firmware resource device. The first hardware ID includes the current firmware resource version, while the second one does not. 

Since the firmware resource version is expected to change as a result of applying a firmware update, it is important that a driver be targeted for the second un-versioned hardware ID so that it can be applicable for installation across all firmware resource versions, no matter which version is currently present on a given system.

## Related topics

[ESRT table definition](esrt-table-definition.md)  

[Authoring an update driver package](authoring-an-update-driver-package.md)  

[Processing updates](processing-updates.md)  

[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  

[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  

[Firmware update status](firmware-update-status.md)  
