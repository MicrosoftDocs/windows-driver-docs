---
title: DEVPKEY_DeviceDisplay_Category
description: The DEVPKEY_DeviceDisplay_Category device property represents one or more functional categories that apply to a device instance.
keywords: ["DEVPKEY_DeviceDisplay_Category Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceDisplay_Category
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
ms.topic: reference
---

# DEVPKEY_DeviceDisplay_Category

The DEVPKEY_DeviceDisplay_Category device property represents one or more functional categories that apply to a device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_DeviceDisplay_Category |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING_LIST**](./devprop-type-string-list.md) |
| Property access | Read-only access by installation applications and installers. |
| Localized? | No |

## Remarks

Device categories for a physical device are specified through the [**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85)) XML element in a [device metadata package](./overview-of-device-metadata-packages.md). Each instance of that device in a system inherits the device categories for that physical device.

Each physical device can have one or more functional categories specified in the [device metadata package](./overview-of-device-metadata-packages.md). Each category is used by Windows Devices and Printers to group the device instance into one of the recognized device categories.

Multifunction devices would typically identify multiple functional categories for each hardware function that the device supports. For example, a multifunction device could identify functional categories for printer, fax, scanner, and removable storage device functionality.

The first functional category string in the [**DEVPROP_TYPE_STRING_LIST**](devprop-type-string-list.md) specifies the physical device's primary functional category. The primary functional category is defined by the independent hardware vendor (IHV) to specify how the device is advertised, packaged, sold, and ultimately identified by users.

If the DEVPKEY_DeviceDisplay_Category device property specifies more than one functional category string, the remaining strings that follow the first string specifies the physical device's secondary functional categories.

The **Devices and Printers** user interface in Control Panel displays the primary and secondary functional categories of the device instance. These categories are displayed in the order that is specified in the DEVPKEY_DeviceDisplay_Category device property.

You can access the DEVPKEY_DeviceDisplay_Category property by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw).

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85))

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
