---
title: Storage Filter Driver's AddDevice Routine
description: Storage Filter Driver's AddDevice Routine
keywords:
- storage filter drivers WDK , AddDevice
- filter drivers WDK storage , AddDevice
- SFD WDK storage , AddDevice
- AddDevice routine WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's AddDevice Routine

The PnP manager calls the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine of a storage filter driver when it detects a device controlled by that driver. The *AddDevice* routine of an storage filter driver (SFD) is similar to that of a storage class driver, except that it must not attempt to claim the device (SRB_FUNCTION_CLAIM_DEVICE).

For information about a storage class driver's [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, see [Storage Class Drivers](introduction-to-storage-class-drivers.md). For general information about a PnP driver's *AddDevice* routine, see [Plug and Play](../kernel/introduction-to-plug-and-play.md).
