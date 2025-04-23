---
title: Driver Store
description: The Driver Store is a trusted collection of inbox and non-Microsoft driver packages.
ms.date: 04/16/2025
---

# Driver store

The Driver Store is a trusted collection of inbox and non-Microsoft [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the Driver Store can be installed on a device.

When a driver package is copied to the Driver Store, all of its files are copied. These files include the [INF file](overview-of-inf-files.md) and all files referenced by the INF file. All files that are in the driver package are considered critical to the device installation. The INF file must reference all of the required files for device installation so that they're present in the Driver Store. If the INF file references a file that isn't included in the driver package, the driver package isn't copied to the store.

The process of copying a driver package to the Driver Store is called *staging*. A driver package must be *staged* to the Driver Store before the package can be used to install any devices. As a result, driver staging and device installation are separate operations.

A driver package is staged to the Driver Store by being verified and validated.

## Verifying the driver package integrity

Before a driver package is staged to the Driver Store, the operating system first verifies that the driver package is trusted. In order for the driver package to be considered trusted, the [INF file](overview-of-inf-files.md) must have a *CatalogFile* directive in the [**Version**](inf-version-section.md) section that provides the file name for a [catalog file](catalog-files.md) that is associated with the INF file. The catalog file must contain hashes for the INF file and any files referenced in the INF file. The catalog file must be signed with a trusted digital signature. For more information about digital signatures, see [Driver Signing](driver-signing.md).

## Validating the driver package

The operating system validates the driver package in the following ways:

- The current user must have permission to install the driver package.
- The [INF file](overview-of-inf-files.md) of the driver package is syntactically correct, and all files referenced by the INF files are present in the driver package.

A driver is copied to the Driver Store after it passes integrity and syntax checks. Afterwards, the operating system uses the driver package to automatically install new devices without requiring user interaction.

Once files are staged to the Driver Store, they shouldn't be removed or modified in any way. New files must not be added to the Driver Store outside of the staging process. This includes adding, removing, or modifying files directly through programmatic calls. It also includes changes made indirectly through INF directives processed later.
