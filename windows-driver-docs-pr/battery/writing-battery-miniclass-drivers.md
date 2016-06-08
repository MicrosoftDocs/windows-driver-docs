---
title: Writing Battery Miniclass Drivers
description: Writing Battery Miniclass Drivers
ms.assetid: 4135af1a-1448-46ad-af6f-26ce8aee6b1d
keywords: ["battery miniclass drivers WDK", "battery miniclass drivers WDK , about writing battery miniclass drivers", "device-independent battery support WDK", "device-specific battery support WDK", "battery class drivers WDK", "battery class drivers WDK , about battery class drivers"]
---

# Writing Battery Miniclass Drivers


## <span id="ddk_writing_battery_miniclass_drivers_dg"></span><span id="DDK_WRITING_BATTERY_MINICLASS_DRIVERS_DG"></span>


A battery typically has a pair of drivers: the generic battery class driver that Microsoft provides, and a miniclass driver written specifically for that individual type of battery.

The class driver defines the overall functionality of the batteries in the system and interacts with the power manager.

The miniclass driver handles device-specific functions such as adding and removing a battery, and keeping track of its capacity and charge. The miniclass driver exports routines that the class driver calls to get information about the devices it controls.

Information about writing battery miniclass drivers is organized as follows:

[Overview of System Battery Management](overview-of-system-battery-management.md)

[Interaction of Battery Class and Miniclass Drivers](interaction-of-battery-class-and-miniclass-drivers.md)

[Supplying Required Battery Miniclass Driver Functionality](supplying-required-battery-miniclass-driver-functionality.md)

[DriverEntry Routine of a Battery Miniclass Driver](driverentry-routine-of-a-battery-miniclass-driver.md)

[AddDevice Routine of a Battery Miniclass Driver](adddevice-routine-of-a-battery-miniclass-driver.md)

[DispatchDeviceControl Routine of a Battery Miniclass Driver](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl Routine of a Battery Miniclass Driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[Responding to Battery Class Driver Queries](responding-to-battery-class-driver-queries.md)

[Supplying Battery Device Notification](supplying-battery-device-notification.md)

[Unload Routine of a Battery Miniclass Driver](unload-routine-of-a-battery-miniclass-driver.md)

[Installing a Battery Driver](installing-a-battery-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Writing%20Battery%20Miniclass%20Drivers%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




