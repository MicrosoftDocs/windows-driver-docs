---
title: RotationsSupported Element
description: The required RotationsSupported element contains the list of rotation values that the scanner supports for rotating each image of a scanned document.
keywords: ["RotationsSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn RotationsSupported
api_type:
- Schema
ms.date: 05/01/2023
---

# RotationsSupported element

The required **RotationsSupported** element contains the list of rotation values that the scanner supports for rotating each image of a scanned document.

## Usage

```xml
<wscn:RotationsSupported>
  child elements
</wscn:RotationsSupported>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**RotationValue**](rotationvalue.md) |

## Parent elements

| Element |
|--|
| [**DeviceSettings**](devicesettings.md) |

## Remarks

The WSD Scan Service must apply all rotation values to the scan data after data acquisition. All rotations must be applied in the clockwise direction.

## See also

[**DeviceSettings**](devicesettings.md)

[**RotationValue**](rotationvalue.md)
