---
title: DEVPKEY_NAME (Device Instance)
description: The DEVPKEY_NAME device property represents the name of a device instance.
keywords: ["DEVPKEY_NAME (Device Instance) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Instance)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_NAME (Device Instance)

The DEVPKEY_NAME device property represents the name of a device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_NAME |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | Yes |

## Remarks

The value of DEVPKEY_NAME device should be used to identify a device instance to an end-user in a user interface item.

The retrieved property value is the same as the value of the [**DEVPKEY_Device_FriendlyName**](devpkey-device-friendlyname.md) device property, if **DEVPKEY_Device_FriendlyName** is set. Otherwise, the value of DEVPKEY_NAME is same as the value of the [**DEVPKEY_Device_DeviceDesc**](devpkey-device-devicedesc.md) device property.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_NAME property.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support properties that correspond to DEVPKEY_Device_FriendlyName and DEVPKEY_Device_DeviceDesc.

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DEVPKEY_Device_DeviceDesc**](devpkey-device-devicedesc.md)

[**DEVPKEY_Device_FriendlyName**](devpkey-device-friendlyname.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
