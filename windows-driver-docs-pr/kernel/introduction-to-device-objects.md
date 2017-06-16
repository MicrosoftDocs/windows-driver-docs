---
title: Introduction to Device Objects
author: windows-driver-content
description: Introduction to Device Objects
ms.assetid: 310a2344-f3bc-4a7a-8e1e-63232ecd4cbe
keywords: ["device objects WDK kernel , about device objects", "multiple device objects WDK kernel", "device stacks WDK kernel , about device stacks", "device extensions WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Device Objects


## <a href="" id="ddk-introduction-to-device-objects-kg"></a>


The operating system represents devices by *device objects*. One or more device objects are associated with each device. Device objects serve as the target of all operations on the device.

Kernel-mode drivers must create at least one device object for each device, with the following exceptions:

-   Minidrivers that have an associated class or port driver do not have to create their own device objects. The class or port driver creates the device objects, and dispatches operations to the minidriver.

-   Drivers that are part of device type-specific subsystems, such as NDIS miniport drivers, have their device objects created by the subsystem.

See the documentation for your particular device type to determine if your driver creates its own device objects.

Some device objects do not represent physical devices. A software-only driver, which handles I/O requests but does not pass those requests to hardware, still must create a device object to represent the target of its operations.

For more information about how your driver can create device objects, see [Creating a Device Object](creating-a-device-object.md).

Devices are usually represented by multiple device objects, one for each driver in the driver stack that handles I/O requests for the device. The device objects for a device are organized into a *device stack*. Whenever an operation is performed on a device, the system passes an [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) data structure to the driver for the top device object in the device stack. Each driver either handles the IRP or passes it to the driver that is associated with the next-lower device object in the device stack. For more information about device stacks, see [WDM Device Objects and Device Stacks](wdm-device-objects-and-device-stacks.md). For more information about IRPs, see [Handling IRPs](handling-irps.md).

Device objects are represented by [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structures, which are managed by the object manager. The object manager provides the same capabilities for device objects that it does for other system objects. In particular, a device object can be named, and a named device object can have handles opened on it. For more information about named device objects, see [Named Device Objects](named-device-objects.md).

The system provides dedicated storage for each device object, called the device extension, which the driver can use for device-specific storage. The device extension is created and freed by the system along with the device object. For more information, see [Device Extensions](device-extensions.md).

The following figure illustrates the relationship between device objects and the I/O manager.

![diagram illustrating a device object](images/3devobj.png)

The figure shows the members of the **DEVICE\_OBJECT** structure that are of interest to a driver writer. For more information about these members, see [Creating a Device Object](creating-a-device-object.md), [Initializing a Device Object](initializing-a-device-object.md), and [Properties of Device Objects](properties-of-device-objects.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


