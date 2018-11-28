---
title: Processing updates
description: After any firmware update package(s) have been applied and the system subsequently rebooted, the Windows OS loader loads all the firmware payload files (in this example, firmware.bin) into physical memory.
ms.assetid: 87BC1366-F69D-412A-883E-861853A4902A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing updates


After any firmware update package(s) have been applied and the system subsequently rebooted, the Windows OS loader loads all the firmware payload files (in this example, *firmware.bin*) into physical memory. The Windows OS loader creates capsule headers using the information from each update’s corresponding ESRT entry, which describes the GUID and flags to use when calling UEFI UpdateCapsule. In setting each capsule header’s flags field, the Windows OS loader always sets CAPSULE\_FLAGS\_PERSIST\_ACROSS\_RESET and CAPSULE\_FLAGS\_INITIATE\_RESET. The Windows OS loader may additionally set CAPSULE\_FLAGS\_POPULATE\_SYSTEM\_TABLE for firmware types DEVICE\_FIRMWARE, if the capsule flag was specified in the INF for the driver package. Proprietary capsule flags may also be specified in the INF and when specified will additionally be included when calling UEFI UpdateCapsule

Referring back to the ESRT example in [ESRT table definition](esrt-table-definition.md) and the firmware resource update driver package INF example in [Authoring an update driver package](authoring-an-update-driver-package.md), the capsule headers the Windows OS loader creates to pass into UpdateCapsule would be as follows.

| Field            | Value              | Comment                                                 |
|------------------|--------------------|---------------------------------------------------------|
| CapsuleGuid      | {SYSTEM\_FIRMWARE} | From corresponding ESRT resource entry’s FirmwareClass. |
| HeaderSize       | …                  | Padded to page-align *firmware.bin* start.              |
| Flags            | 0x50000            | Persist across, and initiate, reset.                    |
| CapsuleImageSize | …                  | Capsule Header Size + The size of *firmware.bin*.       |

 

Note that in this example only one of the two devices defined in the ESRT table has installed a new firmware resource update driver package. If a firmware resource update driver package were authored for the second device in Table 2 and then installed on the corresponding firmware resource device, a second capsule header would be created as follows:

| Field            | Value              | Comment                                                                                                                                 |
|------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| CapsuleGuid      | {DEVICE\_FIRMWARE} | From corresponding ESRT resource entry’s FirmwareClass.                                                                                 |
| HeaderSize       | …                  | Padded to page-align DEVICE.BIN start.                                                                                                  |
| Flags            | 0x50000            | Persist across, and initiate, reset, and populate system table, OR’d with 0x8010 from corresponding ESRT resource entry’s CapsuleFlags. |
| CapsuleImageSize | …                  | Capsule Header Size + The size of DEVICE.BIN.                                                                                           |

 

After the Windows OS loader has loaded all pending firmware updates and created the necessary data structures to describe them, it then calls the UpdateCapsule run-time service, prior to calling ExitBootServices.

**Note**  UpdateCapsule is called prior to ExitBootServices when platform firmware has exclusive control of all devices including the storage device. A platform firmware implementation of UpdateCapsule can save firmware update payloads to persistent storage to stage an update or to support a recovery rollback.

 

## Related topics
[ESRT table definition](esrt-table-definition.md)  
[Plug and play device](plug-and-play-device.md)  
[Authoring an update driver package](authoring-an-update-driver-package.md)  
[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  
[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  
[Firmware update status](firmware-update-status.md)  



