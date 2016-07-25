---
title: Container IDs for Bluetooth Devices
description: Container IDs for Bluetooth Devices
ms.assetid: 7e9c40d9-ed19-4ad2-a749-6e3f4aaca2de
---

# Container IDs for Bluetooth Devices


For a Bluetooth device that is connected to the computer, the device's media access control (MAC) address is used to generate a container ID for the device.

The Bluetooth bus driver uses the MAC address as a seed value to generate a unique container ID for the device. This container ID is supplied by the Bluetooth bus driver for each Bluetooth device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that is enumerated for a physical device.

Bluetooth devices frequently implement Bluetooth-specific services. These services are not installed as Windows PnP devices and therefore do not have associated devnodes. However, these services are effectively functional device instances, because they provide specific functionality and enable communication with the Bluetooth device.

Starting with Windows 7, the operating system considers Bluetooth services to be functional device interfaces, and groups these services together with the Bluetooth devnodes for a device.

All Bluetooth devices must include a MAC address. Therefore, a container ID for Bluetooth devnodes and services is always based on the MAC address value. Unlike USB devices, the removable device capability is never used to generate container IDs for Bluetooth devices.

To ensure that a unique container ID is generated for every device, developers of Bluetooth devices must configure each device with a unique MAC address.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20Bluetooth%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




