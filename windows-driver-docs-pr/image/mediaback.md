---
title: MediaBack Element
description: The optional MediaBack element contains all parameters that are specific to the scanning of the back side of the physical media.
keywords: ["MediaBack element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn MediaBack
api_type:
- Schema
ms.date: 05/01/2023
---

# MediaBack element

The optional **MediaBack** element contains all parameters that are specific to the scanning of the back side of the physical media.

## Usage

```xml
<wscn:MediaBack>
  child elements
</wscn:MediaBack>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ColorProcessing**](colorprocessing.md) |
| [**Resolution**](resolution.md) |
| [**ScanRegion**](scanregion.md) |

## Parent elements

| Element |
|--|
| [**MediaSides**](mediasides.md) |

## Remarks

The **MediaBack** element is valid only when the scanner supports duplex scanning and the current input source, which is defined in the [**InputSource**](inputsource.md) element, is **ADFDuplex**.

If the **MediaBack** element does not contain a [**ScanRegion**](scanregion.md) element, the WSD Scan Service should use 0 as the offsets and the width and height of the [**InputMediaSize**](inputmediasize.md), if given. If **ScanRegion** is missing and **InputMediaSize** is not specified or cannot be determined by the scan device, you can determine the implementation.

If the input source is **ADFDuplex** and the **MediaBack** element is missing, all parameters that are specified in [**MediaFront**](mediafront.md) will apply to the back side scanning as well.

## See also

[**ColorProcessing**](colorprocessing.md)

[**InputMediaSize**](inputmediasize.md)

[**InputSource**](inputsource.md)

[**MediaFront**](mediafront.md)

[**MediaSides**](mediasides.md)

[**Resolution**](resolution.md)

[**ScanRegion**](scanregion.md)
