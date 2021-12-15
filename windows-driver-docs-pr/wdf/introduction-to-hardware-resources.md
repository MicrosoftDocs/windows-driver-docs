---
title: Introduction to Hardware Resources
description: Introduction to Hardware Resources
keywords:
- boot configurations WDK KMDF
- logical configurations WDK KMDF
- hardware resources WDK KMDF , about hardware resources
ms.date: 04/20/2017
---

# Introduction to Hardware Resources


After a user plugs in a PnP device, the driver that [enumerates the device](enumerating-the-devices-on-a-bus.md) typically creates one or more [logical configurations](../kernel/hardware-resources.md#ddk-logical-configurations-kg), which are combinations of hardware resources that the device can use. These configurations include the following:

-   A *boot configuration* that lists the hardware resources that the device requires when the system starts. (For PnP devices, this information is supplied by the BIOS.)

-   Additional configurations in which the device can operate. The driver groups these additional configurations in a [resource requirements list](../kernel/hardware-resources.md). The PnP manager will eventually select resources from this list to assign to the device.

After the driver creates the logical configurations, it sends them to the framework, and the framework sends them to the PnP manager.

Next, the PnP manager determines which drivers the device requires and loads them if they are not already loaded. The PnP manager sends the device's hardware requirements list to the device's drivers for review. Function and filter drivers can modify this list and send it back to the PnP manager.

The PnP manager examines the modified hardware requirements list and determines which of the specified resources are actually available on the system. If the device requires resources that the PnP manager had previously assigned to another device, the PnP manager might attempt to [redistribute resources](handling-requests-to-stop-a-device.md#redistributing-resources) among the system's devices.

Next, the PnP manager creates a [resource list](../kernel/hardware-resources.md), which is a list of resources that the PnP manager intends to assign to the device. The PnP manager sends this list to the device's drivers for review. At this point, the function and filter drivers can remove resources from the list but they cannot add resources to it.

Finally, the PnP manager assigns resources to the device. The framework passes the resource list to the device's function and filter drivers, and the device's function driver performs any initialization that is necessary so that the device and driver can access the resources.

The following steps describe the process in more detail:

1.  [A user plugs in a device](a-user-plugs-in-a-device.md).

2.  A bus driver detects the device and [enumerates](enumerating-the-devices-on-a-bus.md) it.

3.  The framework calls the bus driver's [*EvtDeviceResourcesQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query) callback function, which [creates a resource list](creating-a-resource-list-for-a-boot-configuration.md) that describes the device's boot configuration.

4.  The framework calls the bus driver's [*EvtDeviceResourceRequirementsQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query) callback function, which [creates a resource requirements list](creating-a-resource-requirements-list.md) for the device.

5.  The PnP manager determines which drivers the device requires and loads them, if they are not already loaded, to create a driver stack for the device.

6.  The PnP manager sends the device's resource requirements list to the driver stack for review. As the list travels down the driver stack, the framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function. As the list travels back up the stack, the framework calls each function and filter driver's [*EvtDeviceFilterAddResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function. Both of these callback functions can [modify the resource requirements list](modifying-a-resource-requirements-list.md).

7.  The PnP manager creates a resource list for the device and sends it to the driver stack for review. The framework calls each function and filter driver's [*EvtDeviceRemoveAddedResources*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources) callback function, which [removes resources](modifying-a-resource-list.md) that the driver's *EvtDeviceFilterAddResourceRequirements* callback function added so the bus driver will not attempt to use them.

8.  The framework receives the final resource list from the PnP manager and stores it.

9.  If a driver calls [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) to create interrupt objects, the framework finds interrupt resources in the resource list and assigns them to the interrupt objects.

10. After the device has entered an uninitialized D0 state, the framework calls each driver's [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function, passing [raw and translated](raw-and-translated-resources.md) versions of the device's resource list as an input argument. The driver can save the resource list, which is valid until the framework calls the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function.

 

