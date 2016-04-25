---
title: Installing the update
description: Firmware update packages can be installed using any tool that installs Windows drivers.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 51C50910-8AA3-4ED9-B469-2325BBD2FB31
---

# Installing the update


Firmware update packages can be installed using any tool that installs Windows drivers. The installation process copies the firmware update payload (firmware.bin) to a well-known system directory and creates the registry keys necessary to tell Windows a new update is available. After the installation is finished, a reboot is required in order to trigger the actual firmware update process.

![](images/updateinstallprocess.png)

During the next boot, and before ExitBootServices() has been called, the OS Loader checks the well-known registry key locations to determine if new firmware update payload is available. If new update payload is available, the OS Loader verifies the hash of firmware.bin against the security catalog delivered with the driver package. If the signature is valid, the firmware.bin will be handed off to the platform firmware via the UEFI UpdateCapsule() service.

**Important**  At this point, the platform firmware is solely responsible for completing the firmware update.

 

If multiple firmware update packages are installed, the OS Loader calls UpdateCapsule() with the payload of each available update. Each firmware payload will be a separate capsule, each identified by the GUID of the ESRT entry for the targeted firmware update package.

The EFI System Resource Table provides the current firmware version and the status of the last update attempted. The OS Loader uses this information to assess whether the update was successfully applied. The firmware status information will be persisted into the OS such that it is available to a firmware update application running in Windows. Finally, the OS Loader continues the boot process.

## Related topics
[System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)  
[Populating the ESRT table](populating-the-esrt-table.md)  
[Customizing firmware for different geographic regions](customizing-firmware-for-different-geographic-regions.md)  
[Authoring a firmware update package](authoring-a-firmware-update-package.md)  
[Certifying and signing the update package](certifying-and-signing-the-update-package.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Installing%20the%20update%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


