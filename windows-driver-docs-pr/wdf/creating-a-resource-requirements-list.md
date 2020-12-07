---
title: Creating a Resource Requirements List
description: Creating a Resource Requirements List
keywords:
- hardware resources WDK KMDF , creating resource requirements lists
- resource requirements lists WDK KMDF
- resource requirements lists WDK KMDF , creating
- resource-requirements-list objects WDK KMDF
- framework resource-requirements-list objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Resource Requirements List


When a bus driver detects a child device, the driver is responsible for creating a resource requirements list for the device. Each item in the list is a [logical configuration](../kernel/hardware-resources.md#ddk-logical-configurations-kg) for the device.

After the driver reports the device during bus enumeration, the framework calls the driver's [*EvtDeviceResourceRequirementsQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query) callback function. This callback function receives a handle to a resource-requirements-list object that represents an empty resource requirements list.

The driver must then do the following to add information to a resource requirements list:

-   Create an empty logical configuration.

    For each logical configuration that the driver will specify, the driver must call [**WdfIoResourceListCreate**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistcreate) to create an empty logical configuration.

-   Add resource descriptors to the logical configuration.

    To add resource descriptors to a logical configuration, the driver must do the following, for each type of hardware resource that the device requires:

    1.  Fill in a driver-allocated [**IO\_RESOURCE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_resource_descriptor) structure, which specifies a range of valid values for a particular resource.
    2.  Call [**WdfIoResourceListAppendDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistappenddescriptor) or [**WdfIoResourceListInsertDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistinsertdescriptor) to add the contents of the IO\_RESOURCE\_DESCRIPTOR structure to a logical configuration.

    If a device uses more than one instance of a resource type, all drivers in the stack that access the resource must be aware of the order in which resources are added. For example, if a device requires two ranges of I/O port addresses, all drivers that access the resource descriptors must be aware of the order in which the two ranges are added to the logical configuration.

-   Add the logical configuration to the resource requirements list.

    To add a logical configuration to the device's resource requirements list, the driver calls [**WdfIoResourceRequirementsListAppendIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistappendioreslist) or [**WdfIoResourceRequirementsListInsertIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistinsertioreslist).

    When assigning resources to a device, the PnP manager attempts to match the requirements of the first logical configuration in the list. If the resources required for that configuration are not available, the PnP manager matches the next configuration in the list for which resources are available.

    If your driver supports a non-PnP device, your driver typically must also call [**WdfIoResourceRequirementsListSetSlotNumber**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistsetslotnumber) and [**WdfIoResourceRequirementsListSetInterfaceType**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistsetinterfacetype).

After the driver's [*EvtDeviceResourceRequirementsQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query) callback function returns, the framework passes the resource requirements list to the PnP manager.

 

