---
title: Finding and Mapping Hardware Resources
description: This topic describes how a Kernel Mode Driver Framework (KMDF) driver or User Mode Driver Framework (UMDF) driver starting in version 2 maps a translated memory resource (CmResourceTypeMemory) that it receives in its EvtDevicePrepareHardware callback function.
ms.assetid: 9D65D70C-FFF1-4663-8701-221C5443C425
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Finding%20and%20Mapping%20Hardware%20Resources%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




