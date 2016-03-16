---
title: Modifying a Resource List
description: Modifying a Resource List
ms.assetid: 571b2990-5627-434e-b8fc-d2564188f544
keywords: ["boot configuration resource lists WDK KMDF modifying", "hardware resources WDK KMDF resource lists", "resource lists WDK KMDF modifying"]
---

# Modifying a Resource List


If a driver provides an [*EvtDeviceFilterAddResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540870) callback function, it must also provide an [*EvtDeviceRemoveAddedResources*](https://msdn.microsoft.com/library/windows/hardware/ff540892) callback function. The *EvtDeviceRemoveAddedResources* callback function removes resources that the *EvtDeviceFilterAddResourceRequirements* callback function added so that the bus driver will not attempt to use them.

To modify the resource descriptors in a device's resource list, a driver should call the following methods:

-   [**WdfCmResourceListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff545687), to obtain the number of resource descriptors.

-   [**WdfCmResourceListGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545688), to obtain access to a resource descriptor.

-   [**WdfCmResourceListRemove**](https://msdn.microsoft.com/library/windows/hardware/ff545704) and [**WdfCmResourceListRemoveByDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545717), to remove a resource descriptor.

If the driver removes a resource, it must remove it from both the [raw and translated resource lists](raw-and-translated-resources.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Modifying%20a%20Resource%20List%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




