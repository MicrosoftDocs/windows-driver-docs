---
title: Storage Filter Driver's DriverEntry Routine
description: Storage Filter Driver's DriverEntry Routine
keywords:
- storage filter drivers WDK , DriverEntry
- filter drivers WDK storage , DriverEntry
- SFD WDK storage , DriverEntry
- DriverEntry WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's DriverEntry Routine


## <span id="ddk_storage_filter_drivers_driverentry_routine_kg"></span><span id="DDK_STORAGE_FILTER_DRIVERS_DRIVERENTRY_ROUTINE_KG"></span>


Like any other kernel-mode driver, the [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine of an storage filter driver (SFD) must define its Dispatch and other entry points in the input driver object. If necessary, an SFD can allocate a driver object extension of appropriate size by calling [**IoAllocateDriverObjectExtension**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatedriverobjectextension), copy the input registry path into the driver extension for later use, and initialize the driver extension with other driver-determined data, if any.

For more information about a PnP driver's [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, see [Plug and Play](../kernel/introduction-to-plug-and-play.md).

