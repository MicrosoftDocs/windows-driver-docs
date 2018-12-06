---
title: Accessing the Properties of Installed Device Interfaces
description: Accessing the Properties of Installed Device Interfaces
ms.assetid: 4079DD59-878E-4b71-9815-543BA838C56D
keywords:
- device interfaces WDK device installations , accessing properties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Properties of Installed Device Interfaces


To discover the attributes of device interfaces that are registered on the system, you must not open, read, or write the device interface subkeys by directly accessing the registry. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely query and modify the attributes of device interfaces:

-   User-mode applications should follow these steps:

    1.  Use [**SetupDiOpenDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff552074) to locate a device interface and add it to a set from its name.

    2.  Use [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) to retrieve details for the device interface.

        The optional *DeviceInfoData* parameter will receive the [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) element for the device for which the interface is registered.

    3.  Use persistent registry storage for the custom settings for a device interface class. To do this, use [**SetupDiCreateDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550967) (to create a new registry key) or [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075) (to open an existing registry key).

        To save the custom settings, use [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) after the registry key has been created or opened.

-   Kernel-mode drivers should use [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) to open the registry key for a device interface class.

 

 





