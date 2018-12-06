---
title: Storage Drivers
description: Storage Drivers
ms.assetid: 5512a8f1-20ad-4b78-a60e-7418ac7f2117
keywords:
- storage drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Drivers


## <span id="ddk_storage_drivers_kg"></span><span id="DDK_STORAGE_DRIVERS_KG"></span>


This section contains the following information:

[Storage Driver Architecture](storage-driver-architecture.md)

[Storage Drivers and Device Objects](storage-drivers-and-device-objects.md)

[System Header Files for Storage Drivers](system-header-files-for-storage-drivers.md)

[Restrictions on Pageable Code in Storage Drivers](restrictions-on-pageable-code-in-storage-drivers.md)

[Querying for the Write Cache Property](querying-for-the-write-cache-property.md)

[Device Unique Identifiers for Storage Devices (DUIDs)](device-unique-identifiers--duids--for-storage-devices.md)

Subsequent sections contain guidelines for designing the following kinds of Windows kernel-mode storage drivers:

-   An operating system-independent miniport driver for a vendor-specific SCSI HBA (see [SCSI Miniport Drivers](scsi-miniport-drivers.md))

-   A miniport driver for a non-SCSI storage adapter (see [SCSI Miniport Drivers](scsi-miniport-drivers.md))

-   A class driver for a new type of peripheral device (see [Storage Class Drivers](storage-class-drivers.md))

-   An operating system-independent tape miniclass driver for a vendor-specific tape device (see [Tape Drivers](tape-drivers.md))

-   A changer miniclass driver for a vendor-specific medium changer device (see [Changer Drivers](changer-drivers.md))

-   A filter driver for a peripheral device of a type that already has a class driver (see [Storage Filter Drivers](storage-filter-drivers.md))

 

 




