---
title: AutoExposure Element
description: The required AutoExposure element specifies that the WSD Scan Service should automatically determine the exposure settings for the document.
keywords: ["AutoExposure element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn AutoExposure
api_type:
- Schema
ms.date: 03/27/2023
---

# AutoExposure element

The required **AutoExposure** element specifies that the WSD Scan Service should automatically determine the exposure settings for the document.

## Usage

```xml
<wscn:AutoExposure>
  text
</wscn:AutoExposure>
```

## Attributes

There are no attributes.

## Text value

Required. A Boolean value that must be 0, false, 1, or true.**falsetrue**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**Exposure**](exposure.md) |

## Remarks

When the Boolean value of the **AutoExposure** element is 1 or **true**, the scan device will employ image processing techniques to reduce the background of the document to white.

When the value is 0 or **false**, the device should use the default settings for each of the exposure settings.

## See also

[**Exposure**](exposure.md)
