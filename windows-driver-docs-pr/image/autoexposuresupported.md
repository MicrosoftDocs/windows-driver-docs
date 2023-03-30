---
title: AutoExposureSupported element
description: The required AutoExposureSupported element specifies whether the scan device supports automatic adjustment of the various exposure settings.
keywords: ["AutoExposureSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn AutoExposureSupported
api_type:
- Schema
ms.date: 03/27/2023
---

# AutoExposureSupported element

The required **AutoExposureSupported** element specifies whether the scan device supports automatic adjustment of the various exposure settings.

## Usage

```xml
<wscn:AutoExposureSupported>
  text
</wscn:AutoExposureSupported>
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

[**Exposure**](exposure.md)

If the scan device supports automatic adjustment of various [**Exposure**](exposure.md) settings, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also

[**DeviceSettings**](devicesettings.md)

[**Exposure**](exposure.md)
