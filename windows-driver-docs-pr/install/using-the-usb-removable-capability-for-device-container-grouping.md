---
title: Using the USB Removable Capability for Device Container Grouping
description: Using the USB Removable Capability for Device Container Grouping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the USB Removable Capability for Device Container Grouping


The USB **Removable** capability allows the operating system to create a device container for legacy devices. This mechanism exists to provide backward compatibility for devices that cannot provide a Microsoft OS **ContainerID** descriptor or for devices integrated with a computer which does not have a USB port capabilities (**_UPC**) value for the corresponding USB port.

It is important to recognize that the USB hub driver uses available removability information from the physical USB hardware in order to report a more accurate **Removable** capability for devices connected to each of its internal or external-facing ports. For more information, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

 

 





