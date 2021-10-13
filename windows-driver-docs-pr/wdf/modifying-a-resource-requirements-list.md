---
title: Modifying a Resource Requirements List
description: Modifying a Resource Requirements List
keywords:
- hardware resources WDK KMDF , modifying resource requirements lists
- resource requirements lists WDK KMDF , modifying
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying a Resource Requirements List


After the PnP manager has ensured that all of a newly connected device's drivers have been loaded, it sends the device's hardware requirements list to the device's driver stack.

As the list travels down the stack, the framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function, passing the hardware requirements list as an input argument. This callback function can remove hardware resources from the hardware requirements list that the bus driver has specified but that the function driver determines are not necessary for the device to operate.

For example, a PCI bus driver might, in accordance with the PCI specification, replicate an I/O space resource in memory space. If your device can operate without using the I/O space resource, the device's function driver can remove the I/O space resource from the hardware requirements list.

To remove items from the requirements list, a driver can do the following:

-   Call the following methods to modify the logical configurations in the resource requirements list:
    -   [**WdfIoResourceRequirementsListGetCount**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistgetcount), to obtain the number of logical configurations.
    -   [**WdfIoResourceRequirementsListGetIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistgetioreslist), to obtain access to a logical configuration.
    -   [**WdfIoResourceRequirementsListRemove**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistremove) and [**WdfIoResourceRequirementsListRemoveByIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistremovebyioreslist), to remove a logical configuration.
-   Call the following methods to modify the resource descriptors within a logical configuration:
    -   [**WdfIoResourceListGetCount**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistgetcount), to obtain the number of resource descriptors.
    -   [**WdfIoResourceListGetDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistgetdescriptor), to obtain access to a resource descriptor.
    -   [**WdfIoResourceListRemove**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistremove) and [**WdfIoResourceListRemoveByDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistremovebydescriptor), to remove a resource descriptor.

As the list travels back up the driver stack, the framework calls each function and filter driver's [*EvtDeviceFilterAddResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function, passing the hardware requirements list as an input argument. This callback function can add additional hardware resources that the function driver requires to make the device operational.

To add items to the hardware requirements list, a driver can do the following:

-   Call the following methods to modify the logical configurations in the resource requirements list:
    -   [**WdfIoResourceRequirementsListGetCount**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistgetcount), to obtain the number of logical configurations.
    -   [**WdfIoResourceRequirementsListGetIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistgetioreslist), to obtain access to a logical configuration.
    -   [**WdfIoResourceListCreate**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistcreate), to create a new logical configuration.
    -   [**WdfIoResourceRequirementsListAppendIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistappendioreslist) or [**WdfIoResourceRequirementsListInsertIoResList**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcerequirementslistinsertioreslist), to add a new logical configuration.
-   Call the following methods to modify the resource descriptors within a logical configuration:
    -   [**WdfIoResourceListGetCount**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistgetcount), to obtain the number of resource descriptors.
    -   [**WdfIoResourceListGetDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistgetdescriptor), to obtain access to a resource descriptor.
    -   [**WdfIoResourceListAppendDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistappenddescriptor) or [**WdfIoResourceListInsertDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfioresourcelistinsertdescriptor), to add a resource descriptor.

 

