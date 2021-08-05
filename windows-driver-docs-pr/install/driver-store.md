---
title: Driver Store
description: Driver Store
ms.date: 08/05/2021
ms.localizationpriority: medium
---

# Driver Store

Starting with Windows Vista, the driver store is a trusted collection of inbox and third-party [driver packages](driver-packages.md). The operating system maintains this collection in a secure location on the local hard disk. Only the driver packages in the driver store can be installed for a device.

When a driver package is copied to the driver store, all of its files are copied. This includes the [INF file](overview-of-inf-files.md) and all files that are referenced by the INF file. All files that are in the driver package are considered critical to the device installation. The INF file must reference all of the required files for device installation so that they are present in the driver store. If the INF file references a file that is not included in the driver package, the driver package is not copied to the store.

The process of copying a driver package to the driver store is called *staging*. A driver package must be *staged* to the driver store before the package can be used to install any devices. As a result, driver staging and device installation are separate operations.

A driver package is staged to the driver store by being verified and validated.

## Verifying the driver package integrity

Software integrity has become a top priority for Independent Hardware Vendors (IHVs) and Original Equipment Manufacturers (OEMs). Concerned by the increase in malicious software on the Internet, these customers want to be sure that their software has not been tampered with or corrupted.

Before a driver package is copied to the driver store, the operating system first verifies that the digital signature is correct. For more information about digital signatures, see [Driver Signing](driver-signing.md).

## Validating the driver package

The operating system validates the driver package in the following ways:

- The current user must have permission to install the driver package.
- The [INF file](overview-of-inf-files.md) of the driver package is syntactically correct, and all files referenced by the INF files are present in the driver package.

After a driver package has passed integrity and syntax checks, it is copied to the driver store. Afterwards, the operating system uses the driver package to automatically install new devices without requiring user interaction.

Once files are staged to the driver store, they should not be removed or modified in any way. Additionally, new files should not be added to the driver store outside of the staging process. This includes files being added, removed, or modified directly through programmatic calls, or indirectly through INF directives that will be processed at a later time.
