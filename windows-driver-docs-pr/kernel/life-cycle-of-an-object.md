---
title: Life Cycle of an Object
description: Life Cycle of an Object
ms.assetid: e81bfce6-27c4-4916-adc8-9c014d02bee7
keywords: ["object life cycles WDK kernel", "life cycles WDK objects", "referencing objects", "object reference counts WDK kernel", "temporary objects WDK kernel", "permanent objects WDK kernel", "reference counts WDK objects", "freed objects WDK kernel", "object temporary status WDK kernel", "object permanent status WDK kernel", "automatic object deletions WDK kernel", "object tracking WDK kernel", "open object handles WDK kernel", "counting references WDK objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Life Cycle of an Object





This topic describes the "life cycle" of an object, that is, how objects are referenced and tracked by the object manager. This topic also describes how to make objects temporary or permanent.

### Object Reference Count

The object manager maintains a count of the number of references to an object. When an object is created, the object manager sets the object's reference count to one. Once that counter falls to zero, the object is freed.

Drivers must ensure that the object manager has an accurate reference count for any objects they manipulate. An object that is released prematurely can cause the system to crash. An object whose reference count is mistakenly high will never be freed.

Objects can be referenced either by handle, or by pointer. In addition to the reference count, the object manager maintains a count of the number of open handles to an object. Each routine that opens a handle increases both the object reference count and the object handle count by one. Each call to such a routine must be matched with a corresponding call to [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). For more information, see [Object Handles](object-handles.md).

Within kernel mode, objects can be referenced by a pointer to the object. Routines that return pointers to objects, such as [**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145), increase the reference count by one. Once the driver is done using the pointer, it must call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) to decrease the reference count by one.

The following routines all increase the reference count of an object by one:

[**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560)

[**IoGetAttachedDeviceReference**](https://msdn.microsoft.com/library/windows/hardware/ff549145)

[**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198)

[**IoWMIOpenBlock**](https://msdn.microsoft.com/library/windows/hardware/ff550453)

[**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678)

[**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679)

[**ObReferenceObjectByPointer**](https://msdn.microsoft.com/library/windows/hardware/ff558686)

Each call that is made to any of the preceding routines must be matched with a corresponding call to **ObDereferenceObject**.

The **ObReferenceObject** and **ObReferenceObjectByPointer** routines are provided so that drivers can increase the reference count of a known object pointer by one. **ObReferenceObject** simply increases the reference count. **ObReferenceObjectByPointer** does an access check before increasing the reference count.

The **ObReferenceObjectByHandle** routine receives an object handle and supplies a pointer to the underlying object. It too increases the reference count by one.

### Temporary and Permanent Objects

Most objects are *temporary*; they exist as long as they are in use, and then they are freed by the object manager. Objects can be created that are *permanent*. If an object is permanent, the object manager itself holds a reference to the object. Thus, its reference count remains greater than zero, and the object is not freed when it is no longer in use.

A temporary object can be accessed by name only as long as its handle count is nonzero. Once the handle count decrements to zero, the object's name is removed from the object manager's namespace. Such objects can still be accessed by pointer as long as their reference count remains greater than zero. Permanent objects can be accessed by name as long as they exist.

An object can be made permanent at the time of its creation by specifying the OBJ\_PERMANENT attribute in the [**OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff557749) structure for the object. For more information, see [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804).

To make a permanent object temporary, use the [**ZwMakeTemporaryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566477) routine. This routine causes an object to be automatically deleted once it is no longer in use. (If the object has no open handles, the object's name is immediately removed from the object manager's namespace. The object itself remains until the reference count falls to zero.)

 

 




