---
title: WIA_IPA_FORMAT
description: The WIA_IPA_FORMAT property contains the current format of the image that is about to be transferred. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_FORMAT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_FORMAT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/11/2023
---

# WIA_IPA_FORMAT

The WIA_IPA_FORMAT property contains the current format of the image that is about to be transferred. The WIA minidriver creates and maintains this property.

Property Type: VT_CLSID

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

If you can set the device to only a single value, create a WIA_PROP_LIST type, and place the valid value in it.

For Windows 8 and later versions of Windows, the following values have been added for the WIA_IPA_FORMAT property:

- WiaImgFmt_CSV

- WiaImgFmt_JBIG2

- WiaImgFmt_RawBar

- WiaImgFmt_RawMic

- WiaImgFmt_RawPat

- WiaImgFmt_XmlBar

- WiaImgFmt_XmlMic

- WiaImgFmt_XmlPat

For both the WiaImgFmt_PDFA and WiaImgFmt_XPS formats, the drivers should support any [**WIA_IPA_COMPRESSION**](wia-ipa-compression.md) value. For these two formats, the default WIA_IPA_COMPRESSION value, WIA_COMPRESSION_NONE, means "not defined." The scanner (or the driver, where the PDF/A or XPS file is generated) must choose the internal compression mode that is used for image data.

The following table describes the constants that are valid with WIA_IPA_FORMAT.

| Format | Description |
|--|--|
| WiaAudFmt_AIFF | AIFF audio format |
| WiaAudFmt_MP3 | MP3 audio format |
| WiaAudFmt_WAV | WAV audio format |
| WiaAudFmt_WMA | WMA audio format |
| WiaImgFmt_ASF | ASF video format |
| WiaImgFmt_AVI | AVI video format |
| WiaImgFmt_BMP | Windows Device Independent Bitmap (DIB) file |
| WiaImgFmt_CIFF | Camera Image File format |
| WiaImgFmt_CSV | Comma separated file |
| WiaImgFmt_DPOF | DPOF printing format |
| WiaImgFmt_EMF | Extended Windows metafile |
| WiaImgFmt_EXEC | Executable file |
| WiaImgFmt_EXIF | Exchangeable File Format |
| WiaImgFmt_FLASHPIX | FlashPix format |
| WiaImgFmt_GIF | GIF image format |
| WiaImgFmt_HTML | HTML format |
| WiaImgFmt_ICO | Windows icon file format |
| WiaImgFmt_JBIG | Joint Bi-level Image experts Group format |
| WiaImgFmt_JBIG2 | Joint Bi-level Image experts Group format (version 2) |
| WiaImgFmt_JPEG | JPEG compressed format |
| WiaImgFmt_JPEG2K | JPEG 2000 compressed format |
| WiaImgFmt_JPEG2KX | JPEG 2000 compressed format |
| WiaImgFmt_MEMORYBMP | Windows bitmap without a header file |
| WiaImgFmt_MPG | MPEG video format |
| WiaImgFmt_PHOTOCD | Eastman Kodak file format |
| WiaImgFmt_PDFA | PDF/A (ISO/CD 19005-1) format |
| WiaImgFmt_PICT | Apple file format |
| WiaImgFmt_PNG | W3C PNG format |
| WiaImgFmt_RAW | WIA Raw image file format for data transfers only |
| WiaImgFmt_RawBar | WIA Barcode Metadata Raw Format |
| WiaImgFmt_RawMic | WIA MICR Metadata Raw Format |
| WiaImgFmt_RawPat | WIA Patch Code Metadata Raw Format |
| WiaImgFmt_RAWRGB | Raw RGB format |
| WiaImgFmt_RTF | Rich Text File format |
| WiaImgFmt_SCRIPT | Script file |
| WiaImgFmt_TIFF | Tagged Image File Format (TIFF) |
| WiaImgFmt_TXT | Text file |
| WiaImgFmt_UNICODE16 | Unicode 16-bit encoding |
| WiaImgFmt_WMF | Windows metafile |
| WiaImgFmt_XML | XML file |
| WiaImgFmt_XmlBar | XML file whose content is compliant with the WIA Barcode Metadata Schema |
| WiaImgFmt_XmlMic | XML file whose content is compliant with the WIA MICR Metadata Schema |
| WiaImgFmt_XmlPat | XML file whose content is compliant with the WIA Patch Code Metadata Schema |
| WiaImgFmt_XPS | XPS document file |

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is WiaImgFmt_BMP.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_COMPRESSION**](wia-ipa-compression.md)

[**WIA_IPA_FULL_ITEM_NAME**](wia-ipa-full-item-name.md)
