---
title: Creating a Framework Device Object
description: Creating a Framework Device Object
ms.assetid: 25023c19-a153-4bd4-9fb6-3a1bf85860aa
keywords: ["PnP WDK KMDF device objects", "Plug and Play WDK KMDF device objects", "power management WDK KMDF device objects", "device objects WDK KMDF", "framework objects WDK KMDF device objects"]
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

[Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md)

[Creating Device Objects in a Filter Driver](creating-device-objects-in-a-filter-driver.md)

[Creating Device Objects in a Bus Driver](creating-device-objects-in-a-bus-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20a%20Framework%20Device%20Object%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




