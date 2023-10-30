---
title: ADFBack element
description: The optional ADFBack element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.
keywords: ["ADFBack element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFBack
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFBack element

The optional **ADFBack** element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.

## Usage

```xml
<wscn:ADFBack>
  child elements
</wscn:ADFBack>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ADFColor**](adfcolor.md) |
| [**ADFMaximumSize**](adfmaximumsize.md) |
| [**ADFMinimumSize**](adfminimumsize.md) |
| [**ADFOpticalResolution**](adfopticalresolution.md) |
| [**ADFResolutions**](adfresolutions.md) |

## Parent elements

| Element |
|--|
| [**ADF**](adf.md) |

## Remarks

The WSD Scan Service should specify the **ADFBack** elements and its children only if the scanner's ADF supports duplexing.

## See also

[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)
