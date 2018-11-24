---
title: DispatchDeviceControl Routine of a Battery Miniclass Driver
description: DispatchDeviceControl Routine of a Battery Miniclass Driver
ms.assetid: 26313dcc-9f37-4c5e-a21e-c4d8a50ff564
keywords:
- battery miniclass drivers WDK , routines
- DispatchDeviceControl routine
- IOCTLs WDK battery
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DispatchDeviceControl Routine of a Battery Miniclass Driver


## <span id="ddk_dispatchdevicecontrol_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DISPATCHDEVICECONTROL_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The power manager sends device control IRPs (IRP\_MJ\_DEVICE\_CONTROL) to the miniclass drivers through the composite battery driver. The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine in the battery miniclass driver handles IRPs that contain battery IOCTLs.

In [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287), the miniclass driver can call the class driver's [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) routine to perform any system-defined device control tasks; **BatteryClassIoctl** handles device control IOCTLs for batteries.

The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine should do the following:

1.  If the miniclass driver defines any private IOCTLs, determine whether the current IOCTL is among them. If so, perform the requested operation, complete the IRP, specifying IO\_NO\_INCREMENT, and go to step 4.

2.  If the IOCTL is not a private IOCTL defined by the miniclass driver, call **BatteryClassIoctl**, passing the IRP and the class handle returned by [**BatteryClassInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff536266). For example:

    ```cpp
    Status = BatteryClassIoctl (NewBattNP->ClassHandle, Irp);
    ```

    The class driver's [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267)routine determines whether the IOCTL is intended for the specified battery. If so, it calls the corresponding [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routine to satisfy the request and then completes the IRP, returning STATUS\_SUCCESS. Otherwise, it returns STATUS\_NOT\_SUPPORTED.

3.  If [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) returns STATUS\_NOT\_SUPPORTED, indicating that this is not a battery IRP, pass the IRP to the next-lower driver.

4.  Pass the returned status as its own function return value.

 

 




