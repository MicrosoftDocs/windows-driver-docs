---
title: Responding to Battery Class Driver Queries
description: Responding to Battery Class Driver Queries
keywords:
- battery miniclass drivers WDK , routines
- routines WDK battery
- battery miniclass drivers WDK , status reporting
- status information WDK battery
- queries WDK battery
ms.date: 04/20/2017
---

# Responding to Battery Class Driver Queries


## <span id="ddk_responding_to_battery_class_driver_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_CLASS_DRIVER_QUERIES_DG"></span>


The miniclass driver must provide the following three [BatteryMini*Xxx*](/windows-hardware/drivers/ddi/_battery/) routines, which report battery status:

[*BatteryMiniQueryTag*](/windows/win32/api/batclass/nc-batclass-bclass_query_tag_callback)

[*BatteryMiniQueryInformation*](/windows/win32/api/batclass/nc-batclass-bclass_query_information_callback)

[*BatteryMiniQueryStatus*](/windows/win32/api/batclass/nc-batclass-bclass_query_status_callback)

The [**BatteryClassIoctl**](/windows/win32/api/batclass/nf-batclass-batteryclassioctl) routine in the class driver calls these miniclass driver routines when it receives IOCTLs requesting information about the batteries.

 

