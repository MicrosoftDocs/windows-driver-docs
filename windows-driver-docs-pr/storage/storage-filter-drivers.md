---
title: Storage Filter Drivers
description: Storage Filter Drivers
ms.assetid: 615e8ff1-d5b2-49da-b024-83bbaff70ded
keywords:
- storage filter drivers WDK
- filter drivers WDK storage
- storage drivers WDK , filter drivers
- SFD WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Drivers


## <span id="ddk_storage_filter_drivers_kg"></span><span id="DDK_STORAGE_FILTER_DRIVERS_KG"></span>


This section contains the following information:

[Storage Filter Driver's Support of I/O Requests](storage-filter-driver-s-support-of-i-o-requests.md)

[Storage Filter Driver's Device-Type-Specific Functionality](storage-filter-driver-s-device-type-specific-functionality.md)

[Storage Filter Driver's DriverEntry Routine](storage-filter-driver-s-driverentry-routine.md)

[Storage Filter Driver's AddDevice Routine](storage-filter-driver-s-adddevice-routine.md)

[Handling PnP Start in a Storage Filter Driver](handling-pnp-start-in-a-storage-filter-driver.md)

[Storage Filter Driver's Dispatch Routines](storage-filter-driver-s-dispatch-routines.md)

[Storage Filter Driver's IoCompletion Routines](storage-filter-driver-s-iocompletion-routines.md)

[Handling PnP Paging Requests](handling-pnp-paging-requests.md)

If a storage class driver already exists for a particular type of device, it might be unnecessary to write a driver for a new device of the same type. Each system-supplied storage class driver is designed to support peripheral devices of a given type and is tested against a number of vendors' devices. Thus, any system-supplied storage class driver might provide all the support another device of its type needs.

If an existing storage class driver does not fully support a new device of its type, a new driver can be written as a storage filter driver (SFD) layered over or under an existing system-supplied class driver. An SFD might transform data in read/write requests, define additional I/O control codes (IOCTLs) that enable a user application to take advantage of additional features of a particular device, or work around device-specific problems without requiring hardware-specific changes to the generic class or port drivers.

Unless a new device requires that every request be handled in a device-specific manner, a storage filter driver can be developed in far less time than a new storage class driver.

 

 




