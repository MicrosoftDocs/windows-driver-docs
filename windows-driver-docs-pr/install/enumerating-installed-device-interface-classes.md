---
title: Enumerating Installed Device Interfaces
description: Enumerating Installed Device Interfaces
keywords:
- enumerating installed device interfaces WDK
- installed device interfaces WDK
- installed device interfaces WDK , enumerating
- device interfaces WDK device installations , enumerating
ms.date: 04/20/2017
---

# Enumerating Installed Device Interfaces


You must not enumerate the device interface classes in a system by directly accessing registry keys. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely discover the attributes of device interfaces:

-   User-mode applications should follow these steps:

    1.  Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) or [**SetupDiGetClassDevsEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa) to retrieve the devices that support interfaces for the specified device interface class. You must set the DIGCF_DEVICEINTERFACE flag in the *Flags* parameter, and you must set the *Enumerator* parameter to a specific device instance identifier.

        To include only device interfaces that are present in a system, set the DIGCF_PRESENT flag in the *Flags* parameter.

    2.  Use [**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) to enumerate interfaces that are registered for a device interface class. This interface class is specified through the *InterfaceClassGuid* parameter.

-   Kernel-mode drivers should use [**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces) to enumerate the device interface classes that are installed in the system.

 

