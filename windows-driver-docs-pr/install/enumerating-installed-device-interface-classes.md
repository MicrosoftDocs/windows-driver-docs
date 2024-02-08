---
title: Enumerating Installed Device Interfaces
description: Provides information about enumerating installed device interfaces.
keywords:
- enumerating installed device interfaces WDK
- installed device interfaces WDK
- installed device interfaces WDK , enumerating
- device interfaces WDK device installations , enumerating
ms.date: 08/15/2022
---

# Enumerating installed device interfaces

You must not enumerate the device interfaces in a system by directly accessing registry keys. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely enumerate device interfaces.

User-mode applications should follow these steps:

- Using [configuration manager](/windows/win32/api/cfgmgr32/) functions:

    Use [**CM_Get_Device_Interface_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_listw) to retrieve a list of device interfaces in the specified *InterfaceClassGuid*. You can optionally restrict the list to only device interfaces exposed by a particular device by setting the *pDeviceID* parameter to a specific device instance identifier.

    To include only device interfaces that are present (enabled) in a system, set the *CM_GET_DEVICE_INTERFACE_LIST_PRESENT* flag in the *ulFlags* parameter.

- Using [SetupApi](setupapi.md) functions:

    1. Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) or [**SetupDiGetClassDevsEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa) with the *DIGCF_DEVICEINTERFACE* flag set in the *Flags* parameter to retrieve the device interfaces for the specified device interface class. You can optionally restrict the list to only device interfaces exposed by a particular device by setting the *Enumerator* parameter to a specific device instance identifier.

        To include only device interfaces that are present (enabled) in a system, set the *DIGCF_PRESENT* flag in the *Flags* parameter.

    1. Use [**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) to enumerate interfaces returned by the above calls.

Kernel-mode drivers should use [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to retrieve a list of device interfaces in the specified *InterfaceClassGuid*.  You can optionally restrict the list to only device interfaces exposed by a particular device by setting the *PhysicalDeviceObject* parameter.
