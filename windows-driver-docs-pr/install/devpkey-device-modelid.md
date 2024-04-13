---
title: DEVPKEY_Device_ModelId
description: The DEVPKEY_Device_ModelId device property matches a device to a device metadata package.
keywords: ["DEVPKEY_Device_ModelId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ModelId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_Device_ModelId

The DEVPKEY_Device_ModelId device property matches a device to a [device metadata package](./overview-of-device-metadata-packages.md).

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_ModelId |
| Property-data-type identifier | [**DEVPROP_TYPE_GUID**](./devprop-type-guid.md) |
| Property access | Read and write access by installation applications and installers |
| Localized? | No |

## Remarks

The DEVPKEY_Device_ModelId device property provides support for IHVs and OEMs to uniquely identify devices that share the same manufacturer and model. By using a model identifier (ModelID), OEMs and IHVs can match the device model that they distribute to their own branded device metadata package.

The DEVPKEY_Device_ModelId device property contains the value of the [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)) XML element from the device's metadata package. When the device is installed, this PKEY is populated with the ModelID GUID value as reported by the device.

For more information, see [Device Metadata Packages](./overview-of-device-metadata-packages.md).

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[Device Metadata Packages](./overview-of-device-metadata-packages.md)

[**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85))

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
