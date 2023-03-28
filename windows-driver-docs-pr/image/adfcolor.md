---
title: ADFColor element
description: The required ADFColor element contains the list of color processing capabilities that the front or back side of the automatic document feeder (ADF) supports.
keywords: ["ADFColor element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFColor
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFColor element

The required **ADFColor** element contains the list of color processing capabilities that the front or back side of the automatic document feeder (ADF) supports.

## Usage

```xml
<wscn:ADFColor>
  child elements
</wscn:ADFColor>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ColorEntry**](colorentry.md) |

## Parent elements

| Element |
|--|
| [**ADFBack**](adfback.md) |
| [**ADFFront**](adffront.md) |

## Remarks

The **ADFColor** element contains the information needed to determine the type of color processing and acquisition that the scanner's ADF supports. If the parent element is [**ADFFront**](adffront.md), the specified color information applies to the front side of the ADF; otherwise, the parent element is [**ADFBack**](adfback.md) and the color information applies to the back side of the ADF.

The amount of information that is needed to describe each pixel depends on the specific [**ColorEntry**](colorentry.md) keyword. Black and white images require only one bit per pixel (bpp), whereas grayscale and color images require significantly more information. The exact amount of information is determined by the color space and technical capabilities of the scan device.

Another important aspect of the returned scan data is the photometric interpretation of the acquired data. All image data that the scan device returns is required to be black on white, where black is represented by 0 and white is represented by 1.

## See also

[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ColorEntry**](colorentry.md)
