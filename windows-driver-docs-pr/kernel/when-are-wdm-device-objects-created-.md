---
title: When Are WDM Device Objects Created
description: When Are WDM Device Objects Created
ms.assetid: aeb8039d-2e5d-4700-a9e5-e5ee97c6b0b1
keywords: ["device objects WDK kernel , when created", "layered device objects WDK kernel", "functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "filter DOs WDK kernel", "device stacks WDK kernel , device object layers possible", "attaching device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When Are WDM Device Objects Created?





This section describes each kind of device object and mentions when each is created.

The following figure shows the possible kinds of device objects that can be attached in a device stack, representing the drivers handling I/O requests for a device.

![diagram illustrating possible device object layers for a device](images/objlyr.png)

Starting at the bottom of this figure:

-   A bus driver creates a PDO for each device that it enumerates on its bus.

    A bus driver creates a PDO for a child device when it enumerates the device. A bus driver enumerates a device in response to an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request for **BusRelations** from the PnP manager. The bus driver creates a PDO for a child device if the device has been added to the bus since the last time the bus driver responded to a query-relations request for **BusRelations** (or if this is the first query-relations request since the machine was booted).

    A PDO represents the device to the bus driver, as well as to other kernel-mode system components such as the power manager, the PnP manager, and the I/O manager.

    Other drivers for a device attach device objects on top of the PDO, but the PDO is always at the bottom of the device stack.

-   Optional bus filter drivers create filter DOs for each device they filter.

    When the PnP manager detects a new device in a **BusRelations** list, it determines whether there are any bus filter drivers for the device. If so, for each such driver the PnP manager ensures it is loaded (calls [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) if necessary) and calls the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. If the bus filter driver filters operations for this device, the filter driver creates a device object and attaches it to the device stack in its *AddDevice* routine. If more than one bus filter driver exists and is relevant to this device, each such filter driver creates and attaches its own device object.

-   Optional, lower-level filter drivers create filter DOs for each device they filter.

    If an optional, lower-level filter driver exists for this device, the PnP manager ensures that such a driver is loaded after the bus driver and any bus filter drivers. The PnP manager calls the filter driver's *AddDevice* routine. In its *AddDevice* routine, the lower-level filter driver creates a filter DO for the device and attaches it to the device stack. If more than one lower-level filter driver exists, each such driver would create and attach its own filter DO.

-   The function driver creates an FDO for the device.

    The PnP manager ensures that the function driver for the device is loaded and calls the function driver's *AddDevice* routine. The function driver creates an FDO and attaches it to the device stack.

-   Optional, upper-level filter drivers create a filter DO for each device they filter.

    If any optional, upper-level filter drivers exist for the device, the PnP manager ensures they are loaded after the function driver and calls their *AddDevice* routines. Each such filter driver attaches its device object to the device stack.

In summary, the device stack contains a device object for each driver that is involved in handling I/O to a particular device. The parent bus driver has a PDO, the function driver has an FDO, and each optional filter driver has a filter DO.

Note that all devices, bus adapter/controller devices and nonbus devices, have a PDO and an FDO in their device stack. The PDO for a bus adapter/controller is created by the bus driver for the parent bus. For example, if a SCSI adapter plugs into a PCI bus, the PCI bus driver creates a PDO for the SCSI adapter.

If a device is being used in raw mode, there are no function or filter drivers (no FDO or filter DOs). There is just a PDO for the parent bus driver and zero or more bus filter DOs.

See [Creating a Device Object](creating-a-device-object.md) for information about which driver routines are responsible for creating and attaching device objects.

The device stack plus some additional information constitutes the *devnode* for a device. The PnP manager maintains information in a device's devnode such as whether the device has been started and which drivers, if any, have registered for notification of changes on the device. The kernel debugger command **!devnode** displays information about a devnode.

 

 




