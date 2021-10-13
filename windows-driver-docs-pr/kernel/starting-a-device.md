---
title: Starting a Device
description: Starting a Device
keywords: ["PnP WDK kernel , starting devices", "Plug and Play WDK kernel , starting devices", "starting PnP devices", "DispatchPnP routine", "IoCompletion routine", "failed starts WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Starting a Device





The PnP manager sends an [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request to drivers either to start a newly enumerated device or to restart an existing device that was stopped for resource rebalancing.

Function and filter drivers must set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, pass the **IRP\_MN\_START\_DEVICE** request down the device stack, and postpone their start operations until all lower drivers have finished with the IRP. The parent bus driver, the bottom driver in the device stack, must be the first driver to perform its start operations on a device before the device is accessed by other drivers.

To ensure proper sequencing of start operations, the PnP manager on Windows 2000 and later versions of Windows postpones exposing device interfaces and blocks create requests for the device until the start IRP succeeds.

If a driver for a device fails the **IRP\_MN\_START\_DEVICE** request, the PnP manager sends an [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request to the device stack (on Windows 2000 and later versions of Windows). In response to this IRP, the drivers for the device undo their start operations (if they succeeded the start IRP), undo their [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) operations, and detach from the device stack. The PnP manager marks such a device "failed start."

This section covers the following topics:

[Starting a Device in a Function Driver](starting-a-device-in-a-function-driver.md)

[Starting a Device in a Filter Driver](starting-a-device-in-a-filter-driver.md)

[Starting a Device in a Bus Driver](starting-a-device-in-a-bus-driver.md)

[Design Guidelines for Starting Devices](design-guidelines-for-starting-devices.md)

 

