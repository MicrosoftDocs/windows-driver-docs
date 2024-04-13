---
title: Writing Battery Miniclass Drivers
description: Writing Battery Miniclass Drivers
keywords:
- battery miniclass drivers WDK
- battery miniclass drivers WDK , about writing battery miniclass drivers
- device-independent battery support WDK
- device-specific battery support WDK
- battery class drivers WDK
- battery class drivers WDK , about battery class drivers
ms.date: 04/20/2017
---

# Writing Battery Miniclass Drivers

A battery typically has a pair of drivers: the generic battery class driver that Microsoft provides, and a miniclass driver written specifically for that individual type of battery.

The class driver defines the overall functionality of the batteries in the system and interacts with the power manager.

The miniclass driver handles device-specific functions such as adding and removing a battery, and keeping track of its capacity and charge. The miniclass driver exports routines that the class driver calls to get information about the devices it controls.

Information about writing battery miniclass drivers is organized as follows:

[Overview of System Battery Management](overview-of-system-battery-management.md)

[Interaction of Battery Class and Miniclass Drivers](interaction-of-battery-class-and-miniclass-drivers.md)

[Supplying Required Battery Miniclass Driver Functionality](supplying-required-battery-miniclass-driver-functionality.md)

[Battery miniclass driver: DriverEntry routine](driverentry-routine-of-a-battery-miniclass-driver.md)

[AddDevice routine for battery miniclass drivers](adddevice-routine-of-a-battery-miniclass-driver.md)

[Battery miniclass driver's DispatchDeviceControl routine](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl Routine of a Battery Miniclass Driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[Responding to Battery Class Driver Queries](responding-to-battery-class-driver-queries.md)

[Supplying Battery Device Notification](supplying-battery-device-notification.md)

[Unload Routine of a Battery Miniclass Driver](unload-routine-of-a-battery-miniclass-driver.md)

[Installing a Battery Driver](installing-a-battery-driver.md)
