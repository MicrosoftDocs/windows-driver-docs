---
title: DispatchDeviceControl Routine of a Battery Miniclass Driver
description: DispatchDeviceControl Routine of a Battery Miniclass Driver
ms.assetid: 26313dcc-9f37-4c5e-a21e-c4d8a50ff564
keywords: ["battery miniclass drivers WDK , routines", "DispatchDeviceControl routine", "IOCTLs WDK battery"]
---

# DispatchDeviceControl Routine of a Battery Miniclass Driver


## <span id="ddk_dispatchdevicecontrol_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DISPATCHDEVICECONTROL_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The power manager sends device control IRPs (IRP\_MJ\_DEVICE\_CONTROL) to the miniclass drivers through the composite battery driver. The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine in the battery miniclass driver handles IRPs that contain battery IOCTLs.

In [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287), the miniclass driver can call the class driver's [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) routine to perform any system-defined device control tasks; **BatteryClassIoctl** handles device control IOCTLs for batteries.

The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine should do the following:

1.  If the miniclass driver defines any private IOCTLs, determine whether the current IOCTL is among them. If so, perform the requested operation, complete the IRP, specifying IO\_NO\_INCREMENT, and go to step 4.

2.  If the IOCTL is not a private IOCTL defined by the miniclass driver, call **BatteryClassIoctl**, passing the IRP and the class handle returned by [**BatteryClassInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff536266). For example:

    ```
    Status = BatteryClassIoctl (NewBattNP->ClassHandle, Irp);
    ```

    The class driver's [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267)routine determines whether the IOCTL is intended for the specified battery. If so, it calls the corresponding [BatteryMini*Xxx*](https://msdn.microsoft.com/library/windows/hardware/ff536286) routine to satisfy the request and then completes the IRP, returning STATUS\_SUCCESS. Otherwise, it returns STATUS\_NOT\_SUPPORTED.

3.  If [**BatteryClassIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff536267) returns STATUS\_NOT\_SUPPORTED, indicating that this is not a battery IRP, pass the IRP to the next-lower driver.

4.  Pass the returned status as its own function return value.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20DispatchDeviceControl%20Routine%20of%20a%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




