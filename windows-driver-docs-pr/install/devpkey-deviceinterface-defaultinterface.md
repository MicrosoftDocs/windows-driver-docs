---
title: DEVPKEY_DeviceInterfaceClass_DefaultInterface
description: The DEVPKEY_DeviceInterfaceClass_DefaultInterface property represents the symbolic link name of the default device interface for a device interface class.
keywords: ["DEVPKEY_DeviceInterfaceClass_DefaultInterface Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterfaceClass_DefaultInterface
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 09/16/2022
---

# DEVPKEY_DeviceInterfaceClass_DefaultInterface

The DEVPKEY_DeviceInterfaceClass_DefaultInterface property represents the symbolic link name of the default device interface for a device interface class.

| Attribute | Value |
|--|--|
| **Property key** | DEVPKEY_DeviceInterfaceClass_DefaultInterface |
| **Property-data-type identifier** | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| **Property access** | Read and write access by installation applications and installers |
| **Localized?** | No |

## Remarks

For information about how to install and use device interface classes, see [Device interface classes](./overview-of-device-interface-classes.md).

You can retrieve the value of DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) with a *ulFlags* of CM_CLASS_PROPERTY_INTERFACE or [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) with a *Flags* of DICLASSPROP_INTERFACE. You can set DEVPKEY_DeviceInterfaceClass_DefaultInterface by calling [**CM_Set_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw) with a *ulFlags* of CM_CLASS_PROPERTY_INTERFACE or [**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw) with a *Flags* of DICLASSPROP_INTERFACEDICLASSPROP_INTERFACE.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterfaceClass_DefaultInterface property key. For information about how to access the default interface of a device interface class on these earlier versions of Windows, see [Accessing device interface class properties](./accessing-device-interface-class-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows  
**Header**: Devpkey.h (include Devpkey.h)

## See also

[**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw)

[**CM_Set_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw)

[**SetupDiSetDeviceInterfaceDefault**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacedefault)
