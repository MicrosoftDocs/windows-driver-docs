---
title: Firmware user experience (UX) best practices
description: Provides information about firmware user experience (UX) best practices.
ms.date: 03/23/2023
---

# Firmware user experience (UX) best practices

A firmware update to a system can be important to the continued use of that machine. Microsoft wants to ensure that firmware updates are safely delivered, and installation is uninterrupted. To do this, we have recommended the following guidelines that are described in greater detail in the **Related resources** section.

1. Progress bar/indicator that the system is installing an update.

1. Windows Boot loader with **UpdateCapsule** function will provide a bitmap containing message for user.

1. UEFI check for AC Power, or sufficient battery life (RSOC) or fail out with error codes recorded in ESRT.

The **Related resources** links contain the most recent information on firmware UX guidance.

## Related resources

[Windows UEFI firmware update platform](./windows-uefi-firmware-update-platform.md)

[Seamless crisis prevention and recovery](./seamless-crisis-prevention-and-recovery.md)

[User experience for UEFI firmware updates](./user-experience-for-uefi-firmware-updates.md)

[Boot screen components](./boot-screen-components.md)

[ESRT table definition](./esrt-table-definition.md)

[Validating Windows UEFI Firmware Update Platform Functionality](/windows-hardware/manufacture/desktop/validating-windows-uefi-firmware-update-platform-functionality)
