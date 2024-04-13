---
title: PlatenResolutions Element
description: The required PlatenResolutions element contains a list of resolutions at which the scanner's platen can scan.
keywords: ["PlatenResolutions element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn PlatenResolutions
api_type:
- Schema
ms.date: 05/01/2023
---

# PlatenResolutions element

The required **PlatenResolutions** element contains a list of resolutions at which the scanner's platen can scan.

## Usage

```xml
<wscn:PlatenResolutions>
  child elements
</wscn:PlatenResolutions>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**Heights**](heights.md) |
| [**Widths**](widths.md) |

## Parent elements

| Element |
|--|
| [**Platen**](platen.md) |

## Remarks

The resolution is specified as a [**Width**](width.md) x [**Height**](height.md) pair, where both Width and Height are specified in pixels per inch.

The WSD Scan Service should list all possible widths that the scan device supports within the Widths child element and all possible heights that the scan device supports within the Heights child element. All Width and Height values are independent of each other, and most devices will support them being paired in any combination within a [**ScanTicket**](scanticket.md) element.

## See also

[**Height**](height.md)

[**Heights**](heights.md)

[**Platen**](platen.md)

[**ScanTicket**](scanticket.md)

[**Width**](width.md)

[**Widths**](widths.md)
