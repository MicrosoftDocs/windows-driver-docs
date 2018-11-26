---
title: Using General Framework Objects
description: Using General Framework Objects
ms.assetid: d3356d3f-8110-44dd-b4a2-36265f5a1714
keywords:
- framework objects WDK KMDF , general
- general framework objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





