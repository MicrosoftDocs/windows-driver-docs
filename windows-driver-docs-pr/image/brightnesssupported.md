---
title: BrightnessSupported Element
description: The required BrightnessSupported element specifies whether the scan device supports user control of the scan brightness setting.
keywords: ["BrightnessSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn BrightnessSupported
api_type:
- Schema
ms.date: 03/27/2023
---

# BrightnessSupported element

The required **BrightnessSupported** element specifies whether the scan device supports user control of the scan brightness setting.

## Usage

```xml
<wscn:BrightnessSupported>
  text
</wscn:BrightnessSupported>
```

## Attributes

There are no attributes.

## Text value

Required. A Boolean value that must be 0, 1, false, or true.**falsetrue**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DeviceSettings**](devicesettings.md) |

## Remarks

If the scan device allows user control of the scan brightness setting, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also

[**DeviceSettings**](devicesettings.md)
