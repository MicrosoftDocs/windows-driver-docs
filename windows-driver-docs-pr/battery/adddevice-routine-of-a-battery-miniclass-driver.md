---
title: AddDevice routine for battery miniclass drivers
description: Discover the AddDevice routine and its role in initializing battery-specific state for battery miniclass drivers.
keywords:
- AddDevice routine WDK battery
- battery miniclass drivers WDK, routines
ms.date: 10/04/2023
---

# AddDevice routine for battery miniclass drivers

Every battery miniclass driver must have an [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine to initialize battery-specific state. The PnP Manager calls the AddDevice routine for each battery device controlled by this miniclass driver.

In addition to the tasks required of a PnP AddDevice routine, the AddDevice routine for a battery miniclass driver must also:

1. Create an FDO for the battery and attach the FDO to the device stack for the controller.
1. Initialize the [BATTERY_MINIPORT_INFO](/windows/win32/api/batclass/ns-batclass-battery_miniport_info) structure and call [BatteryClassInitializeDevice](/windows/win32/api/batclass/nf-batclass-batteryclassinitializedevice) to register the miniclass driver with the battery class driver.
1. Perform any other required initialization for the device.
