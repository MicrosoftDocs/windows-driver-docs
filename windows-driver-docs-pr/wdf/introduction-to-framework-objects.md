---
title: Introduction to Framework Objects
description: Introduction to Framework Objects
ms.assetid: 1314501a-bff1-4aac-a391-a72acca9cc26
keywords:
- framework objects WDK KMDF , about framework objects
- reference counts WDK KMDF
- deletion callback functions WDK KMDF
- callback functions WDK KMDF
- parent objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Framework Objects





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

 

 





