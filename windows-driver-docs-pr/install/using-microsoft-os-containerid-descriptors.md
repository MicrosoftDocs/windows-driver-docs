---
title: Using Microsoft OS ContainerID Descriptors
description: Using Microsoft OS ContainerID Descriptors
ms.assetid: e51b1bc8-fd9d-40f9-b2ae-9f5886f57c7b
---

# Using Microsoft OS ContainerID Descriptors


The Microsoft operating system (OS) **ContainerID** descriptor can be used in devices that support simultaneous connections of the device through multiple system buses. An explicitly defined Microsoft OS **ContainerID** descriptor ensures that all the device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) enumerated for the device on the USB bus are grouped into the same device container.

**Note**  If you decide to implement an Microsoft OS **ContainerID** descriptor, the descriptor value must be unique on every device to avoid container ID conflicts.

 

The Microsoft OS **ContainerID** descriptor is useful when a device supports simultaneous connections to the device through more than one bus. In this way, the same container ID is used on each bus supported by the device. This allows the operating system to determine whether functions on each bus are part of the same device container.

If you decide to use a Microsoft OS **ContainerID** within your USB device, you should be aware of the following points:

-   For devices that are not integrated into the computer (that is, all external devices), it is a best practice to always provide a Microsoft OS **ContainerID** descriptor and a serial number in the USB device hardware. This will ensure that the Windows Plug and Play (PnP) infrastructure is able to correctly group all the device functions exposed by the device. Starting with Windows 7, components of the operating system rely on the proper grouping of device functions. Following this practice will provide the best user experience for devices on the Windows platform.

-   USB devices integrated with a computer should never provide a Microsoft OS **ContainerID** descriptor. To ensure that integrated devices are correctly grouped with the computer's device container, integrated devices should rely on ACPI BIOS settings or on the USB hub descriptor **DeviceRemovable** bit for the port.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20Microsoft%20OS%20ContainerID%20Descriptors%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




