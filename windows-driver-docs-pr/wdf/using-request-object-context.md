---
title: Using Request Object Context
description: Using Request Object Context
keywords:
- request objects WDK KMDF , context space
- context space WDK KMDF
ms.date: 04/20/2017
---

# Using Request Object Context





Every framework request object, whether created by the framework or by a driver, can contain driver-defined context space. When a framework-based driver initializes a framework device object, the driver can call [**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes) to specify a [**WDF\_OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure that describes context space for the device's request objects.

The framework allocates context space for request objects as follows:

-   When the framework creates request objects for your driver, it allocates context space with the size that your driver specified when it called **WdfDeviceInitSetRequestAttributes**.

-   If your driver creates additional request objects by calling [**WdfRequestCreate**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate), you can specify a context size by providing a WDF\_OBJECT\_ATTRIBUTES structure.

For more information about allocating and accessing context space for framework objects, see [Framework Object Context Space](framework-object-context-space.md).

 

