---
title: Battery Devices Design Guide
description: Battery Devices Design Guide
ms.assetid: d8eecfcb-6c06-40d1-8c78-b8c88eb890f2
---

# Battery Devices Design Guide


## <span id="ddk_design_guide_battery_devices_dg"></span><span id="DDK_DESIGN_GUIDE_BATTERY_DEVICES_DG"></span>


A battery typically has a pair of drivers: the generic battery class driver that Microsoft provides, and a miniclass driver written specifically for that individual type of battery.

The class driver defines the overall functionality of the batteries in the system and interacts with the power manager.

This design guide focuses on [Writing Battery Miniclass Drivers](writing-battery-miniclass-drivers.md).

In addition this section includes information on [Writing UPS Minidrivers](writing-ups-minidrivers.md) that were used with older versions of Windows.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Battery%20Devices%20Design%20Guide%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




