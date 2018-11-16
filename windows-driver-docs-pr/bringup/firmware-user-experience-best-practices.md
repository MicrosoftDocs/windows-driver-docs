---
title: Firmware user experience (UX) best practices
description: Firmware user experience (UX) best practices
ms.date: 05/15/2018
ms.localizationpriority: medium
---


# Firmware user experience (UX) best practices


A firmware update to a system can be important to the continued use of that machine. Microsoft wants to ensure that firmware updates are safely delivered, and installation is uninterrupted. To do this, we have recommended the following guidelines that are described in greater detail in the **Related resources** section.

1.  Progress bar/indicator that the system is installing an update.

2.  Windows Boot loader with **UpdateCapsule** function will provide a bitmap containing message for user.

3.  UEFI check for AC Power, or sufficient battery life (RSOC) or fail out with error codes recorded in ESRT.

The **Related resources** links contain the most recent information on firmware UX guidance.

## Related resources

[Windows UEFI firmware update platform](https://docs.microsoft.com/windows-hardware/drivers/bringup/windows-uefi-firmware-update-platform)

[Seamless crisis prevention and recovery](https://docs.microsoft.com/windows-hardware/drivers/bringup/seamless-crisis-prevention-and-recovery)

[User experience for UEFI firmware updates](https://docs.microsoft.com/windows-hardware/drivers/bringup/user-experience-for-uefi-firmware-updates)

[Boot screen components](https://docs.microsoft.com/windows-hardware/drivers/bringup/boot-screen-components)

[ESRT table definition](https://docs.microsoft.com/windows-hardware/drivers/bringup/esrt-table-definition)

[Validating Windows UEFI Firmware Update Platform Functionality](https://docs.microsoft.com/windows-hardware/manufacture/desktop/validating-windows-uefi-firmware-update-platform-functionality)




