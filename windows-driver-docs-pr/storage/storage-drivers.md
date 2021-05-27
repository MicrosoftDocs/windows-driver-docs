---
title: About Storage Drivers
description: Storage Drivers
keywords:
- storage drivers WDK
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# About Storage Drivers

This section of the Storage Driver Design Guide contains the following information:

[Storage Driver Architecture](storage-driver-architecture.md)

[Storage Drivers and Device Objects](storage-drivers-and-device-objects.md)

[System Header Files for Storage Drivers](system-header-files-for-storage-drivers.md)

[Restrictions on Pageable Code in Storage Drivers](restrictions-on-pageable-code-in-storage-drivers.md)

[Querying for the Write Cache Property](querying-for-the-write-cache-property.md)

[Device Unique Identifiers for Storage Devices (DUIDs)](device-unique-identifiers--duids--for-storage-devices.md)

[General Storage I/O Control Codes](general-storage-io-control-codes.md)

Subsequent sections contain guidelines for designing the following kinds of Windows kernel-mode storage drivers:

- An operating system-independent miniport driver for a vendor-specific SCSI HBA (see [SCSI Miniport Drivers](scsi-miniport-drivers.md))

- A miniport driver for a non-SCSI storage adapter (see [SCSI Miniport Drivers](scsi-miniport-drivers.md))

- A class driver for a new type of peripheral device (see [Storage Class Drivers](introduction-to-storage-class-drivers.md))

- An operating system-independent tape miniclass driver for a vendor-specific tape device (see [Tape Drivers](tape-drivers-overview.md))

- A changer miniclass driver for a vendor-specific medium changer device (see [Changer Drivers](changer-drivers.md))

- A filter driver for a peripheral device of a type that already has a class driver (see [Storage Filter Drivers](storage-filter-drivers.md))
