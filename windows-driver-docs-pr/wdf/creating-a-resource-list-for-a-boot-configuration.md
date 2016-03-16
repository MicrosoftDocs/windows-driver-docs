---
title: Creating a Resource List for a Boot Configuration
description: Creating a Resource List for a Boot Configuration
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 8b78cbac-b547-45a1-a49c-f5543bf5ffed
keywords: ["hardware resources WDK KMDF boot configuration resource lists", "boot configuration resource lists WDK KMDF", "boot configuration resource lists WDK KMDF creating", "resource lists WDK KMDF", "resource lists WDK KMDF creating"]
---

# Creating a Resource List for a Boot Configuration


After a bus driver enumerates a device, the framework calls the driver's [*EvtDeviceResourcesQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540895) callback function. This callback function receives a handle to a resource-list object, which represents an empty resource list. The driver must then do the following to add information to the list, for each type of hardware resource that the device's boot configuration requires:

1.  Fill in a driver-supplied [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure, which specifies a valid value for a particular resource.

2.  Call [**WdfCmResourceListAppendDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545683) or [**WdfCmResourceListInsertDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545698) to add the contents of the CM\_PARTIAL\_RESOURCE\_DESCRIPTOR structure to the resource list.

After the driver's *EvtDeviceResourcesQuery* callback function returns, the framework passes the resource list to the PnP manager.

Device installers can specify additional resource lists. For more information about additional resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20a%20Resource%20List%20for%20a%20Boot%20Configuration%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




