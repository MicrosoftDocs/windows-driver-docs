---
title: Avoiding Device Container Conflicts
description: Avoiding Device Container Conflicts
ms.assetid: 1c752333-8776-4c5e-bc2f-47ffde60c931
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Avoiding Device Container Conflicts


Attaching two or more devices to a computer which share the same container ID (explicitly defined by using Microsoft operating system (OS) **ContainerID** descriptor or the same USB serial number) will result in a device container conflict. The operating system will interpret the device functions as originating from a single device and will create a single device container. This could cause unexpected behavior with the devices and within Windows.

To avoid this problem, ensure that the Microsoft OS **ContainerID** descriptor value and USB serial number are unique to a single physical device. Do not share these values among devices in a product line.

If your USB device relies on the operating system to generate a container ID based on the USB serial number, the container ID is generated as follows:

1.  The operating system concatenates the USB device serial number, vendor ID, product ID, and revision number to generate a string.

2.  The string that results is hashed into a GUID by using the UUID Version 5 (SHA-1) hash algorithm under a USB-specific namespace. The generated container ID will be unique, provided the independent hardware vendor (IHV) provides a unique serial number on each device.

 

 





