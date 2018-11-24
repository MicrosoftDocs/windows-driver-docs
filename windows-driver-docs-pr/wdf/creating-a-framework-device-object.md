---
title: Creating a Framework Device Object
description: Creating a Framework Device Object
ms.assetid: 25023c19-a153-4bd4-9fb6-3a1bf85860aa
keywords:
- PnP WDK KMDF , device objects
- Plug and Play WDK KMDF , device objects
- power management WDK KMDF , device objects
- device objects WDK KMDF
- framework objects WDK KMDF , device objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Framework Device Object


Every function driver, filter driver, and bus driver must create a framework device object for each instance of a supported device that is connected to the system.

Creating a framework device object involves three steps:

1.  Obtaining a pointer to a [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure.

    This is an opaque, system-allocated structure, into which the driver stores information about a device.

2.  Initializing the WDFDEVICE\_INIT structure.

    The driver calls a set of framework-supplied functions that add information to the structure.

3.  Calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

    The driver passes the WDFDEVICE\_INIT structure's pointer to the **WdfDeviceCreate** method. The method creates a framework device object and uses information in the WDFDEVICE\_INIT structure to initialize the object.

For more information about creating framework device objects, see the following topics:

-   [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md)

-   [Creating Device Objects in a Filter Driver](creating-device-objects-in-a-filter-driver.md)

-   [Creating Device Objects in a Bus Driver](creating-device-objects-in-a-bus-driver.md)

 

 





