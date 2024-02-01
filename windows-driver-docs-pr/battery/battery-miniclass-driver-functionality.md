---
title: Battery Miniclass Driver Functionality
description: Discover the responsibilities and functions of a battery miniclass driver, including managing battery capacity, charge, and power state.
keywords:
- battery miniclass drivers WDK, functionality
ms.date: 10/04/2023
---

# Battery miniclass driver functionality

A battery miniclass driver is responsible for:

- Creating a functional device object (FDO) for its devices and storing device-specific information in the associated device extension
- Assigning and maintaining the battery tag for the current battery
- Keeping track of battery capacity, charge, and power state
- Responding to requests from the class driver for battery status information
- Notifying the battery class driver when the power state of the battery changes
- Charging or discharging a specific battery when requested

A battery miniclass driver calls the battery class driver's support routines for other operations, such as handling IOCTLs, as described in [Battery class driver functionality](battery-class-driver-functionality.md).

Every battery miniclass driver provides a set of [BatteryMini*Xxx*](/windows-hardware/drivers/ddi/_battery/) routines. The battery class driver calls these routines to request that the miniclass driver perform device-specific tasks. In addition, the miniclass driver must have other routines, as described in [Supplying required battery miniclass driver functionality](supplying-required-battery-miniclass-driver-functionality.md).
