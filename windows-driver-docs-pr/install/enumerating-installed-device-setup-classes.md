---
title: Enumerating Installed Device Setup Classes
description: Enumerating Installed Device Setup Classes
keywords:
- enumerating installed device setup classes WDK
- installed device setup classes WDK
- installed device setup classes WDK , enumerating
- device setup classes WDK device installations , enumerating
ms.date: 04/20/2017
---

# Enumerating Installed Device Setup Classes


To discover the [device setup classes](./overview-of-device-setup-classes.md) that are installed in a system, do not enumerate the device setup classes by directly accessing registry keys. As with any registry key, the location and format of these keys might change between different versions of Windows.

To safely discover the installed device setup classes, and to query and modify the properties of a setup class, follow these steps:

1.  Use [**SetupDiBuildClassInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolist) or [**SetupDiBuildClassInfoListEx**](/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolistexa) to retrieve the set of device setup classes that are currently installed on the system.

2.  Use [**SetupDiGetClassDescription**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptiona) or [**SetupDiGetClassDescriptionEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptionexa) to retrieve the description of an installed setup class.

3.  Use [**SetupDiGetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertya) to query the setup class properties and [**SetupDiSetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya) to set the setup class properties.

4.  Use [**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey) or [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) to access the persistent registry storage for custom device setup class settings.

 

