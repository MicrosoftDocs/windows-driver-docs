---
title: ContrastSupported Element
description: The required ContrastSupported element specifies whether the scan device supports user control of the scan contrast setting.
keywords: ["ContrastSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ContrastSupported
api_type:
- Schema
ms.date: 03/29/2023
---

# ContrastSupported element

The required **ContrastSupported** element specifies whether the scan device supports user control of the scan contrast setting.

## Usage

```xml
<wscn:ContrastSupported>
  text
</wscn:ContrastSupported>
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

If the scan device allows user control of the scan contrast setting, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also

[**DeviceSettings**](devicesettings.md)
