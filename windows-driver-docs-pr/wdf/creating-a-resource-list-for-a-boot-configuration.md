---
title: Creating a Resource List for a Boot Configuration
description: Creating a Resource List for a Boot Configuration
ms.assetid: 8b78cbac-b547-45a1-a49c-f5543bf5ffed
keywords:
- hardware resources WDK KMDF , boot configuration resource lists
- boot configuration resource lists WDK KMDF
- boot configuration resource lists WDK KMDF , creating
- resource lists WDK KMDF
- resource lists WDK KMDF , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Resource List for a Boot Configuration


After a bus driver enumerates a device, the framework calls the driver's [*EvtDeviceResourcesQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540895) callback function. This callback function receives a handle to a resource-list object, which represents an empty resource list. The driver must then do the following to add information to the list, for each type of hardware resource that the device's boot configuration requires:

1.  Fill in a driver-supplied [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure, which specifies a valid value for a particular resource.

2.  Call [**WdfCmResourceListAppendDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545683) or [**WdfCmResourceListInsertDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545698) to add the contents of the CM\_PARTIAL\_RESOURCE\_DESCRIPTOR structure to the resource list.

After the driver's *EvtDeviceResourcesQuery* callback function returns, the framework passes the resource list to the PnP manager.

Device installers can specify additional resource lists. For more information about additional resource lists, see [Hardware Resources](https://msdn.microsoft.com/library/windows/hardware/ff547012).

 

 





