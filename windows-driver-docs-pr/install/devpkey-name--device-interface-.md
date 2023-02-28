---
title: DEVPKEY_NAME (Device Interface)
description: The DEVPKEY_NAME device interface property represents the name of a device interface.
keywords: ["DEVPKEY_NAME (Device Interface) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Interface)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_NAME (Device Interface)

The DEVPKEY_NAME device interface property represents the name of a device interface.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_NAME |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers. |
| Localized? | Yes |

## Remarks

The value of the DEVPKEY_NAME should be used to identify an interface to an end-user in a user interface item.

The value of DEVPKEY_NAME is the same as the value of the [**DEVPKEY_DeviceInterface_FriendlyName**](devpkey-deviceinterface-friendlyname.md) device property, if DEVPKEY_DeviceInterface_FriendlyName is set. Otherwise, DEVPKEY_NAME does not exist.

You can retrieve the value of DEVPKEY_NAME by calling [**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) or [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw).

For information about device interfaces, see [Device Interface Classes](./overview-of-device-interface-classes.md) and the [**INF AddInterface Directive**](./inf-addinterface-directive.md).

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support a property that corresponds to DEVPKEY_DeviceInterface_FriendlyName.

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DEVPKEY_DeviceInterface_FriendlyName**](devpkey-deviceinterface-friendlyname.md)

[**INF AddInterface Directive**](./inf-addinterface-directive.md)

[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)
