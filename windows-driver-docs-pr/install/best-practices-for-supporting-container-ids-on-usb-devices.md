---
title: Best Practices for Supporting Container IDs on USB Devices
description: Best Practices for Supporting Container IDs on USB Devices
ms.assetid: 58086d52-196f-4ea3-9ce6-62d3fcb43f9e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best Practices for Supporting Container IDs on USB Devices


The heuristic used to generate the container ID for a USB device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)), which was discussed in [How USB Devices are Assigned Container IDs](how-usb-devices-are-assigned-container-ids.md), is complex, and relies on information taken from several sources.

Starting with Windows 7, the recommendations that are discussed in this section should be followed to allow the operating system to correctly determine the device container and provide the best user experience for your device.

This section includes the following topics that discuss these recommendations:

[Using Microsoft OS ContainerID Descriptors](using-microsoft-os-containerid-descriptors.md)

[Using the USB Removable Capability for Device Container Grouping](using-the-usb-removable-capability-for-device-container-grouping.md)

[Avoiding Device Container Conflicts](avoiding-device-container-conflicts.md)

 

 





