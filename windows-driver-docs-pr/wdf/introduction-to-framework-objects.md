---
title: Introduction to Framework Objects
description: Introduction to Framework Objects
ms.assetid: 1314501a-bff1-4aac-a391-a72acca9cc26
keywords: ["framework objects WDK KMDF about framework objects", "reference counts WDK KMDF", "deletion callback functions WDK KMDF", "callback functions WDK KMDF", "parent objects WDK KMDF"]
---

# Introduction to Framework Objects


## <a href="" id="ddk-introduction-to-framework-objects-df"></a>


The interfaces that Windows Driver Frameworks (WDF) provides to drivers are object-based. The framework defines several objects. These objects export [methods](framework-object-methods.md) (functions) and [properties](framework-object-properties.md) (data) that drivers can access. Framework objects also initiate [events](framework-object-events.md), which drivers can support by providing event callback functions.

Framework-based drivers never directly access framework objects. Instead, drivers reference the objects by *handles*, which the driver passes as input to object methods.

All framework objects have the following characteristics:

<a href="" id="reference-count"></a>*Reference count*  
The framework maintains a count of the number of references to each object. When the framework creates an object, it sets the object's reference count to one. When the framework has finished using an object, it decrements the reference count. The framework cannot delete the object until the reference count is decremented to zero, so drivers can prevent the deletion of an object by incrementing its reference count.

<a href="" id="context-space"></a>*Context space*  
Framework-based drivers can create object-specific context space for every framework object that the driver receives or creates. Drivers should store all object-specific data in an object's context space. For more information about context space, see [Framework Object Context Space](framework-object-context-space.md).

<a href="" id="deletion-callback-functions"></a>*Deletion callback functions*  
Drivers can register callback functions that the framework calls when it is deleting an object. The callback functions can remove driver-assigned resources, such as object-specific memory allocations. For more information about these callback functions, see [Framework Object Life Cycle](framework-object-life-cycle.md).

<a href="" id="parent-object"></a>*Parent object*  
All framework objects can have a parent object. The framework designates a default parent object for most objects. When a driver creates an object, it can designate a parent object that overrides the object's default parent object. To designate an object's parent object, drivers set the **ParentObject** member of the object's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure. (For a few object types, drivers cannot override the default parent object.) When the framework or a driver deletes a parent object, the framework also deletes the parent object's children.

For an overview of all of the objects that are defined by WDF, see [Summary of Framework Objects](summary-of-framework-objects.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Introduction%20to%20Framework%20Objects%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




