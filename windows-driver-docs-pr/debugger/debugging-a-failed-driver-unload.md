---
title: Debugging a Failed Driver Unload
description: Debugging a Failed Driver Unload
ms.assetid: df4b6082-8236-4a7f-80f4-6c33dc8e887a
keywords: ["failed driver unload", "driver unload debugging", "unload failures"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging a Failed Driver Unload


## <span id="ddk_debugging_a_failed_driver_unload_dbg"></span><span id="DDK_DEBUGGING_A_FAILED_DRIVER_UNLOAD_DBG"></span>


A driver will not unload if there is a leaked reference to **DeviceObject** or **DriverObject**. This is a common cause of failed driver unloads.

Apart from **IoCreateDevice**, there are several functions that take reference to **DriverObject** and **DeviceObject**. If you do not follow the guidelines for using the functions, you will end up leaking the reference.

Here is an example of how to debug this problem. Although **DeviceObject** is used in this example, this technique works for all objects.

**Fixing a driver that fails to unload**

1.  Put a breakpoint right after the driver calls **IoCreateDevice**. Get the **DeviceObject** address.

2.  Find the object header by using the [**!object**](-object.md) extension on this object address:

    ``` syntax
    kd> !object 81a578c0 
    Object: 81a578c0  Type: (81bd0e70) Device
        ObjectHeader: 81a578a8
        HandleCount: 0  PointerCount: 3
        Directory Object: e1001208  Name: Serial0 
    ```

    The first variable in the **ObjectHeader** is the *pointer count* or *reference count*.

3.  Put a write breakpoint on the pointer count, using the **ObjectHeader**'s address:

    ``` syntax
    kd> ba w4 81a578a8 "k;g" 
    ```

4.  Use [**g (Go)**](g--go-.md). The debugger will produce a log.

5.  Look for the mismatched reference/dereference pair -- specifically, a missing dereference. (Note that **ObReferenceObject** is implemented as a macro inside the kernel.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Failed%20Driver%20Unload%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




