---
title: DEVPKEY_Device_PhysicalDeviceLocation
description: The DEVPKEY_Device_PhysicalDeviceLocation device property encapsulates the physical device location information provided by a device's firmware to Windows.
keywords: ["DEVPKEY_Device_PhysicalDeviceLocation Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_PhysicalDeviceLocation
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_Device_PhysicalDeviceLocation

The DEVPKEY_Device_PhysicalDeviceLocation device property encapsulates the physical device location information provided by a device's firmware to Windows.

| Attribute | Value |
|--|--|
| **Property key | DEVPKEY_Device_PhysicalDeviceLocation |
| **Property-data-type identifier | [**DEVPROP_TYPE_BINARY**](devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Corresponding SPDRP_Xxx identifier | SPDRP_PHYSICAL_DEVICE_LOCATION |
| Localized? | No |

## Remarks

Windows sets the value of DEVPKEY_Device_PhysicalDeviceLocation with the physical device location information. The format of the information is defined in the ACPI 4.0a Specification, section 6.1.6.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_PhysicalDeviceLocation.

## Requirements

**Version**: Windows 8 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
