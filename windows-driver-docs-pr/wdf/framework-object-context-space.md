---
title: Framework Object Context Space
description: Framework Object Context Space
keywords:
- framework objects WDK KMDF , context space
- context space WDK KMDF
- object context space WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Object Context Space





*Object context space* is extra, nonpageable, memory space that a driver can allocate and assign to an object. Each framework-based driver can create one or more object-specific context spaces for every framework object that the driver receives or creates.

Framework-based drivers should store all object-specific data, either by value or by pointer, within the context space of the object to which the data belongs.

For example, a driver for USB devices might create context space for its framework device objects. In the context space, the driver might store such device-specific information as the device's [**USB\_DEVICE\_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_device_descriptor) and [**USB\_CONFIGURATION\_DESCRIPTOR**](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_configuration_descriptor) structures, plus a handle to a [collection object](framework-object-collections.md) that represents a device interface's pipes.

The framework does not pass framework objects from one driver to another, so you cannot use an object's context space to pass data between two drivers.

To define an object's context space, you must create one or more structures. Each structure represents a separate context space. Your driver will use each structure member to store a piece of object-specific information. Additionally, your driver must ask the framework to generate an *accessor method* for each structure. This accessor method accepts an object handle as input and returns the address of the object's context space.

Whenever your driver calls an object creation method, such as [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate), the method optionally allocates context space. All object creation methods accept an optional [**WDF\_OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure as input. This structure describes the context space that you want the framework to allocate for the object.

To add additional context space to an object after the driver has called the object's creation method, the driver can call the [**WdfObjectAllocateContext**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectallocatecontext) method--which, like the object creation methods, accepts a [**WDF\_OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure as input.

When the framework allocates context space for an object, it also zero-initializes the context space.

When either the framework or a driver deletes a framework object, the framework deletes all of the object's context space.

If your driver uses context space to store pointers to buffers that the driver allocates when it creates an object, the driver should provide an [*EvtCleanupCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup) function that deallocates the buffers when the object is deleted.

To define an object's context space structure and accessor method for the objects that your driver creates, your driver must use the following steps:

1.  Define a structure that describes the data that you want to store. For example, if you want to create context data for your driver's device objects, your driver might define a structure called MY\_DEVICE\_CONTEXT.

2.  Use either the [**WDF\_DECLARE\_CONTEXT\_TYPE**](./wdf-declare-context-type.md) macro or the [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](./wdf-declare-context-type-with-name.md) macro. Both of these macros do the following:

    -   Create and initialize a [**WDF\_OBJECT\_CONTEXT\_TYPE\_INFO**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_context_type_info) structure.
    -   Define an accessor method that your driver will later use to access an object's context space. The accessor method's return value is a pointer to the object's context space.

    The WDF\_DECLARE\_CONTEXT\_TYPE macro creates the accessor method's name from your structure's name. For example, if your context structure's name is MY\_DEVICE\_CONTEXT, the macro creates an accessor method that is named **WdfObjectGet\_MY\_DEVICE\_CONTEXT**.

    The WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME macro lets you specify the accessor method's name. For example, you might specify **GetMyDeviceContext** as the name for your context accessor method for device objects.

3.  Call [**WDF\_OBJECT\_ATTRIBUTES\_INIT**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdf_object_attributes_init) to initialize the object's [**WDF\_OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure.

4.  Use the [**WDF\_OBJECT\_ATTRIBUTES\_SET\_CONTEXT\_TYPE**](./wdf-object-attributes-set-context-type.md) macro to set the **ContextTypeInfo** member of the WDF\_OBJECT\_ATTRIBUTES structure to the address of the WDF\_OBJECT\_CONTEXT\_TYPE\_INFO structure.

5.  Call an object creation method, such as [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate).

After your driver has created an object, the driver can call [**WdfObjectAllocateContext**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectallocatecontext) at any time to add additional context space to the object.

Because steps 1 and 2 define global data structures and create a driver-callable routine, your driver must complete these steps in an area of the driver that declares global data--typically a header file. These steps must not be completed from within your driver's routines.

Your driver must complete steps 3, 4, and 5 from within a driver routine that creates an object, such as an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function that calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate).

The framework can create two types of objects -- framework request objects and framework file objects -- on behalf of your driver. Your driver can register context space for these objects by calling [**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes) and [**WdfDeviceInitSetFileObjectConfig**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig), respectively. Your driver can also call [**WdfObjectAllocateContext**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectallocatecontext) to allocate context space for these objects.

After an object has been created, the driver can obtain a pointer to the object's context space by using either of the following techniques:

-   Call the context accessor method that you created in step 2 in the preceding procedure by using either the [**WDF\_DECLARE\_CONTEXT\_TYPE**](./wdf-declare-context-type.md) or the [**WDF\_DECLARE\_CONTEXT\_TYPE\_WITH\_NAME**](./wdf-declare-context-type-with-name.md) macro.

-   Call [**WdfObjectGetTypedContext**](./wdfobjectgettypedcontext.md), supplying the name of your driver-defined context structure.

If your driver has a context space pointer, it can find the object that the context space belongs to by calling [**WdfObjectContextGetObject**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectcontextgetobject).

 

