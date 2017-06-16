---
title: Object-Based
author: windows-driver-content
description: Object-Based
ms.assetid: 53024912-5e6e-4738-81b5-dacc59c22c3f
keywords: ["object-based drivers WDK kernel", "object opacity WDK kernel", "opacity WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Object-Based


## <a href="" id="ddk-object-based-kg"></a>


The Microsoft Windows NT-based operating system is object-based. Various components in the executive define one or more object types. Each component exports kernel-mode support routines that manipulate instances of its object types. No component can directly access another component's objects. To use another component's objects, a component must call the exported support routines.

This design allows the operating system to be both portable and flexible. For example, it is possible for a future release of the operating system to contain a recoded kernel component that defines the same object types, but with entirely different internal structures. If this hypothetical recoded version of the kernel exports a set of support routines that have the same names and parameters as the existing set, the internal changes would have no effect on the portability of any other executive component in the existing system.

Likewise, to remain portable and configurable, drivers must communicate with the operating system and with each other by using only the support routines and other interfaces that are described in the WDK.

Like the operating system, drivers are also object-based. For example:

-   [*File objects*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-file-object) represent a user-mode application's connection to a device.

-   [*Device objects*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-object) represent each driver's logical, virtual, or physical devices.

-   [*Driver objects*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-object) represent each driver's load image.

The I/O manager defines the structure and interfaces for file objects, device objects, and driver objects.

Like any other executive component, drivers use objects by calling kernel-mode support routines that the I/O manager and other system components export. Kernel-mode support routines generally have names that identify the specific object that each routine manipulates and the operation that each routine performs on that object. These support routine names have the following form:

*PrefixOperationObject*

where

*Prefix*
Identifies the kernel-mode component that exports the support routine and, usually, the component that defined the object type. Most prefixes have two letters.

*Operation*
Describes what is done to the object.

*Object*
Identifies the type of object.

For example, the I/O manager's [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) routine creates a device object to represent a physical, logical, or virtual device as the target of I/O requests.

One system component can export routines that call another component's support routines. This can reduce the number of calls that a driver must make. The I/O manager, in particular, exports certain routines that make it easier to develop drivers. For example, [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378), which lowest-level drivers call to register their [*ISRs*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-interrupt-service-routine--isr-), calls the kernel support routines for [*interrupt objects*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-interrupt-object).

### <a href="" id="ddk-object-opacity-kg"></a>Object Opacity

Some system-defined objects are *opaque*: only the defining system component is aware of such an object's internal structure and can directly access all of the data that an object contains. The system component that defines an opaque object exports support routines that drivers and other kernel-mode components can call to manipulate that object. Drivers never access opaque object structures directly.

**Note**   To maintain driver portability, drivers must use the system-supplied support routines to manipulate system-defined objects. The defining system component can change the internal structure of its object types at any time.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Object-Based%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


