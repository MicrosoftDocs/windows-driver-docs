---
title: ColorEntry Element
description: The required ColorEntry element describes a single color-processing mode that an input source on the scanner supports.
keywords: ["ColorEntry element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ColorEntry
api_type:
- Schema
ms.date: 03/29/2023
---

# ColorEntry element

The required **ColorEntry** element describes a single color-processing mode that an input source on the scanner supports.

## Usage

```xml
<wscn:ColorEntry>
  text
</wscn:ColorEntry>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following keywords:

| Term | Description |
|--|--|
| BlackAndWhite1 | Black and white images; 1 bit per pixel (bpp) and a single channel |
| Grayscale4 | Grayscale images; 4 bpp and a single channel |
| Grayscale8 | Grayscale images; 8 bpp and a single channel |
| Grayscale16 | Grayscale images; 16 bpp and a single channel |
| RGB24 | RGB-encoded color images; 24 bpp divided between three channels of 8 bits each |
| RGB48 | RGB-encoded color images; 48 bpp divided between three channels of 16 bits each |
| RGBa32 | RGB-encoded color images with an alpha channel; 32 bits bpp divided between four channels of 8 bits each |
| RGBa64 | RGB-encoded color images with an alpha channel; 64 bpp divided between four channels of 16 bits each |

## Child elements

There are no child elements.

## Parent elements

[**ADFColor**](adfcolor.md)

[**FilmColor**](filmcolor.md)

[**PlatenColor**](platencolor.md)

## Remarks

Each value keyword describes the color data type and encoding, bit depth, and bits per channel. The following table shows how the value keywords map to the scanner's color processing properties.

| Keyword | Pixel bit depth | Bits per channel |
|--|--|--|
| BlackAndWhite1 | 1 | 1 |
| Grayscale4 | 4 | {4} |
| Grayscale8 | 8 | {8} |
| Grayscale16 | 16 | {16} |
| RGB24 | 24 | {8,8,8} |
| RGB48 | 48 | {16,16,16} |
| RGBa32 | 32 | {8,8,8,8} |
| RGBa64 | 64 | {16,16,16,16} |

You can both extend and subset the allowed values for this element.
