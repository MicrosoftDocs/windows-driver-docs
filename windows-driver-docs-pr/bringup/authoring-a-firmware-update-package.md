---
title: Authoring a firmware update package
description: Each firmware update package includes a single binary file that contains the entire firmware payload (for example firmware.bin) and a security catalog that Windows uses to validate firmware.bin.
ms.assetid: 672F5E45-C0AB-4C19-BB0A-C8B5A66D8EED
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authoring a firmware update package


Each firmware update package includes a single binary file that contains the entire firmware payload (for example firmware.bin) and a security catalog that Windows uses to validate firmware.bin. For more information about security catalogs and drivers, see [Catalog Files and Digital Signatures](https://msdn.microsoft.com/library/windows/hardware/ff537872) and [Creating a Catalog File for a PnP Driver Package](https://msdn.microsoft.com/library/windows/hardware/ff540161).

Firmware update packages must be capable of updating one or more of the following types of firmware:

-   The UEFI system firmware.
-   The firmware for a single device in the system.

It is recommended that each firmware update package target a single firmware resource (UEFI system firmware or a single device), but there may be circumstances where it is advantageous to have a single firmware update package that updates both system firmware and one or more devices.

**Note**  A device cannot be targeted by more than one firmware update package. If a device is targeted by a firmware update package which also includes system firmware, it cannot be targeted by a second firmware update package which only targets the device.

 

1.  To allow a firmware update package to target a firmware update to the appropriate system hardware, Windows surfaces a device instance for each entry in the ESRT, where such a device instance exposes a Hardware ID that identifies it as belonging to the ESRT entry.

2.  When a firmware update package is installed, it is processed by Windows as a driver package. Windows will copy the firmware payload of each update package to a safe location under the System directory, prepare the system to perform the firmware updates and trigger the system to restart.

    Windows does not support dependencies between driver packages. Therefore, the following requirements must be observed when authoring a new firmware update package:

    -   A firmware update package must be capable of successful installation on its own and without dependency on other device firmware, system firmware, or other firmware update packages.
    
    -   It is recommended that each update package is targeted to a single device on the system or to the UEFI system firmware (defined in the ESRT).
    
    -   Each update package must contain a single firmware update binary (for example firmware.bin).

3.  The firmware update payload in each update package needs to be contained in a single binary file. Upon system reboot, the OS loader loads each firmware update binary file for each firmware update package into physical memory and builds an array of pointers to each payload file provisioned for installation (the UEFI 2.3.1 specification refers to this array as the CapsuleHeaderArray).

4.  This array is passed in the call to the EFI UpdateCapsule() function. UpdateCapsule() is used as a mailbox, passing each driver package’s firmware update payload to the platform firmware.

5.  Each capsule (a firmware update payload) is identified by the firmware ID specified by the ESRT entry for a firmware resource.

6.  Upon receipt of each firmware update payload, the firmware update request is processed and applied when applicable.

    Each entry in the CapsuleHeaderArray is a single, contiguous block of data containing the firmware update payload from a firmware driver package for a single device in the system. For each targeted firmware resource, the firmware update payload must contain the firmware image and all information required by the platform for validation.

    The firmware payload for all firmware update driver packages are passed to platform firmware through the UEFI UpdateCapsule service. Since integrated devices will be sourced from a variety of different IHVs, the system OEM (and possibly the SoC manufacturer) will need to work directly with these IHVs to ensure device firmware updates are authored appropriately for the given system. Additionally, the system OEM needs to ensure that the ESRT entries allow UpdateCapsule packages to be targeted to the appropriate systems.

    For example, several OEMs might choose the same model Mobile Broadband (MBB) device for their systems. Even though the MBB device is identical in each system, each OEM must collaborate with the MBB IHV to author a firmware update package customized for their system. This level of customization of the device firmware update is necessary to address variables across OEM systems.

    -   Addressing the device may differ based on the SoC chosen by the OEM and how the device is connected to the SoC.
    
    -   The system OEM may sell the system to multiple Mobile Network Operators (MNOs) for resale to consumers. The MBB device must be MNO-aware, requiring the firmware to be both customized and certified to a particular MNO’s requirements.
    
    -   The system may be sold in multiple markets worldwide, each with different RF regulations and radio frequency assignments. The MBB device firmware may require customization to meet these market requirements.

    Each OEM must carefully consider such device-specific requirements, and take necessary steps to ensure that device firmware can be targeted and updated appropriately. This requires careful management of ESRT entries to ensure device firmware can be properly deployed.

7.  After the update package is authored, it needs to be submitted to Microsoft for certification and signing.

## Related topics
[System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)  
[Populating the ESRT table](populating-the-esrt-table.md)  
[Customizing firmware for different geographic regions](customizing-firmware-for-different-geographic-regions.md)  
[Certifying and signing the update package](certifying-and-signing-the-update-package.md)  
[Installing the update](installing-the-update.md)  



