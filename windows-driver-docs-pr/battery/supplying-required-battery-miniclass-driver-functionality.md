---
title: Supplying Required Battery Miniclass Driver Functionality
description: Supplying Required Battery Miniclass Driver Functionality
ms.assetid: d33d3c8c-f867-40dc-901c-6b0dd5d57dac
keywords:
- battery miniclass drivers WDK , routines
- routines WDK battery
- battery miniclass drivers WDK , functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supplying Required Battery Miniclass Driver Functionality


## <span id="ddk_supplying_required_battery_miniclass_driver_functionality_dg"></span><span id="DDK_SUPPLYING_REQUIRED_BATTERY_MINICLASS_DRIVER_FUNCTIONALITY_DG"></span>


In addition to the routines required to support [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125), a battery miniclass driver must have the following routines:

[DriverEntry](driverentry-routine-of-a-battery-miniclass-driver.md)

[AddDevice](adddevice-routine-of-a-battery-miniclass-driver.md)

[DispatchDeviceControl](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275)

[*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274)

[*BatteryMiniQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536273)

[*BatteryMiniSetInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536276)

[*BatteryMiniSetStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536277)

[*BatteryMiniDisableStatusNotify*](https://msdn.microsoft.com/library/windows/hardware/ff536272)

[Unload](unload-routine-of-a-battery-miniclass-driver.md)

[DriverEntry](driverentry-routine-of-a-battery-miniclass-driver.md), [Unload](unload-routine-of-a-battery-miniclass-driver.md), [DispatchDeviceControl](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md), and [AddDevice](adddevice-routine-of-a-battery-miniclass-driver.md) are standard driver routines. The name DriverEntry is required, so that the operating system can call it upon starting the driver. You can choose names for the other driver routines at your discretion, as long as their addresses are loaded properly in the appropriate data structures.

The [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routines are supplied by the miniclass driver and called by the battery class driver. When writing a miniclass driver, you can choose not to implement the functionality of any of these routines; however, an entry point for the routine must nevertheless be provided, and the routine must return STATUS\_NOT\_SUPPORTED. Prototypes for these routines appear in Batclass.h.

Battery miniclass drivers must include the following header files:

-   Batclass.h

-   Ntddk.h or Wdm.h

 

 




