---
title: DocumentSizeAutoDetectSupported Element
description: The required DocumentSizeAutoDetectSupported element indicates whether the scan device can detect the size of the original media.
keywords: ["DocumentSizeAutoDetectSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DocumentSizeAutoDetectSupported
api_type:
- Schema
ms.date: 04/24/2023
---

# DocumentSizeAutoDetectSupported element

The required **DocumentSizeAutoDetectSupported** element indicates whether the scan device can detect the size of the original media.

## Usage

```xml
<wscn:DocumentSizeAutoDetectSupported>
  text
</wscn:DocumentSizeAutoDetectSupported>
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

If the scan device can detect the size of the original media, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also

[**DeviceSettings**](devicesettings.md)
