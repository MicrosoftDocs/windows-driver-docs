---
title: Container ID
description: A container ID is a system-supplied device identification string that uniquely groups the functional devices associated with a single-function or multifunction device installed in the computer.
ms.assetid: 66e0c68a-c7bd-4d85-a438-0342c5943562
---

# Container ID


A container ID is a system-supplied device identification string that uniquely groups the functional devices associated with a single-function or multifunction device installed in the computer.

Starting with Windows 7, the Plug and Play (PnP) manager uses the container ID to group one or more device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that originated from and belong to each instance of a particular physical device. This instance is referred to as the *device* *container*.

Grouping all the devnodes that originated from an instance of a single device achieves the following:

-   The operating system can determine how functionality is related among child devnodes and their container devnode.

-   The user or applications are presented with a device-centric view of devices instead of the traditional function-centric view.

This section contains topics that discuss the container ID in more detail:

[Overview of Container IDs](overview-of-container-ids.md)

[How Container IDs are Generated](how-container-ids-are-generated.md)

[Verifying the Implementation of Container IDs](verifying-the-implementation-of-container-ids.md)

[Troubleshooting the Implementation of Container IDs](troubleshooting-the-implementation-of-container-ids.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20ID%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




