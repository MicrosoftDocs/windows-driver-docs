---
title: DEVPKEY_Device_SafeRemovalRequired
description: The DEVPKEY_Device_SafeRemovalRequired device property represents a Boolean value that indicates whether a hot-plug device instance requires safe removal from the computer.
keywords: ["DEVPKEY_Device_SafeRemovalRequired Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequired
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_Device_SafeRemovalRequired

The DEVPKEY_Device_SafeRemovalRequired device property represents a Boolean value that indicates whether a hot-plug device instance requires safe removal from the computer.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_SafeRemovalRequired |
| Property-data-type identifier | [**DEVPROP_TYPE_BOOLEAN**](devprop-type-boolean.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | No |

  [**DEVPROP_TYPE_BOOLEAN**]: devprop-type-boolean.md

## Remarks

If this property for a hot-plug device instance has a value of DEVPROP_TRUE, the device instance requires safe removal from the computer. In this case, Windows displays the **Safely Remove Hardware** icon in the notification area on the right side of the taskbar. When the user clicks this icon, the system starts the **Safely Remove Hardware** program. By using this program, the user can instruct the system to prepare the device instance for removal before it can be surprise-removed from the computer.

**Note**   If the device instance is a removable media device, such as an optical disk drive, the device instance must have media inserted and must have the DEVPKEY_Device_SafeRemovalRequired property value of DEVPROP_TRUE. If both are true, the device instance is displayed in the **Safely Remove Hardware** program.

Windows Plug and Play (PnP) determines that the hot-plug device instance requires safe removal from the system if the following are true:

- The device instance is currently connected to the system.

- The device instance is either started or can be ejected automatically by the system.

- The CM_DEVCAP_SURPRISEREMOVALOK device capability bit for the device instance is not set. For more information about device capabilities, see [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya).

- The device instance does not have the [**DEVPKEY_Device_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md) device property set to DEVPROP_FALSE.

> [!NOTE]
> PnP unconditionally determines that the hot-plug device requires safe removal if the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE.

- The device instance is either directly removable from its parent device instance or has a removable ancestor in its device tree.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_SafeRemovalRequired.

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DEVPKEY_Device_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya)
