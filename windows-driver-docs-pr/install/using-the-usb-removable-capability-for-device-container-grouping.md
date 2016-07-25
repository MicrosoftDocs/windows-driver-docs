---
title: Using the USB Removable Capability for Device Container Grouping
description: Using the USB Removable Capability for Device Container Grouping
ms.assetid: ed78a544-1035-4b99-b27c-90ebef2ed710
---

# Using the USB Removable Capability for Device Container Grouping


The USB **Removable** capability allows the operating system to create a device container for legacy devices. This mechanism exists to provide backward compatibility for devices that cannot provide a Microsoft OS **ContainerID** descriptor or for devices integrated with a computer which does not have a USB port capabilities (**\_UPC**) value for the corresponding USB port.

It is important to recognize that the USB hub driver uses available removability information from the physical USB hardware in order to report a more accurate **Removable** capability for devices connected to each of its internal or external-facing ports. For more information, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20the%20USB%20Removable%20Capability%20for%20Device%20Container%20Grouping%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




