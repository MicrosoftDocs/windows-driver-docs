---
title: Format element
description: The optional Format element indicates a single file format and compression type supported by the scanner.
keywords: ["Format element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Format wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 09/27/2021
ms.localizationpriority: medium
---

# Format element

The optional **Format** element indicates a single file format and compression type supported by the scanner.

## Usage

```xml
<wscn:Format wscn:Override="" wscn:UsedDefault=""
  
      Override
      = "xs:string"
  
      UsedDefault
      = "xs:string">
  text
</wscn:Format wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute       | Type      | Required | Description                                                          |
|-----------------|-----------|----------|----------------------------------------------------------------------|
| **Override**    | xs:string | No       | Optional. A Boolean value that must be 0, **false**, 1, or **true**. |
| **UsedDefault** | xs:string | No       | Optional. A Boolean value that must be 0, **false**, 1, or **true**. |

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| dib | Windows Device Independent Bitmap. |
| exif | Exchangeable Image File Format Version 2.x. |
| jbig | ISO/IEC 11544:1993 Standard - Coded representation of picture and audio information; progressive bi-level image compression. |
| jfif | JPEG File Interchange Format 1.x. |
| jpeg2k | JPEG 2000 standard-based file format and compression. |
| pdf-a | PDF/A format (standard based on ISO/CD 19005-1). |
| png | Portable Networks Graphics (PNG) format. This format supports only the PNG compression type. |
| tiff-single-uncompressed | Single page TIFF file with no compression type. |
| tiff-single-g4 | Single page TIFF file with g4 compression type. |
| tiff-single-g3mh | Single page TIFF file with g3mh compression type. |
| tiff-single-jpeg-tn2 | Single page TIFF file with the JPEG compression type as described in Technical Note 2. |
| tiff-multi-uncompressed | Multiple page TIFF file with no compression type. |
| tiff-multi-g4 | Multiple page TIFF file with g4 compression type. |
| tiff-multi-g3mh | Multiple page TIFF file with g3mh compression type. |
| tiff-multi-jpeg-tn2 | Multiple page TIFF file with the JPEG compression type as described in Technical Note 2. |
| xps | XML Paper Specification |
| Any vendor-defined values |  |

## Child elements

There are no child elements.

## Parent elements

| Element                         |
|---------------------------------|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md)      |

## Remarks

If the image **Format** element is unsupported, then the scanner must reject the request and return the **ClientErrorDocumentFormatNotSupported** error code.

When the scanner sends out the **ClientErrorDocumentFormatNotSupported** error code because it doesn't support an image format, then the WSD scanner driver will try selecting other image formats in the following order, to find a format that the scanner supports.

1. PNG (W3C PNG) format is selected, if it's supported by the scanner.

1. EXIF format is selected, if it's supported by the scanner and the color mode matches RGB (24bpp) or grayscale (8pp).

1. G4 single-page TIFF (tiff-single-g4) format is selected, if it's supported by the scanner and color mode is monochrome (1bpp).

1. Uncompressed single-page TIFF (tiff-single-uncompressed) format is selected, if it's supported by the scanner.

Starting with Windows 7, WIA supports auto-configured scanning. And if auto-configured scanning with DIB format is requested, but the scanner doesn't support the DIB format, then the WSD scanner driver uses the same algorithm shown in the preceding steps to select an image format that the scanner supports.

> [!NOTE]
> Color mode is not selectable for auto-configured scan.

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Format**element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can both extend and create a subset of the allowed values for this element.

Although the WSD Scan Service supports the JBIG file format (ISO/IEC 11544:1993), it does not currently support JBIG2 (ISO/IEC 14492:2001).

## See also

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**FormatValue**](formatvalue.md)
