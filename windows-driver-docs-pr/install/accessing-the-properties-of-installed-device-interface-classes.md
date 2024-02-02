---
title: Access the Properties of Installed Device Interfaces
description: Provides information about how to access the properties of installed device interfaces.
keywords:
- device interfaces WDK device installations, access properties
ms.date: 08/29/2022
---

# Access the properties of installed device interfaces

To discover the attributes of device interfaces that are registered on the system, you must not open, read, or write the device interface subkeys by directly accessing the registry. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely query and modify the attributes of device interfaces.

User-mode applications should follow these steps:

- Using [configuration manager](/windows/win32/api/cfgmgr32/) functions:
    1. Use [**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) and [**CM_Set_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw) to get and set device interface properties or use [**CM_Open_Device_Interface_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_device_interface_keyw) to access a persistent registry storage location for the device interface.

- Using [SetupAPI](setupapi.md) functions:

    1. Use [**SetupDiOpenDeviceInterface**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfacew) to add a specified device interface to a set from its name.

    1. Use [**SetupDiGetDeviceInterfaceDetail**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetailw) to retrieve details for the device interface.

        The optional *DeviceInfoData* parameter will receive the [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) element for the device for which the interface is registered.

    1. Use [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) and [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw) to get and set device interface properties or use [**SetupDiCreateDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeyw) (to create a new registry key) or [**SetupDiOpenDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey) (to open an existing registry key) to access a persistent registry storage location for the device interface.

Kernel-mode drivers should use [**IoGetDeviceInterfacePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfacepropertydata) and [**IoSetDeviceInterfacePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata) to get and set device interface properties or use [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey)  to access a persistent registry storage location for the device interface.
