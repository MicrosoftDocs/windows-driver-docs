---
title: ADFMinimumSize Element
description: The required ADFMinimumSize element specifies the smallest size original that an end user can scan on the front or back of the automatic document feeder (ADF).
keywords: ["ADFMinimumSize element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFMinimumSize
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFMinimumSize element

The required **ADFMinimumSize** element specifies the smallest size original that an end user can scan on the front or back of the automatic document feeder (ADF).

## Usage

```xml
<wscn:ADFMinimumSize>
  child elements
</wscn:ADFMinimumSize>
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

The [**Width**](width.md) child element specifies the minimum size of media that the ADF supports in the fast scan direction. The [**Height**](height.md) child element specifies the minimum size of media that the ADF supports in the slow scan direction.

If the parent element of the **ADFMinimumSize** element is [**ADFFront**](adffront.md), the specified size applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the size applies to the back side of the ADF.

All media dimensions are measured in one thousandths (1/1000) of an inch. The possible values for both **Width** and **Height** range from 1 through 2147483648.

## See also

[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Width**](width.md)
