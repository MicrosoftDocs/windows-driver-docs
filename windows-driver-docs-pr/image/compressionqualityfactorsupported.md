---
title: CompressionQualityFactorSupported Element
description: The required CompressionQualityFactorSupported element specifies the range of compression quality factors that the scan device supports.
keywords: ["CompressionQualityFactorSupported element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn CompressionQualityFactorSupported
api_type:
- Schema
ms.date: 03/29/2023
---

# CompressionQualityFactorSupported element

The required **CompressionQualityFactorSupported** element specifies the range of compression quality factors that the scan device supports.

## Usage

```xml
<wscn:CompressionQualityFactorSupported>
  child elements
</wscn:CompressionQualityFactorSupported>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**MaxValue**](maxvalue.md) |
| [**MinValue**](minvalue.md) |

## Parent elements

| Element |
|--|
| [**DeviceSettings**](devicesettings.md) |

## Remarks

The compression quality factor is an integer value that you use for a lossy compression type to determine the amount of acceptable image loss during compression. The higher the requested fidelity, the larger the resulting file size will be.

[**MinValue**](minvalue.md)[**MaxValue**](maxvalue.md)

The minimum and maximum compression quality factors that the scan device supports are specified in the [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements, respectively. **MinValue** and **MaxValue** must be integers from 1 through 100. A value of 100 means that the device should use the least amount of compression that it supports to produce the highest quality image. Currently, JPEG compression is the only supported lossy compression type.

## See also

[**DeviceSettings**](devicesettings.md)

[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)
