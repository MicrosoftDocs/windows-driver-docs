---
title: Accessing the Properties of Installed Device Interfaces
description: Accessing the Properties of Installed Device Interfaces
keywords:
- device interfaces WDK device installations , accessing properties
ms.date: 04/20/2017
---

# Accessing the Properties of Installed Device Interfaces


To discover the attributes of device interfaces that are registered on the system, you must not open, read, or write the device interface subkeys by directly accessing the registry. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely query and modify the attributes of device interfaces:

-   User-mode applications should follow these steps:

    1.  Use [**SetupDiOpenDeviceInterface**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfacea) to locate a device interface and add it to a set from its name.

    2.  Use [**SetupDiGetDeviceInterfaceDetail**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetaila) to retrieve details for the device interface.

        The optional *DeviceInfoData* parameter will receive the [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) element for the device for which the interface is registered.

    3.  Use persistent registry storage for the custom settings for a device interface class. To do this, use [**SetupDiCreateDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeya) (to create a new registry key) or [**SetupDiOpenDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey) (to open an existing registry key).

        To save the custom settings, use [RegCloseKey](/windows/win32/api/winreg/nf-winreg-regclosekey) after the registry key has been created or opened.

-   Kernel-mode drivers should use [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) to open the registry key for a device interface class.

