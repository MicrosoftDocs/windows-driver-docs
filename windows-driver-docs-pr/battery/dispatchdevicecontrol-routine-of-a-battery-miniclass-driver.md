---
title: Battery miniclass driver's DispatchDeviceControl routine
description: Discover the DispatchDeviceControl routine in a battery miniclass driver and how it manages IRPs containing battery IOCTLs.
keywords:
- battery miniclass drivers WDK, routines
- DispatchDeviceControl routine
- IOCTLs WDK battery
ms.date: 04/20/2017
---

# Battery miniclass driver's DispatchDeviceControl routine

The power manager sends device control IRPs (IRP_MJ_DEVICE_CONTROL) to miniclass drivers through the composite battery driver. The battery miniclass driver's [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs containing battery IOCTLs.

In the [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine, the miniclass driver can call the class driver's [**BatteryClassIoctl**](/windows/win32/api/batclass/nf-batclass-batteryclassioctl) routine to perform system-defined device control tasks. **BatteryClassIoctl** handles device control IOCTLs for batteries.

The [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine should:

1. Determine if the current IOCTL is a private IOCTL defined by the miniclass driver. If so, perform the requested operation, complete the IRP with IO_NO_INCREMENT, and proceed to step 4.

1. If the IOCTL isn't a private IOCTL, call **BatteryClassIoctl** with the IRP and the class handle returned by [**BatteryClassInitializeDevice**](/windows/win32/api/batclass/nf-batclass-batteryclassinitializedevice). For example:

   ```cpp
   Status = BatteryClassIoctl (NewBattNP->ClassHandle, Irp);
   ```

   The class driver's [**BatteryClassIoctl**](/windows/win32/api/batclass/nf-batclass-batteryclassioctl) routine checks if the IOCTL is intended for the specified battery. If so, it calls the corresponding [BatteryMini*Xxx*](/windows-hardware/drivers/ddi/_battery/) routine to satisfy the request and completes the IRP with STATUS_SUCCESS. Otherwise, it returns STATUS_NOT_SUPPORTED.

1. If [**BatteryClassIoctl**](/windows/win32/api/batclass/nf-batclass-batteryclassioctl) returns STATUS_NOT_SUPPORTED, indicating that this isn't a battery IRP, pass the IRP to the next-lower driver.

1. Return the status as the function's return value.
