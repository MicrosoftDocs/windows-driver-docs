---
title: Uninstalling Devices and Driver Packages
description: Uninstalling Devices and Driver Packages
ms.assetid: 4381ee42-778b-402d-b242-892ec921c28f
---

# Uninstalling Devices and Driver Packages


After a device is installed, it might be necessary to uninstall a device or a [driver package](driver-packages.md). For example, an end-user might decide to replace the associated device, or the driver package might have to be uninstalled when a driver is updated.

When you uninstall a device, you must remove the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that represents the physical instance of the device in the system.

When you uninstall a [driver package](driver-packages.md), you must complete the following actions:

-   Remove the files that are associated with the [driver package](driver-packages.md) from the [driver store](driver-store.md).

-   Delete the binary files of the driver package.

This section describes how to uninstall devices and driver packages. It is intended for driver developers who want to provide instructions or tools to their customers.

This section includes the following topics:

[How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md)

[Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md)

[Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md)

[Using the DIFx Tools to Uninstall Driver Packages](using-the-difx-tools-to-uninstall-driver-packages.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Uninstalling%20Devices%20and%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




