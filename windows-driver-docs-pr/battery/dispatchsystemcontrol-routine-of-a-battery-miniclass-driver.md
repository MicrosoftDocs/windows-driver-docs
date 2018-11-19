---
title: DispatchSystemControl Routine of a Battery Miniclass Driver
description: DispatchSystemControl Routine of a Battery Miniclass Driver
ms.assetid: bb9bb04e-4284-4e9c-85ea-60f99a01d7d9
keywords:
- battery miniclass drivers WDK , routines
- DispatchSystemControl routine
- WMI WDK battery
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DispatchSystemControl Routine of a Battery Miniclass Driver


## <span id="ddk_dispatchsystemcontrol_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DISPATCHSYSTEMCONTROL_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


Battery miniclass drivers must support [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) by supplying a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine to handle the [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) IRP. WMI provides a uniform way for drivers to expose measurement and instrumentation data.

Battery miniclass drivers use the [**BatteryClassSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff536270) routine to do initial processing. **BatteryClassSystemControl** takes a *WmiLibContext* parameter, which specifies a dispatch table of functions. The routine uses the **MinorFunction** member of IRP\_MJ\_SYSTEM\_CONTROL to determine which dispatch function it calls.

There are certain WMI queries that all drivers for battery devices must handle. Battery miniclass drivers do not need to support these WMI queries directly, but instead forward them to the battery class driver to handle. To handle WMI queries, the miniclass driver provides a pointer to a [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine in the **QueryWmiDataBlock** member of [**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813). The miniclass driver is not required to handle any other type of WMI request. If it does not, the driver sets the other members of WMILIB\_CONTEXT to zero.

Inside its [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine, the miniclass driver calls the [**BatteryClassQueryWmiDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff536268) routine to allow the battery class driver to handle the WMI query request if it can. If the battery class driver handles that WMI class GUID, it completes the IRP. Otherwise, **BatteryClassQueryWmiDataBlock** returns a value of STATUS\_WMI\_GUID\_NOT\_FOUND. Then, the miniclass driver can do its driver-specific processing, and use [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) to complete the request.

Battery miniclass drivers are not required to do any WMI IRP processing beyond calling **BatteryClassQueryWmiDataBlock**. In a minimal implementation of WMI handling for a battery miniclass driver, if **BatteryClassQueryWmiDataBlock** returns STATUS\_WMI\_GUID\_NOT\_FOUND, the miniclass driver simply calls [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) with a status value of STATUS\_WMI\_GUID\_NOT\_FOUND.

 

 




