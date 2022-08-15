---
title: DEVPKEY_DeviceInterface_Restricted
description: The DEVPKEY_DeviceInterface_Restricted device interface property indicates that the device interface on which it is present and set to TRUE, should be treated with privileged access by system components that honor the setting.
keywords: ["DEVPKEY_DeviceInterface_Restricted Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterface_Restricted
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
---

# DEVPKEY_DeviceInterface_Restricted

The DEVPKEY_DeviceInterface_Restricted device interface property indicates that the device interface on which it is present and set to TRUE, should be treated with privileged access by system components that honor the setting.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DeviceInterface_Restricted |
| Property-data-type identifier | [**DEVPROP_TYPE_BOOLEAN**](devprop-type-boolean.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | No |

## Remarks

You can call [**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) or [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) to retrieve the value of DEVPKEY_DeviceInterface_Restricted.

## Requirements

**Version**: Windows 8 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)
