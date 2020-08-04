---
title: WDM Reader Driver
description: WDM Reader Driver
ms.assetid: ead76f5f-1d28-4343-99c0-e7974fa4c3da
keywords:
- vendor-supplied drivers WDK smart card , required routines
- WDM WDK smart card
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Reader Driver

## Required routines

The following routines are required by a WDM reader driver.

### [DriverEntry](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)

Initializes the driver object and the dispatch table.

### [AddDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)

Creates a device object for the smart card reader. In addition, [AddDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) can call any of the following driver library routines:

- [SmartcardInitialize (WDM)](https://docs.microsoft.com/previous-versions/ff548944(v=vs.85)) to complete driver initialization. Calling this routine in [AddDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) is obligatory.
- [SmartcardLogError (WDM)](https://docs.microsoft.com/previous-versions/ff548947(v=vs.85)) to log an error. Drivers must call this routine in [AddDevice](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) if [SmartcardInitialize (WDM)](https://docs.microsoft.com/previous-versions/ff548944(v=vs.85)) fails.
- [SmartcardCreateLink (WDM)](https://docs.microsoft.com/previous-versions/ff548935(v=vs.85)) to create a symbolic link for the reader device in the registry.

### [Unload](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)

Removes the driver from the system.

### [DispatchCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

-and-

### [DispatchClose](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_CREATE](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-create) and [IRP_MJ_CLOSE&lt](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close), respectively. To establish a connection to the reader, the resource manager sends **IRP_MJ_CREATE** to the reader driver. To sever the connection, the resource manager sends **IRP_MJ_CLOSE**.

### [DispatchCleanup](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_CLEANUP](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-cleanup), which the resource manager sends to the reader driver to cancel pending I/O requests.

### [DispatchPnP](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_PNP](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-pnp)

### [DispatchPower](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_POWER](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-power).

### [DispatchDeviceControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

Supports [IRP_MJ_DEVICE_CONTROL](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-device-control) and is the main entry point for smart card requests. Upon receiving IRP_MJ_DEVICE_CONTROL, [DispatchDeviceControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) must immediately call [SmartcardDeviceControl (WDM)](https://docs.microsoft.com/previous-versions/ff548939(v=vs.85)), which is the smart card driver library routine that handles device-control requests. The following code example shows how to call this library routine from a WDM driver:

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
