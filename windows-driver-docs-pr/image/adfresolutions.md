---
title: ADFResolutions element
description: The required ADFResolutions element contains a list of resolutions at which the front or back side of the scanner's automatic document feeder (ADF) can scan.
keywords: ["ADFResolutions element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFResolutions
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFResolutions element

The required **ADFResolutions** element contains a list of resolutions at which the front or back side of the scanner's automatic document feeder (ADF) can scan.

## Usage

```xml
<wscn:ADFResolutions>
  child elements
</wscn:ADFResolutions>
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

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both **Width** and **Height** are specified in pixels per inch.

If the parent element of the **ADFResolutions** element is [**ADFFront**](adffront.md), the specified resolution applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the resolution applies to the back side of the ADF.

The WSD Scan Service should list all possible widths that the scan device supports within the **Widths** child element and all possible heights that the scan device supports within the **Heights** child element. All **Width** and **Height** values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## See also

[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**Height**](height.md)

[**Heights**](heights.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)
