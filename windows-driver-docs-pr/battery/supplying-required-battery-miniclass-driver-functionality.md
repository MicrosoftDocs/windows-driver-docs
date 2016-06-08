---
title: Supplying Required Battery Miniclass Driver Functionality
description: Supplying Required Battery Miniclass Driver Functionality
ms.assetid: d33d3c8c-f867-40dc-901c-6b0dd5d57dac
keywords: ["battery miniclass drivers WDK , routines", "routines WDK battery", "battery miniclass drivers WDK , functionality"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Supplying%20Required%20Battery%20Miniclass%20Driver%20Functionality%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




