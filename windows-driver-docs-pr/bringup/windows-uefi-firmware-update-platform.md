---
title: Windows UEFI firmware update platform
description: Windows supports installing system and device firmware updates via driver packages that are processed using the UpdateCapsule function.
ms.date: 10/19/2022
---

# Windows UEFI firmware update platform

Windows supports a platform for installing system and device firmware updates via driver packages that are processed by using the UEFI UpdateCapsule function. This platform provides a consistent, reliable firmware update experience, and it improves the discoverability of important system firmware updates for end-users.

The UEFI firmware update platform guidance is intended for SoC vendors and OEMs who are building hardware platforms that run Windows. The UEFI firmware update platform is supported by the following operating system versions:

- Windows 8

- Windows 8.1

- Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)

## UEFI firmware update support in Windows 10

All systems that run Windows 10 for desktop editions should implement UEFI firmware updates by following the UpdateCapsule-based update process described in this section of the documentation.

## Overview of the UEFI firmware update platform

There are two types of firmware that can be serviced via Windows: system firmware and device firmware. System firmware is responsible for providing critical boot and runtime services to the system as a whole, and device firmware is associated with a particular device integrated into a system. Such device firmware typically works together with a device driver, allowing the OS to expose the device to OS-level services and applications.

### System firmware updates

System firmware updates for UEFI-based systems will be deployed as device driver packages (INFs). Windows will use information provided by the platform to ensure that the update package only applies to appropriate systems. A firmware update package contains a binary file containing the system firmware image. After the firmware update package is on the end-user's system, Windows will use the UEFI UpdateCapsule function to hand-off the firmware payload to the platform firmware for processing.

Deploying the update as a driver package allows the firmware update process to align with many existing deployment and servicing tools, and ensures simple update package authoring for hardware vendors.

> [!NOTE]
> Although the firmware update is delivered as a driver package, it does not mean that the update is written as an actual driver. The driver package will contain an INF file and a binary file containing the system or device firmware image.

### Device firmware updates

For the purposes of updating device firmware, the device firmware can be assigned to one of these two categories:

- UEFI-updatable device firmware.

    This device firmware can be updated using a device driver package using the same mechanism as system firmware. A device firmware update is distributed as a firmware update package. After the firmware update package is on the end-user's system, Windows will use the UEFI UpdateCapsule function to hand-off the device firmware payload to the platform firmware for processing. This process is identical to how Windows hands off system firmware update payload, and is discussed below.

    It's recommended that device firmware is updated using a discrete firmware update driver package. However, device firmware may also be updated with system firmware as part of a single firmware update driver package.

    > [!NOTE]
    > UEFI should not be used to update peripheral devices. UEFI requires devices to be present during reboot to apply a firmware update which cannot be guaranteed with (external, removable) peripheral devices.

- Driver-updatable device firmware.

    This device firmware can be updated by the device driver during the normal Windows OS runtime. Updating device firmware using normal Windows OS drivers isn't covered by this paper.

### System requirements for Windows firmware updates

In order for a system to be compatible with the Windows firmware updating mechanism, it must meet the following requirements:

- The system must implement UpdateCapsule and QueryCapsuleCapabilities as defined by section 8.5.3 of the [UEFI specification 2.8](https://uefi.org/specifications).

    UpdateCapsule is used to pass the firmware update payload between Windows and the platform firmware.

- Platform firmware must support firmware updates initiated by Windows.

    System firmware, and some classes of device firmware, must be updatable using this process. Firmware code recognizes a firmware update payload passed to UpdateCapsule and initiates the update process. The implementation is owned by the partner.

- Must specify a Firmware Resource in the EFI System Resource Table (ESRT)

    The Firmware Resource allows Windows to surface a device instance with a Hardware ID, which will be used to target the system or device firmware update to appropriate systems and devices. It also describes the current firmware version and provides status for previous updates.

    There exists a single entry for system firmware updates. All devices with updateable firmware must have a resource specified in the ESRT, unless a device's firmware is updated as part of a system firmware update.

    For more information, see [ESRT table definition](esrt-table-definition.md).

## In this section

- [System and device firmware updates via a firmware driver package](system-and-device-firmware-updates-via-a-firmware-driver-package.md)

- [Implementing support for UEFI firmware updates](implementing-support-for-uefi-firmware-updates.md)

- [User experience for UEFI firmware updates](user-experience-for-uefi-firmware-updates.md)
