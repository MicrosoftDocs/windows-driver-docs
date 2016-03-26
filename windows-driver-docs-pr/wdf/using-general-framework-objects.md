---
title: Using General Framework Objects
description: Using General Framework Objects
ms.assetid: d3356d3f-8110-44dd-b4a2-36265f5a1714
keywords: ["framework objects WDK KMDF , general", "general framework objects WDK KMDF"]
---

# Using General Framework Objects


The *general framework object* is the framework object from which all other types of framework objects are derived.

Like other framework objects, general objects support a reference count, context space, deletion callback functions, and a parent object, as described in [Introduction to Framework Objects](introduction-to-framework-objects.md).

Drivers can create and use general framework objects. If your driver calls [**WdfObjectCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548730) to create general objects, the driver can:

-   Create one or more context spaces for each general object.

    You can use object context space to store information about system resources that you want to associate with the general object.

    For more information about context space, see [Framework Object Context Space](framework-object-context-space.md).

-   Assign a parent to the general object.

    The general object will be deleted when the parent object is deleted. For example, if your driver specifies a framework device object as the parent object of one of its general objects, the framework will delete the general object when it deletes the device object.

    Drivers specify an object's parent object by setting the **ParentObject** member of the object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

-   Provide deletion callback functions.

    The driver can provide [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) and [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) functions, which can deallocate system resources that the driver allocated when it created the general object. For example, if the driver called [**ExAllocatePool**](https://msdn.microsoft.com/library/windows/hardware/ff544501) when it created a general object, the cleanup or destroy callback function can call [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590).

Using general objects can be a convenient way to manage driver-allocated resources. For example, a higher-level driver might require multiple memory allocations to process a received I/O request, if the driver sends the request to multiple devices or breaks the request into several smaller ones. The driver can create one or more general objects that are children of the received I/O request, and it can store information about the memory allocations in the general objects' context space.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20General%20Framework%20Objects%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




