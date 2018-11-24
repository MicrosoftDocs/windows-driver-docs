---
title: Finding and Mapping Hardware Resources
description: This topic describes how a Kernel-Mode Driver Framework (KMDF) driver or User-Mode Driver Framework (UMDF) driver starting in version 2 maps a translated memory resource (CmResourceTypeMemory) that it receives in its EvtDevicePrepareHardware callback function.
ms.assetid: 9D65D70C-FFF1-4663-8701-221C5443C425
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Finding and Mapping Hardware Resources


This topic describes how a Kernel-Mode Driver Framework (KMDF) driver or User-Mode Driver Framework (UMDF) driver starting in version 2 maps a translated memory resource (**CmResourceTypeMemory**) that it receives in its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function.

A UMDF 1.x driver can also receive this type of resource in its [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method. For more info, see [Finding and Mapping Hardware Resources in UMDF 1.x Drivers](finding-and-mapping-hardware-resources-in-umdf-1-x-drivers.md).

Your driver receives [raw and translated](raw-and-translated-resources.md) versions of hardware resources in the device's resource list in its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function. The driver can save the resource list, which is valid until the framework calls the driver's [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function.

Typically, the driver calls [**WdfCmResourceListGetCount**](https://msdn.microsoft.com/library/windows/hardware/ff545687) from its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function to determine the number of resource descriptors in the translated resource list, and then calls [**WdfCmResourceListGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff545688) in a loop to identify memory-mapped registers, I/O ports, and interrupts.

If a driver is assigned a translated memory resource (**CmResourceTypeMemory**), it must map the physical address into an address through which it can access device registers.

A KMDF driver calls [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618) to map the given physical address range to nonpaged system space. Then it uses the [**HAL Library Routines**](https://msdn.microsoft.com/library/windows/hardware/ff546644) to read and write to registers.

A UMDF driver calls [**WdfDeviceMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/dn265605) to map the physical address to a pseudo base address that it can use in conjunction with [WDF Register/Port Access Functions](https://msdn.microsoft.com/library/windows/hardware/dn265662) to read and write to registers and ports.

The driver unmaps the resources by calling [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387) or [**WdfDeviceUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/dn265610) from its [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function.

You do not need to map resources in I/O space (**CmResourceTypePort**, **CmResourceTypeInterrupt**, **CmResourceTypeDma**).

If your UMDF driver calls [**WdfDeviceMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/dn265605), you must set the **UmdfDirectHardwareAccess** INF directive to **AllowDirectHardwareAccess**.

For an example that shows how a driver finds and maps memory-mapped register resources, see [Reading and Writing to Device Registers](reading-and-writing-to-device-registers.md).

 

 





