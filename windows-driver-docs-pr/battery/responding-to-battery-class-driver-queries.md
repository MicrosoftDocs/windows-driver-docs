---
title: Responding to Battery Class Driver Queries
description: Responding to Battery Class Driver Queries
ms.assetid: 00b24b37-d312-46ee-8218-2bd7a9453d13
keywords:
- battery miniclass drivers WDK , routines
- routines WDK battery
- battery miniclass drivers WDK , status reporting
- status information WDK battery
- queries WDK battery
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to Battery Class Driver Queries


## <span id="ddk_responding_to_battery_class_driver_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_CLASS_DRIVER_QUERIES_DG"></span>


The miniclass driver must provide the following three [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routines, which report battery status:

[*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275)

[*BatteryMiniQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536273)

[*BatteryMiniQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff536274)

The [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) routine in the class driver calls these miniclass driver routines when it receives IOCTLs requesting information about the batteries.

 

 




