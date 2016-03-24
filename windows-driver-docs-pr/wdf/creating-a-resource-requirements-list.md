---
title: Creating a Resource Requirements List
description: Creating a Resource Requirements List
ms.assetid: 1254aa21-c64b-4c62-93dc-6758cef382f9
keywords: ["hardware resources WDK KMDF , creating resource requirements lists", "resource requirements lists WDK KMDF", "resource requirements lists WDK KMDF , creating", "resource-requirements-list objects WDK KMDF", "framework resource-requirements-list objects WDK KMDF"]
---

# Creating a Resource Requirements List


When a bus driver detects a child device, the driver is responsible for creating a resource requirements list for the device. Each item in the list is a [logical configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#ddk-logical-configurations-kg) for the device.

After the driver reports the device during bus enumeration, the framework calls the driver's [*EvtDeviceResourceRequirementsQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540894) callback function. This callback function receives a handle to a resource-requirements-list object that represents an empty resource requirements list.

The driver must then do the following to add information to a resource requirements list:

-   Create an empty logical configuration.

    For each logical configuration that the driver will specify, the driver must call [**WdfIoResourceListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548502) to create an empty logical configuration.

-   Add resource descriptors to the logical configuration.

    To add resource descriptors to a logical configuration, the driver must do the following, for each type of hardware resource that the device requires:

    1.  Fill in a driver-allocated [**IO\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff550598) structure, which specifies a range of valid values for a particular resource.
    2.  Call [**WdfIoResourceListAppendDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548498) or [**WdfIoResourceListInsertDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff548513) to add the contents of the IO\_RESOURCE\_DESCRIPTOR structure to a logical configuration.

    If a device uses more than one instance of a resource type, all drivers in the stack that access the resource must be aware of the order in which resources are added. For example, if a device requires two ranges of I/O port addresses, all drivers that access the resource descriptors must be aware of the order in which the two ranges are added to the logical configuration.

-   Add the logical configuration to the resource requirements list.

    To add a logical configuration to the device's resource requirements list, the driver calls [**WdfIoResourceRequirementsListAppendIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548537) or [**WdfIoResourceRequirementsListInsertIoResList**](https://msdn.microsoft.com/library/windows/hardware/ff548560).

    When assigning resources to a device, the PnP manager attempts to match the requirements of the first logical configuration in the list. If the resources required for that configuration are not available, the PnP manager matches the next configuration in the list for which resources are available.

    If your driver supports a non-PnP device, your driver typically must also call [**WdfIoResourceRequirementsListSetSlotNumber**](https://msdn.microsoft.com/library/windows/hardware/ff548579) and [**WdfIoResourceRequirementsListSetInterfaceType**](https://msdn.microsoft.com/library/windows/hardware/ff548577).

After the driver's [*EvtDeviceResourceRequirementsQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540894) callback function returns, the framework passes the resource requirements list to the PnP manager.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20a%20Resource%20Requirements%20List%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




