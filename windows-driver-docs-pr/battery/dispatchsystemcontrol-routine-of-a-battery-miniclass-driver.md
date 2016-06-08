---
title: DispatchSystemControl Routine of a Battery Miniclass Driver
description: DispatchSystemControl Routine of a Battery Miniclass Driver
ms.assetid: bb9bb04e-4284-4e9c-85ea-60f99a01d7d9
keywords: ["battery miniclass drivers WDK , routines", "DispatchSystemControl routine", "WMI WDK battery"]
---

# DispatchSystemControl Routine of a Battery Miniclass Driver


## <span id="ddk_dispatchsystemcontrol_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DISPATCHSYSTEMCONTROL_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


Battery miniclass drivers must support [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) by supplying a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine to handle the [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) IRP. WMI provides a uniform way for drivers to expose measurement and instrumentation data.

Battery miniclass drivers use the [**BatteryClassSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff536270) routine to do initial processing. **BatteryClassSystemControl** takes a *WmiLibContext* parameter, which specifies a dispatch table of functions. The routine uses the **MinorFunction** member of IRP\_MJ\_SYSTEM\_CONTROL to determine which dispatch function it calls.

There are certain WMI queries that all drivers for battery devices must handle. Battery miniclass drivers do not need to support these WMI queries directly, but instead forward them to the battery class driver to handle. To handle WMI queries, the miniclass driver provides a pointer to a [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine in the **QueryWmiDataBlock** member of [**WMILIB\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff565813). The miniclass driver is not required to handle any other type of WMI request. If it does not, the driver sets the other members of WMILIB\_CONTEXT to zero.

Inside its [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine, the miniclass driver calls the [**BatteryClassQueryWmiDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff536268) routine to allow the battery class driver to handle the WMI query request if it can. If the battery class driver handles that WMI class GUID, it completes the IRP. Otherwise, **BatteryClassQueryWmiDataBlock** returns a value of STATUS\_WMI\_GUID\_NOT\_FOUND. Then, the miniclass driver can do its driver-specific processing, and use [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) to complete the request.

Battery miniclass drivers are not required to do any WMI IRP processing beyond calling **BatteryClassQueryWmiDataBlock**. In a minimal implementation of WMI handling for a battery miniclass driver, if **BatteryClassQueryWmiDataBlock** returns STATUS\_WMI\_GUID\_NOT\_FOUND, the miniclass driver simply calls [**WmiCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff565798) with a status value of STATUS\_WMI\_GUID\_NOT\_FOUND.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20DispatchSystemControl%20Routine%20of%20a%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




