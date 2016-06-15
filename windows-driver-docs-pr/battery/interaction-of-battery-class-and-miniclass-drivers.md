---
title: Interaction of Battery Class and Miniclass Drivers
description: Interaction of Battery Class and Miniclass Drivers
ms.assetid: bf35a034-1bb9-4106-aafe-7692d0ff92d0
keywords: ["battery miniclass drivers WDK , battery class driver interaction", "battery class drivers WDK , battery miniclass driver interaction"]
---

# Interaction of Battery Class and Miniclass Drivers


## <span id="ddk_interaction_of_battery_class_and_miniclass_drivers_dg"></span><span id="DDK_INTERACTION_OF_BATTERY_CLASS_AND_MINICLASS_DRIVERS_DG"></span>


Together, the battery class driver and the miniclass driver manage the computer's use of a battery. The following figure shows how these two drivers interact.

![diagram illustrating the interaction of battery class and miniclass drivers](images/battmini.png)

The miniclass driver is the primary function driver for the devices it controls. It receives IRPs from the power manager through the composite battery driver and calls support routines in the battery class driver to register its devices, to report status, and to handle certain system-defined battery IOCTLs.

The class driver receives information and status from all the miniclass drivers and reports it to the power manager through the composite battery driver. In response to battery IOCTLs, the class driver calls [battery miniclass driver routines](https://msdn.microsoft.com/library/windows/hardware/ff536286) (BatteryMini*Xxx* routines) in the miniclass drivers to perform specific device control operations. Additionally, applications such as the power meter can send [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests to a miniclass driver to get information about a specific battery.

The class driver is designed to handle the superset of possible battery information and conditions, including temperature, changes in capacity, and so forth; individual batteries vary in their ability to detect and report all these conditions. Each miniclass driver should be designed to manage its specific battery type and must respond appropriately to the class driver when asked for any information that the battery does not support.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Interaction%20of%20Battery%20Class%20and%20Miniclass%20Drivers%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


