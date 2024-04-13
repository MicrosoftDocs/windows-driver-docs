---
title: ADFOpticalResolution Element
description: The required ADFOpticalResolution element specifies the maximum optical resolution at which the front or back side of the automatic document feeder (ADF) can scan.
keywords: ["ADFOpticalResolution element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFOpticalResolution
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFOpticalResolution element

The required **ADFOpticalResolution** element specifies the maximum optical resolution at which the front or back side of the automatic document feeder (ADF) can scan.

## Usage

```xml
<wscn:ADFOpticalResolution>
  child elements
</wscn:ADFOpticalResolution>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Height**](height.md) |
| [**Width**](width.md) |

## Parent elements

| Element |
|--|
| [**ADFBack**](adfback.md) |
| [**ADFFront**](adffront.md) |

## Remarks

Resolution is specified as a [**Width**](width.md) × [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the parent element of the **ADFOpticalResolution** element is [**ADFFront**](adffront.md), the specified optical resolution applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the optical resolution applies to the back side of the ADF.

## See also

[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)
