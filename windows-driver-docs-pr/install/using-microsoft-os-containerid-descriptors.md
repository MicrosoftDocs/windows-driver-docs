---
title: Using Microsoft OS ContainerID Descriptors
description: Using Microsoft OS ContainerID Descriptors
ms.assetid: e51b1bc8-fd9d-40f9-b2ae-9f5886f57c7b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Microsoft OS ContainerID Descriptors


The Microsoft operating system (OS) **ContainerID** descriptor can be used in devices that support simultaneous connections of the device through multiple system buses. An explicitly defined Microsoft OS **ContainerID** descriptor ensures that all the device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) enumerated for the device on the USB bus are grouped into the same device container.

**Note**  If you decide to implement an Microsoft OS **ContainerID** descriptor, the descriptor value must be unique on every device to avoid container ID conflicts.

 

The Microsoft OS **ContainerID** descriptor is useful when a device supports simultaneous connections to the device through more than one bus. In this way, the same container ID is used on each bus supported by the device. This allows the operating system to determine whether functions on each bus are part of the same device container.

If you decide to use a Microsoft OS **ContainerID** within your USB device, you should be aware of the following points:

-   For devices that are not integrated into the computer (that is, all external devices), it is a best practice to always provide a Microsoft OS **ContainerID** descriptor and a serial number in the USB device hardware. This will ensure that the Windows Plug and Play (PnP) infrastructure is able to correctly group all the device functions exposed by the device. Starting with Windows 7, components of the operating system rely on the proper grouping of device functions. Following this practice will provide the best user experience for devices on the Windows platform.

-   USB devices integrated with a computer should never provide a Microsoft OS **ContainerID** descriptor. To ensure that integrated devices are correctly grouped with the computer's device container, integrated devices should rely on ACPI BIOS settings or on the USB hub descriptor **DeviceRemovable** bit for the port.

 

 





