---
title: Driver Packages
description: Driver Packages
ms.date: 12/09/2021
ms.localizationpriority: High
---

# Driver Packages

A *driver package* consists of a set of software components to support a device under Windows. If you plan to design and build a new device, follow industry hardware standards. When you follow these standards, you are more likely to have a streamlined development process as well as lower your support costs. Not only do test suites exist for such devices, but, in many cases, generic driver packages exist for standard types. Therefore, you might not have to write a new driver package.

All devices on a Windows system should have a driver package installed on them.  The system provides some generic driver packages that can be installed on some classes of devices. For devices that do not have driver packages provided by the system, a vendor should provide a driver package to install on the device to support it under Windows. For a device that is covered by a system provided driver package, a vendor may choose to provide a better matching driver package to install on the device to provide enhanced functionality.

This section provides information to help you determine which components to supply within your driver package.

## In this section

-   [Components of a Driver Package](components-of-a-driver-package.md)
-   [Installation Component Overview](installation-component-overview.md)
-   [Sample Device Installation Files](sample-device-installation-files.md)