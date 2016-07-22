---
title: Best Practices for Supporting Container IDs on USB Devices
description: Best Practices for Supporting Container IDs on USB Devices
ms.assetid: 58086d52-196f-4ea3-9ce6-62d3fcb43f9e
---

# Best Practices for Supporting Container IDs on USB Devices


The heuristic used to generate the container ID for a USB device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)), which was discussed in [How USB Devices are Assigned Container IDs](how-usb-devices-are-assigned-container-ids.md), is complex, and relies on information taken from several sources.

Starting with Windows 7, the recommendations that are discussed in this section should be followed to allow the operating system to correctly determine the device container and provide the best user experience for your device.

This section includes the following topics that discuss these recommendations:

[Using Microsoft OS ContainerID Descriptors](using-microsoft-os-containerid-descriptors.md)

[Using the USB Removable Capability for Device Container Grouping](using-the-usb-removable-capability-for-device-container-grouping.md)

[Avoiding Device Container Conflicts](avoiding-device-container-conflicts.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Best%20Practices%20for%20Supporting%20Container%20IDs%20on%20USB%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




