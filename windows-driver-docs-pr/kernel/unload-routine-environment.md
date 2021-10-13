---
title: Unload Routine Environment
description: Unload Routine Environment
keywords: ["Unload routines WDK kernel , environment"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Unload Routine Environment





The operating system unloads a driver when the driver is being replaced or when all of the devices that the driver services have been removed. The PnP manager calls a PnP driver's [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine if the driver has no more device objects after it handles an [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request.

At the start of the unloading sequence, the I/O manager or PnP manager marks the driver object and its device objects as "Unload Pending". After a driver has been marked as "Unload Pending", no additional drivers can attach to that driver, nor can any additional references be made to the driver's device objects. The driver can complete outstanding IRPs, but the system will not send any new IRPs to the driver.

The I/O manager calls a driver's *Unload* routine when all of the following are true:

-   No references remain to any of the device objects the driver has created. In other words, no files associated with the underlying device can be open, nor can any IRPs be outstanding for any of the driver's device objects.

-   No other drivers remain attached to this driver.

-   The driver has called [**IoUnregisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregisterplugplaynotification) to unregister all PnP notifications for which it previously registered.

Note that the *Unload* routine is not called if a driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine returns a failure status. In this case, the I/O manager simply frees the memory space taken up by the driver.

Neither the PnP manager nor the I/O manager calls *Unload* routines at system shutdown time. A driver that must perform shutdown processing should register a [*DispatchShutdown*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

 

