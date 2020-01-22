---
title: Modifying a Resource List
description: Modifying a Resource List
ms.assetid: 571b2990-5627-434e-b8fc-d2564188f544
keywords:
- boot configuration resource lists WDK KMDF , modifying
- hardware resources WDK KMDF , resource lists
- resource lists WDK KMDF , modifying
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying a Resource List


If a driver provides an [*EvtDeviceFilterAddResourceRequirements*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function, it must also provide an [*EvtDeviceRemoveAddedResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources) callback function. The *EvtDeviceRemoveAddedResources* callback function removes resources that the *EvtDeviceFilterAddResourceRequirements* callback function added so that the bus driver will not attempt to use them.

To modify the resource descriptors in a device's resource list, a driver should call the following methods:

-   [**WdfCmResourceListGetCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistgetcount), to obtain the number of resource descriptors.

-   [**WdfCmResourceListGetDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistgetdescriptor), to obtain access to a resource descriptor.

-   [**WdfCmResourceListRemove**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistremove) and [**WdfCmResourceListRemoveByDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistremovebydescriptor), to remove a resource descriptor.

If the driver removes a resource, it must remove it from both the [raw and translated resource lists](raw-and-translated-resources.md).

 

 





