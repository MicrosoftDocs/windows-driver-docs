---
title: DEVPKEY_Device_Parent
description: DEVPKEY_Device_Parent
keywords: ["DEVPKEY_Device_Parent Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Parent
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 04/17/2025
ms.topic: reference
---

# DEVPKEY_Device_Parent

The **DEVPKEY_Device_Parent** device property represents the [device instance identifier](device-instance-ids.md) of the parent for a device instance.

| Attribute | Value |
|--|--|
| **Property key** | DEVPKEY_Device_Parent |
| **Property-data-type identifier** | [**DEVPROP_TYPE_STRING**](devprop-type-string.md) |
| **Property access** | Read-only access by installation applications and installers |
| **Localized?** | Not applicable |

## Remarks

You can call **[CM_Get_DevNode_Property](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw)** or **[SetupDiGetDeviceProperty](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)** to retrieve the value of **DEVPKEY_Device_Parent** property.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support this property. For information about how to retrieve device relations properties on these earlier versions of Windows, see [Retrieving Device Relations](./retrieving-device-relations.md).

For a *present* device, the **DEVPKEY_Device_Parent** property will provide you the device instance ID of the parent of that device.  For a *non-present* device:

- On Windows 8 and later:
  - If the parent of the *non-present* device from the last time the *non-present* device was a *present* device still exists as a device on the system (*present* or *non-present* device), **DEVPKEY_Device_Parent** will provide the device instance ID of that parent device.
  - If the parent of the *non-present* device from the last time the *non-present* device was a *present* device does not still exist as a device on the system, **DEVPKEY_Device_Parent** will return the device instance ID of the device that is at the root of the device tree.
- Prior to Windows 8:
  - Retrieving **DEVPKEY_Device_Parent** will return an error that the property is not found.

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also

- **[SetupDiGetDeviceProperty](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)**
