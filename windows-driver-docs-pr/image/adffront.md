---
title: ADFFront Element
description: The required ADFFront element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.
keywords: ["ADFFront element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFFront
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFFront element

The required **ADFFront** element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.

## Usage

```xml
<wscn:ADFFront>
  child elements
</wscn:ADFFront>
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

If the scanner has an ADF the WSD Scan Service must provide details for it in the **ADFFront** element, regardless of the ADF's duplexing capabilities.

## See also

[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)
