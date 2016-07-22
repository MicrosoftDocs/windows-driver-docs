---
title: Accessing the Properties of Installed Device Interfaces
description: Accessing the Properties of Installed Device Interfaces
ms.assetid: 4079DD59-878E-4b71-9815-543BA838C56D
keywords: ["device interfaces WDK device installations , accessing properties"]
---

# Accessing the Properties of Installed Device Interfaces


To discover the attributes of device interfaces that are registered on the system, you must not open, read, or write the device interface subkeys by directly accessing the registry. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely query and modify the attributes of device interfaces:

-   User-mode applications should follow these steps:

    1.  Use [**SetupDiOpenDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff552074) to locate a device interface and add it to a set from its name.

    2.  Use [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) to retrieve details for the device interface.

        The optional *DeviceInfoData* parameter will receive the [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) element for the device for which the interface is registered.

    3.  Use persistent registry storage for the custom settings for a device interface class. To do this, use [**SetupDiCreateDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550967) (to create a new registry key) or [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075) (to open an existing registry key).

        To save the custom settings, use [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) after the registry key has been created or opened.

-   Kernel-mode drivers should use [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) to open the registry key for a device interface class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20the%20Properties%20of%20Installed%20Device%20Interfaces%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




