---
title: Enumerating Installed Device Setup Classes
description: Provides information about enumerating installed device setup classes.
keywords:
- enumerating installed device setup classes WDK
- installed device setup classes WDK
- installed device setup classes WDK , enumerating
- device setup classes WDK device installations , enumerating
ms.date: 08/15/2022
---

# Enumerating installed device setup classes

To discover the [device setup classes](./overview-of-device-setup-classes.md) that are installed in a system, do not enumerate the device setup classes by directly accessing registry keys. As with any registry key, the location and format of these keys might change between different versions of Windows.

To safely discover the installed device setup classes, and to query and modify the properties of a setup class, follow these steps:

Using [configuration manager](/windows/win32/api/cfgmgr32/) functions:

1. Use [**CM_Enumerate_Classes**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_enumerate_classes) with a *ulFlags* of *CM_ENUMERATE_CLASSES_INSTALLER* to enumerate through the list of device setup classes that are currently installed on the system.

1. Use [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) with a *ulFlags* of *CM_CLASS_PROPERTY_INSTALLER* to retrieve the [**DEVPKEY_NAME**](devpkey-name--device-setup-class-.md) property to get the description of an installed setup class.

1. Use [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) with a *ulFlags* of *CM_CLASS_PROPERTY_INSTALLER* to query other setup class properties and use [**CM_Set_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw) with a *ulFlags* of *CM_CLASS_PROPERTY_INSTALLER* to set setup class properties.

1. Use [**CM_Open_Class_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_class_keyw) with a *ulFlags* of *CM_OPEN_CLASS_KEY_INSTALLER* to access the persistent registry storage for custom device setup class settings.

Using [SetupApi](setupapi.md) functions:

1. Use [**SetupDiBuildClassInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolist) to retrieve the set of device setup classes that are currently installed on the system.

1. Use [**SetupDiGetClassDescription**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptiona) to retrieve the description of an installed setup class.

1. Use [**SetupDiGetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertya) to query the setup class properties and [**SetupDiSetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya) to set the setup class properties.

1. Use [**SetupDiOpenClassRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey) or [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) with a *Flags* of *DIOCR_INSTALLER* to access the persistent registry storage for custom device setup class settings.
