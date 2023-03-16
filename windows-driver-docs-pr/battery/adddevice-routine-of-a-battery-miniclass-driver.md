---
title: AddDevice Routine of a Battery Miniclass Driver
description: AddDevice Routine of a Battery Miniclass Driver
keywords:
- AddDevice routine WDK battery
- battery miniclass drivers WDK , routines
ms.date: 04/20/2017
---

# AddDevice Routine of a Battery Miniclass Driver

Every battery miniclass driver must have an [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, which initializes battery-specific state. The PnP Manager calls the *AddDevice* routine for each battery device controlled by this miniclass driver.

In addition to the tasks required of a PnP *AddDevice* routine, the *AddDevice* routine for a battery miniclass driver must also do the following:

1. Create an FDO for the battery and attach the FDO to the device stack for the controller.

2. Initialize the [**BATTERY\_MINIPORT\_INFO**](/windows/win32/api/batclass/ns-batclass-battery_miniport_info) structure and call [**BatteryClassInitializeDevice**](/windows/win32/api/batclass/nf-batclass-batteryclassinitializedevice) to register the miniclass driver with the battery class driver.

3. Perform any other initialization required for the device.
