---
title: WDM Reader Driver
description: WDM Reader Driver
keywords:
- vendor-supplied drivers WDK smart card , required routines
- WDM WDK smart card
ms.date: 04/20/2017
---

# WDM Reader Driver

## Required routines

The following routines are required by a WDM reader driver.

### [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)

Initializes the driver object and the dispatch table.

### [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)

Creates a device object for the smart card reader. In addition, [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) can call any of the following driver library routines:

- [SmartcardInitialize (WDM)](/previous-versions/ff548944(v=vs.85)) to complete driver initialization. Calling this routine in [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) is obligatory.
- [SmartcardLogError (WDM)](/previous-versions/ff548947(v=vs.85)) to log an error. Drivers must call this routine in [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) if [SmartcardInitialize (WDM)](/previous-versions/ff548944(v=vs.85)) fails.
- [SmartcardCreateLink (WDM)](/previous-versions/ff548935(v=vs.85)) to create a symbolic link for the reader device in the registry.

### [Unload](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)

Removes the driver from the system.

### [DispatchCreate](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

-and-

### [DispatchClose](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_CREATE](../kernel/irp-mj-create.md) and [IRP_MJ_CLOSE&lt](../kernel/irp-mj-close.md), respectively. To establish a connection to the reader, the resource manager sends **IRP_MJ_CREATE** to the reader driver. To sever the connection, the resource manager sends **IRP_MJ_CLOSE**.

### [DispatchCleanup](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_CLEANUP](../kernel/irp-mj-cleanup.md), which the resource manager sends to the reader driver to cancel pending I/O requests.

### [DispatchPnP](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_PNP](../kernel/irp-mj-pnp.md)

### [DispatchPower](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_POWER](../kernel/irp-mj-power.md).

### [DispatchDeviceControl](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_DEVICE_CONTROL](../kernel/irp-mj-device-control.md) and is the main entry point for smart card requests. Upon receiving IRP_MJ_DEVICE_CONTROL, [DispatchDeviceControl](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) must immediately call [SmartcardDeviceControl (WDM)](/previous-versions/ff548939(v=vs.85)), which is the smart card driver library routine that handles device-control requests. The following code example shows how to call this library routine from a WDM driver:

```cpp
NTSTATUS
DriverDeviceControl(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp
    )
{
    PDEVICE_EXTENSION deviceExtension = DeviceObject -&gt; DeviceExtension;

    return SmartcardDeviceControl(
        &(deviceExtension-&gt;SmartcardExtension),
        Irp
        );
```

If it is unable to handle the particular IOCTL that is indicated in the call, **SmartcardDeviceControl** will call the driver's callback for unknown IOCTL requests.
