---
title: Driver Store
description: Driver Store
ms.date: 11/29/2021
ms.localizationpriority: medium
---

# Driver Store

Starting with Windows Vista, the Driver Store is a trusted collection of inbox and third-party [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the Driver Store can be installed on a device.

When a driver package is copied to the Driver Store, all of its files are copied. This includes the [INF file](overview-of-inf-files.md) and all files that are referenced by the INF file. All files that are in the driver package are considered critical to the device installation. The INF file must reference all of the required files for device installation so that they are present in the Driver Store. If the INF file references a file that is not included in the driver package, the driver package is not copied to the store.

The process of copying a driver package to the Driver Store is called *staging*. A driver package must be *staged* to the Driver Store before the package can be used to install any devices. As a result, driver staging and device installation are separate operations.

A driver package is staged to the Driver Store by being verified and validated.

## Verifying the driver package integrity

Before a driver package is staged to the Driver Store, the operating system first verifies that the driver package is trusted. In order for the driver package to be considered trusted, the [INF file](overview-of-inf-files.md) must have a *CatalogFile* directive in the [**Version**](inf-version-section.md) section that provides the file name for a [catalog file](catalog-files.md) that is associated with the INF file. The catalog file must contain hashes for the INF file and any files that are referenced by the INF file and the catalog file must be signed with a trusted digital signature.  For more information about digital signatures, see [Driver Signing](driver-signing.md). 

## Validating the driver package

The operating system validates the driver package in the following ways:

- The current user must have permission to install the driver package.
- The [INF file](overview-of-inf-files.md) of the driver package is syntactically correct, and all files referenced by the INF files are present in the driver package.

After a driver package has passed integrity and syntax checks, it is copied to the Driver Store. Afterwards, the operating system uses the driver package to automatically install new devices without requiring user interaction.

Once files are staged to the Driver Store, they should not be removed or modified in any way. Additionally, new files should not be added to the Driver Store outside of the staging process. This includes files being added, removed, or modified directly through programmatic calls, or indirectly through INF directives that will be processed at a later time.
