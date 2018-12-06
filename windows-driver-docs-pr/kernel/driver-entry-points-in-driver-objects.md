---
title: Driver Entry Points in Driver Objects
description: Driver Entry Points in Driver Objects
ms.assetid: f004c2b3-8435-4c25-82e9-aff3911dc316
keywords: ["driver objects WDK kernel", "standard driver routines WDK kernel , driver objects", "driver routines WDK kernel , driver objects", "routines WDK kernel , driver objects", "objects WDK driver objects", "entry points WDK kernel", "driver entry points WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Driver Entry Points in Driver Objects





A kernel-mode driver must specify the following entry points in its driver object:

-   At least one dispatch routine's entry point, in order to get IRPs requesting PnP, power, and I/O operations.

-   The entry point of its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, at **DriverObject -&gt; DriverExtension -&gt; AddDevice**.

-   The entry point of its [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, if it manages its own queue of IRPs.

-   If the driver can be loaded and/or replaced dynamically, an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) entry point in order to free any system resources, such as system objects or memory, that the driver has allocated. (Drivers that cannot be replaced while the system is running, such as a keyboard driver, need not supply an *Unload* routine.)

These requirements do not apply to some miniport drivers, for which the corresponding class or port driver defines the entry points in the driver object. See the device-type-specific documentation for details.

The I/O manager maintains information about driver-created device objects in the corresponding driver object.

When a driver is loaded, its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine is called with a pointer to the driver object. When a driver's **DriverEntry** routine is called, it sets *Dispatch*, *StartIo* (if any), and *Unload* (if any) entry points directly in the driver object as follows:

```cpp
DriverObject->MajorFunction[IRP_MJ_xxx] = DDDispatchXxx; 
              :    : 
DriverObject->MajorFunction[IRP_MJ_yyy] = DDDispatchYyy; 
              :    : 
DriverObject->DriverStartIo = DDStartIo; 
DriverObject->DriverUnload = DDUnload; 
              :    : 
```

The **DriverEntry** routine also sets the entry point of its *AddDevice* routine, in the **DriverExtension** of its driver object, as follows:

```cpp
DriverObject->DriverExtension->AddDevice = DDAddDevice; 
```

A **DriverEntry** or optional [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routine also can use a field in the driver object (not shown in the [driver object illustration](introduction-to-driver-objects.md#driver-object-illustration)) to get information from and/or set information in the configuration manager's registry database. For more information, see [Registry Keys for Drivers](https://msdn.microsoft.com/library/windows/hardware/ff549538).

The I/O manager exports no support routines to manipulate driver objects, which are [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structures. Driver objects are used by the I/O manager to keep track of currently loaded drivers. Some members of a driver object are used only by the I/O manager. Others members are also used by driver writers; for example, you must know certain member names to define *AddDevice*, *Dispatch*, *StartIo*, and *Unload* entry points. You should neither attempt to use undocumented members within a **DRIVER\_OBJECT** structure, nor make assumptions about the locations of any driver object members that are named in this documentation. Otherwise, you cannot maintain the portability of a driver from one Windows platform to another.

 

 




