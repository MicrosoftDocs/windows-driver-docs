---
title: Avoiding Device Container Conflicts
description: Avoiding Device Container Conflicts
ms.assetid: 1c752333-8776-4c5e-bc2f-47ffde60c931
---

# Avoiding Device Container Conflicts


Attaching two or more devices to a computer which share the same container ID (explicitly defined by using Microsoft operating system (OS) **ContainerID** descriptor or the same USB serial number) will result in a device container conflict. The operating system will interpret the device functions as originating from a single device and will create a single device container. This could cause unexpected behavior with the devices and within Windows.

To avoid this problem, ensure that the Microsoft OS **ContainerID** descriptor value and USB serial number are unique to a single physical device. Do not share these values among devices in a product line.

If your USB device relies on the operating system to generate a container ID based on the USB serial number, the container ID is generated as follows:

1.  The operating system concatenates the USB device serial number, vendor ID, product ID, and revision number to generate a string.

2.  The string that results is hashed into a GUID by using the UUID Version 5 (SHA-1) hash algorithm under a USB-specific namespace. The generated container ID will be unique, provided the independent hardware vendor (IHV) provides a unique serial number on each device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Avoiding%20Device%20Container%20Conflicts%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




