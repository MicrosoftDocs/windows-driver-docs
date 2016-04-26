---
title: Processing updates
author: windows-driver-content
description: After any firmware update package(s) have been applied and the system subsequently rebooted, the Windows OS loader loads all the firmware payload files (in this example, firmware.bin) into physical memory.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 87BC1366-F69D-412A-883E-861853A4902A
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Processing%20updates%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


