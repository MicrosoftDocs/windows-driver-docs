---
title: Modifying a Resource Requirements List
description: Modifying a Resource Requirements List
ms.assetid: 75391dd2-5ae1-4562-97a0-4de21a08b61c
keywords: ["hardware resources WDK KMDF , modifying resource requirements lists", "resource requirements lists WDK KMDF , modifying"]
---

# Modifying a Resource Requirements List


After the PnP manager has ensured that all of a newly connected device's drivers have been loaded, it sends the device's hardware requirements list to the device's driver stack.

As the list travels down the stack, the framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540872) callback function, passing the hardware requirements list as an input argument. This callback function can remove hardware resources from the hardware requirements list that the bus driver has specified but that the function driver determines are not necessary for the device to operate.

For example, a PCI bus driver might, in accordance with the PCI specification, replicate an I/O space resource in memory space. If your device can operate without using the I/O space resource, the device's function driver can remove the I/O space resource from the hardware requirements list.

To remove items from the requirements list, a driver can do the following:

-   Call the following methods to modify the logical configurations in the resource requirements list:
    -   [**WdfIoResourceRequirementsListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff548545), to obtain the number of logical configurations.
    -   [**WdfIoResourceRequirementsListGetIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548553), to obtain access to a logical configuration.
    -   [**WdfIoResourceRequirementsListRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548570) and [**WdfIoResourceRequirementsListRemoveByIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548575), to remove a logical configuration.
-   Call the following methods to modify the resource descriptors within a logical configuration:
    -   [**WdfIoResourceListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff548506), to obtain the number of resource descriptors.
    -   [**WdfIoResourceListGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548510), to obtain access to a resource descriptor.
    -   [**WdfIoResourceListRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548523) and [**WdfIoResourceListRemoveByDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548528), to remove a resource descriptor.

As the list travels back up the driver stack, the framework calls each function and filter driver's [*EvtDeviceFilterAddResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540870) callback function, passing the hardware requirements list as an input argument. This callback function can add additional hardware resources that the function driver requires to make the device operational.

To add items to the hardware requirements list, a driver can do the following:

-   Call the following methods to modify the logical configurations in the resource requirements list:
    -   [**WdfIoResourceRequirementsListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff548545), to obtain the number of logical configurations.
    -   [**WdfIoResourceRequirementsListGetIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548553), to obtain access to a logical configuration.
    -   [**WdfIoResourceListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548502), to create a new logical configuration.
    -   [**WdfIoResourceRequirementsListAppendIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548537) or [**WdfIoResourceRequirementsListInsertIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548560), to add a new logical configuration.
-   Call the following methods to modify the resource descriptors within a logical configuration:
    -   [**WdfIoResourceListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff548506), to obtain the number of resource descriptors.
    -   [**WdfIoResourceListGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548510), to obtain access to a resource descriptor.
    -   [**WdfIoResourceListAppendDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548498) or [**WdfIoResourceListInsertDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548513), to add a resource descriptor.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Modifying%20a%20Resource%20Requirements%20List%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




