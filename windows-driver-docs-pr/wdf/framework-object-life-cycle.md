---
title: Framework Object Life Cycle
description: Framework Object Life Cycle
keywords:
- framework objects WDK KMDF , life cycle
- life cycles WDK KMDF
- framework objects WDK KMDF , creating
- reference counts WDK KMDF
- framework objects WDK KMDF , deleting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Object Life Cycle





A framework object's "life cycle" spans the time from when an object is created to when it is deleted. An object's reference count controls when it will be deleted.

### Creating a Framework Object

Most framework objects are created by a driver's call to the object's creation method. For example, each framework driver must call [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate) to create a framework driver object.

Other framework objects are created by the framework. For example, when a user application opens a device for read or write operations, the framework creates a framework file object and passes it to the driver's [*EvtDeviceFileCreate*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_file_create) callback function.

A few framework objects can be created by either the framework or by a driver. For example, when the I/O manager delivers an I/O request to a driver, the framework creates a framework request object and delivers it to the driver, typically by calling one of the driver's request handlers. A driver can also create framework request objects and deliver them to other drivers.

### Using Reference Counts

The framework maintains a reference count for each object. When an object is created, the framework sets its reference count to one. If the reference count becomes zero, the framework deletes the object.

Drivers can modify an object's reference count by calling [**WdfObjectReference**](./wdfobjectreference.md) to increment the reference count or [**WdfObjectDereference**](./wdfobjectdereference.md) to decrement the reference count. (A driver can call **WdfObjectDereference** only if it has previously called **WdfObjectReference**.)

In most cases, drivers do not have to increment or decrement an object's reference count. The framework increments the count before it passes the object's handle to the driver, and it decrements the count when the driver no longer needs the object.

Drivers call [**WdfObjectReference**](./wdfobjectreference.md) to ensure that an object will not be deleted (by the framework or by a driver thread) before the driver has finished using it. For an example situation in which a driver should call **WdfObjectReference** and [**WdfObjectDereference**](./wdfobjectdereference.md), see [Synchronizing Cancellation of Sent Requests](synchronizing-cancellation-of-sent-requests.md).

### Deleting a Framework Object

Objects are deleted either because a driver calls [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) or because the framework calls an internal deletion routine, but an object is deleted only if its reference count is zero. After the driver or the framework has attempted to delete an object, the object's handle remains valid until after the reference count becomes zero. A driver *cannot* delete an object by simply calling [**WdfObjectDereference**](./wdfobjectdereference.md) to decrement the object's reference count to zero--the driver must also call **WdfObjectDelete**.

If a framework object is the child object of a parent and the parent is being deleted, the framework attempts to delete the child object before it deletes the parent. Object deletion starts from the object farthest from the parent and works up the object hierarchy toward the root.

Drivers can register the following two callback functions that the framework calls when the driver or the framework is deleting an object:

-   An [*EvtCleanupCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup) callback function, which the framework calls so that the driver can call [**WdfObjectDereference**](./wdfobjectdereference.md) if it had previously called [**WdfObjectReference**](./wdfobjectreference.md) for the object that is being deleted.

-   An [*EvtDestroyCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy) callback function, which the framework calls after the object's reference count has been decremented to zero.

One of these callback functions must deallocate any object-specific resources that the driver allocated when the object was created.

The framework always handles the deletion of some framework objects, and drivers must not attempt to delete these objects. For a list of framework objects that drivers cannot delete, see [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

 

