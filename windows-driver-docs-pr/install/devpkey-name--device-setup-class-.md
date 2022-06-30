---
title: DEVPKEY_NAME (Device Setup Class)
description: The DEVPKEY_NAME device property represents the name of a device setup class.
keywords: ["DEVPKEY_NAME (Device Setup Class) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Setup Class)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
---

# DEVPKEY_NAME (Device Setup Class)

The DEVPKEY_NAME device property represents the name of a [device setup class](./overview-of-device-setup-classes.md).

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_NAME |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

You can use the value of DEVPKEY_NAME to identify a device setup class to an end-user in a user interface item.

If DEVPKEY_DeviceClass_Name is set, the value of DEVPKEY_NAME is the same as the value of the [**DEVPKEY_DeviceClass_Name**](devpkey-deviceclass-name.md) device property. Otherwise, the DEVPKEY_NAME value is the same as the value of the [**DEVPKEY_DeviceClass_ClassName**](devpkey-deviceclass-classname.md) device property.

You can call [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) or [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) to retrieve the value of DEVPKEY_NAME for a device setup class.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support properties that correspond to DEVPKEY_DeviceClass_Name and DEVPKEY_DeviceClass_ClassName.

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DEVPKEY_DeviceClass_ClassName**](devpkey-deviceclass-classname.md)

[**DEVPKEY_DeviceClass_Name**](devpkey-deviceclass-name.md)

[**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)

[**SetupDiGetClassDescription**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptiona)

[**SetupDiClassNameFromGuid**](/windows/win32/api/setupapi/nf-setupapi-setupdiclassnamefromguida)
