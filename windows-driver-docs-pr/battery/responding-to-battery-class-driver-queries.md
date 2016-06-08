---
title: Responding to Battery Class Driver Queries
description: Responding to Battery Class Driver Queries
ms.assetid: 00b24b37-d312-46ee-8218-2bd7a9453d13
keywords: ["battery miniclass drivers WDK , routines", "routines WDK battery", "battery miniclass drivers WDK , status reporting", "status information WDK battery", "queries WDK battery"]
---

# Responding to Battery Class Driver Queries


## <span id="ddk_responding_to_battery_class_driver_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_CLASS_DRIVER_QUERIES_DG"></span>


The miniclass driver must provide the following three [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routines, which report battery status:

[*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275)

[*BatteryMiniQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536273)

[*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274)

The [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) routine in the class driver calls these miniclass driver routines when it receives IOCTLs requesting information about the batteries.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Responding%20to%20Battery%20Class%20Driver%20Queries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




