---
title: Debugging a Failed Driver Unload
description: Debugging a Failed Driver Unload
ms.assetid: df4b6082-8236-4a7f-80f4-6c33dc8e887a
keywords: ["failed driver unload", "driver unload debugging", "unload failures"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Failed Driver Unload


## <span id="ddk_debugging_a_failed_driver_unload_dbg"></span><span id="DDK_DEBUGGING_A_FAILED_DRIVER_UNLOAD_DBG"></span>


A driver will not unload if there is a leaked reference to **DeviceObject** or **DriverObject**. This is a common cause of failed driver unloads.

Apart from **IoCreateDevice**, there are several functions that take reference to **DriverObject** and **DeviceObject**. If you do not follow the guidelines for using the functions, you will end up leaking the reference.

Here is an example of how to debug this problem. Although **DeviceObject** is used in this example, this technique works for all objects.

**Fixing a driver that fails to unload**

1.  Put a breakpoint right after the driver calls **IoCreateDevice**. Get the **DeviceObject** address.

2.  Find the object header by using the [**!object**](-object.md) extension on this object address:

    ```dbgcmd
    kd> !object 81a578c0 
    Object: 81a578c0  Type: (81bd0e70) Device
        ObjectHeader: 81a578a8
        HandleCount: 0  PointerCount: 3
        Directory Object: e1001208  Name: Serial0 
    ```

    The first variable in the **ObjectHeader** is the *pointer count* or *reference count*.

3.  Put a write breakpoint on the pointer count, using the **ObjectHeader**'s address:

    ```dbgcmd
    kd> ba w4 81a578a8 "k;g" 
    ```

4.  Use [**g (Go)**](g--go-.md). The debugger will produce a log.

5.  Look for the mismatched reference/dereference pair -- specifically, a missing dereference. (Note that **ObReferenceObject** is implemented as a macro inside the kernel.)

 

 





