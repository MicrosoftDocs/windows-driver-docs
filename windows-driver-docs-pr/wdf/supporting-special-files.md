---
title: Supporting Special Files
description: Supporting Special Files
keywords:
- special files WDK KMDF
- paging files WDK KMDF
- dump files WDK KMDF
- hibernation files WDK KMDF
ms.date: 04/20/2017
---

# Supporting Special Files


*Special files* include paging files, dump files, and hibernation files. If the target device for your driver is a storage device that the system might use for these files, the driver must do the following:

-   Call [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) to enable or disable support for each type of special file. (Each driver's support for special files is disabled by default.)

    A bus driver that [enumerates child devices](enumerating-the-devices-on-a-bus.md) should also call [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) for each child device that can support special files.

-   Call [**WdfDeviceAddDependentUsageDeviceObject**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceadddependentusagedeviceobject), if one device is dependent on another device when supporting special files.

-   Optionally provide an [*EvtDeviceUsageNotification*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification) or (starting in KMDF 1.11) [*EvtDeviceUsageNotificationEx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_usage_notification_ex) callback function, so the driver will be notified when a special file is created or removed.

If your driver calls [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) for a device, and if a special file is open on the device, the framework does not allow the PnP manager to remove or stop the device.

After a driver has called [**WdfDeviceAddDependentUsageDeviceObject**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceadddependentusagedeviceobject), it can call [**WdfDeviceRemoveDependentUsageDeviceObject**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceremovedependentusagedeviceobject) to remove a device's dependency on another device.

 

