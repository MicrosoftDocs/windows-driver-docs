---
title: DEVPKEY_Device_FirstInstallDate
description: The DEVPKEY_Device_FirstInstallDate device property specifies the time stamp when the device instance was first installed in the system.
keywords: ["DEVPKEY_Device_FirstInstallDate Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_FirstInstallDate
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
ms.topic: reference
---

# DEVPKEY_Device_FirstInstallDate

The DEVPKEY_Device_FirstInstallDate device property specifies the time stamp when the device instance was first installed in the system.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_FirstInstallDate |
| Property-data-type identifier | [**DEVPROP_TYPE_FILETIME**](devprop-type-filetime.md) |
| Property access | Read-only access by installation applications and installers. |
| Localized? | No |

## Remarks

Windows sets the value of DEVPKEY_Device_FirstInstallDate with the time stamp that specifies when the device instance was first installed in the system.

**Note**   Unlike the [**DEVPKEY_Device_InstallDate**](devpkey-device-installdate.md) property, the value of the DEVPKEY_Device_FirstInstallDate property does not change with each successive update of the device driver. For example, a driver that was updated through Windows Update does not change the value of this property,

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_FirstInstallDate property.

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
