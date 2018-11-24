---
title: Container IDs for Bluetooth Devices
description: Container IDs for Bluetooth Devices
ms.assetid: 7e9c40d9-ed19-4ad2-a749-6e3f4aaca2de
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container IDs for Bluetooth Devices


For a Bluetooth device that is connected to the computer, the device's media access control (MAC) address is used to generate a container ID for the device.

The Bluetooth bus driver uses the MAC address as a seed value to generate a unique container ID for the device. This container ID is supplied by the Bluetooth bus driver for each Bluetooth device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that is enumerated for a physical device.

Bluetooth devices frequently implement Bluetooth-specific services. These services are not installed as Windows PnP devices and therefore do not have associated devnodes. However, these services are effectively functional device instances, because they provide specific functionality and enable communication with the Bluetooth device.

Starting with Windows 7, the operating system considers Bluetooth services to be functional device interfaces, and groups these services together with the Bluetooth devnodes for a device.

All Bluetooth devices must include a MAC address. Therefore, a container ID for Bluetooth devnodes and services is always based on the MAC address value. Unlike USB devices, the removable device capability is never used to generate container IDs for Bluetooth devices.

To ensure that a unique container ID is generated for every device, developers of Bluetooth devices must configure each device with a unique MAC address.

 

 





