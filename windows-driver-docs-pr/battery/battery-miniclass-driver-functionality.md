---
title: Battery Miniclass Driver Functionality
description: Battery Miniclass Driver Functionality
ms.assetid: f8da63fd-0bf9-4085-88c2-022c4ddc7caa
keywords: ["battery miniclass drivers WDK , functionality"]
---

# Battery Miniclass Driver Functionality


## <span id="ddk_battery_miniclass_driver_functionality_dg"></span><span id="DDK_BATTERY_MINICLASS_DRIVER_FUNCTIONALITY_DG"></span>


A battery miniclass driver is responsible for the following:

-   Creating an FDO for its devices and storing device-specific information in the associated device extension

-   Assigning and maintaining the battery tag for the current battery

-   Keeping track of battery capacity, charge, and power state

-   Responding to requests from the class driver for battery status information

-   Notifying the battery class driver when the power state of the battery changes

-   Charging or discharging a specific battery when requested

A battery miniclass driver calls the battery class driver's support routines for other operations, such as handling IOCTLs, as described in [Battery Class Driver Functionality](battery-class-driver-functionality.md).

Every battery miniclass driver provides a set of [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routines. The battery class driver calls these routines to request that the miniclass driver perform device-specific tasks. In addition, the miniclass driver must have other routines, as described in [Supplying Required Battery Miniclass Driver Functionality](supplying-required-battery-miniclass-driver-functionality.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Battery%20Miniclass%20Driver%20Functionality%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




