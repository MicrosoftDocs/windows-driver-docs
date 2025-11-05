---
title: "Windows UEFI Firmware Update Platform: Implementation Guide"
description: Learn how to implement UEFI firmware updates for Windows systems using UpdateCapsule. Get implementation guidance for system and device firmware updates via driver packages.
ms.date: 11/04/2025
ms.topic: concept-article
---

# Windows UEFI firmware update platform

Windows supports a platform for installing system and device firmware updates through driver packages that use the UEFI UpdateCapsule function. This platform provides a consistent, reliable firmware update experience for SoC vendors and OEMs who build hardware platforms that run Windows.

**In this article, you'll learn:**

- How to implement UEFI firmware updates on Windows systems
- System requirements for firmware updates
- The difference between system and device firmware updates
- Implementation steps and user experience considerations

The UEFI firmware update platform guidance describes how to implement firmware updates on systems running Windows 8, Windows 8.1, and Windows 10 for desktop editions (Home, Pro, Enterprise, and Education). This implementation improves the discoverability of important system firmware updates for end users.

## UEFI firmware update support in Windows 10

All systems that run Windows 10 for desktop editions should implement UEFI firmware updates by following the UpdateCapsule-based update process described in this section of the documentation.

## Overview of the UEFI firmware update platform

Windows can service two types of firmware:

- **System firmware**: Provides critical boot and runtime services to the system as a whole
- **Device firmware**: Associated with a particular device integrated into a system, typically working together with a device driver to expose the device to OS-level services and applications

### System firmware updates

You can deploy system firmware updates for UEFI-based systems as device driver packages (INFs). Windows uses information provided by the platform to ensure that the update package only applies to appropriate systems. A firmware update package contains a binary file with the system firmware image. After the firmware update package is on the end user's system, Windows uses the UEFI UpdateCapsule function to hand off the firmware payload to the platform firmware for processing.

Deploying the update as a driver package allows the firmware update process to align with many existing deployment and servicing tools, and ensures simple update package authoring for hardware vendors.

Although the firmware update is delivered as a driver package, the update isn't written as an actual driver. The driver package contains an INF file and a binary file with the system or device firmware image.

### Device firmware updates

For the purposes of updating device firmware, the device firmware can be assigned to one of these two categories:

- UEFI-updatable device firmware.

    This device firmware can be updated using a device driver package using the same mechanism as system firmware. A device firmware update is distributed as a firmware update package. After the firmware update package is on the end-user's system, Windows will use the UEFI UpdateCapsule function to hand-off the device firmware payload to the platform firmware for processing. This process is identical to how Windows hands off system firmware update payload, and is discussed below.

    It's recommended that device firmware is updated using a discrete firmware update driver package. However, device firmware may also be updated with system firmware as part of a single firmware update driver package.

    UEFI shouldn't be used to update peripheral devices. UEFI requires devices to be present during reboot to apply a firmware update that can't be guaranteed with (external, removable) peripheral devices.

- Driver-updatable device firmware.

    This device firmware can be updated by the device driver during the normal Windows OS runtime. Updating device firmware using normal Windows OS drivers isn't covered by this paper.

### System requirements for Windows firmware updates

Your system must meet these requirements to be compatible with Windows firmware updates:

1. **Implement UpdateCapsule and QueryCapsuleCapabilities**
   
   Required: [UEFI specification 2.8, section 8.5.3](https://uefi.org/specifications)
   
   UpdateCapsule passes the firmware update payload between Windows and the platform firmware.

2. **Support firmware updates initiated by Windows**
   
   System firmware and some device firmware must be updatable using this process. Your firmware code must recognize a firmware update payload passed to UpdateCapsule and initiate the update process.

3. **Specify a Firmware Resource in the EFI System Resource Table (ESRT)**
   
   The Firmware Resource enables Windows to:
   - Surface a device instance with a Hardware ID
   - Target system or device firmware updates to appropriate systems and devices
   - Describe the current firmware version and provide status for previous updates
   
   Requirements:
   - One entry for system firmware updates
   - All devices with updateable firmware must have an ESRT resource (unless updated as part of system firmware)
   
   **Next step:** Learn about [ESRT table definition](esrt-table-definition.md).

## Next steps

Choose the guide that matches your implementation stage:

- **[System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)** - Learn how to package and deploy firmware updates
  
- **[Implementing support for UEFI firmware updates](implementing-support-for-uefi-firmware-updates.md)** - Get step-by-step implementation guidance
  
- **[User experience for UEFI firmware updates](user-experience-for-uefi-firmware-updates.md)** - Understand the end-user update experience
