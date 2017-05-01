---
title: WIA RAW Data Header
author: windows-driver-content
description: WIA RAW Data Header
ms.assetid: a2cb3835-7879-4f69-9784-9487df40730a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA RAW Data Header


The header for RAW data is as follows:

```
DWORD Tag;         // must contain &#39;WRAW&#39; (single byte ASCII characters)
DWORD Version;        // must contain 0x00010000
DWORD HeaderSize;       // contains amount of valid bytes in header
DWORD XRes;              // X (horizontal) resolution, in DPI
DWORD YRes;              // Y (vertical) resolution, in DPI
DWORD XExtent;           // image width, in pixels
DWORD YExtent;           // image height, in pixels
DWORD BytesPerLine;      // used only for uncompressed image data, 0 (unknown) for compressed data 
DWORD BitsPerPixel;      // number of bits per pixel (all channels)
DWORD ChannelsPerPixel;  // number of color channels (samples) within a pixel
DWORD DataType;    // current WIA_IPA_DATATYPE value describing the image
BYTE  BitsPerChannel[8]; // up to 8 channels per pixel, use as many as needed  
DWORD Compression;       // current WIA_IPA_COMPRESSION value
DWORD PhotometricInterp; // current WIA_IPS_PHOTOMETRIC_INTERP value
DWORD LineOrder;         // image line order as a WIA_LINE_ORDER value
DWORD RawDataOffset;     // offset position (in bytes, starting from 0) for the raw image data
DWORD RawDataSize;       // size of raw image data, in bytes
DWORD PaletteOffset;     // offset position (in bytes, starting from 0) for the palette (0 if none)
DWORD PaletteSize;       // size, in bytes, of color palette table (0 if no palette is required) 
```

### Additional Header Field Descriptions

<a href="" id="dword-compression"></a>DWORD *Compression*  
Allows compressed raw formats, such as Nikon's compressed NEF and headerless compressed data used for compressed fax transmissions (Group 3.1, 3.2d, 4). Values for this field would be WIA\_IPA\_COMPRESSION constants, possibly vendor-specific for specialized applications. Default value is WIA\_COMPRESSION\_NONE.

Compression Examples:

G4 compressed data (WIA\_COMPRESSION\_G4) could be transferred either within a TIFF file (WiaImgFmt\_TIFF) or using the raw format (WiaImgFmt\_RAW).

JPEG compressed data (WIA\_COMPRESSION\_JPEG) could be transferred either using the JFIF format (WiaImgFmt\_JPEG), the EEXIF format (WiaImgFmt\_EXIF), or the TIFF format (WiaImgFmt\_TIFF). It is not possible to transfer JPEG data formatted in one of the Interchange Formats (JFIF, EEXIF) within transfers using the raw format (WiaImgFmt\_RAW) - instead, it is necessary to use one of the other JPEG-compatible formats.

For more information on the WIA compression constants, see the [**WIA\_IPA\_COMPRESSION**](https://msdn.microsoft.com/library/windows/hardware/ff551540) property.

<a href="" id="dword-photometricinterp"></a>DWORD *PhotometricInterp*  
Describes the photometric interpretation for the image that is transferred. This field is required for black and white (1bpp) and grayscale (4bpp or more) images. These images need to indicate the values for white and black, either WIA\_PHOTO\_WHITE\_1 (where white is 1, black is 0) or WIA\_PHOTO\_WHITE\_0 (where white is 0, black is 1). This field is optional for color images.

<a href="" id="dword-lineorder"></a>DWORD *LineOrder*  
Describes whether the lines/rows in the image data are ordered top-to-bottom or bottom-to-top. Two new constants were defined in *wiadef.h* for this:

```
#define  WIA_LINE_ORDER_TOP_TO_BOTTOM        0x00000001 
#define  WIA_LINE_ORDER_BOTTOM_TO_TOP        0x00000002
```

There is no new property defined for this. This isn't a configurable scan setting. *LingOrder* only matters when executing image data transfers.

<a href="" id="dword-rawdatasize"></a>DWORD *RawDataSize*  
Indicates the size, in bytes, of the raw data following the header (not including the optional color palette). Applications could use this field to verify the completion of a presumed successful image transfer. When this information is unknown to the minidriver at the time the transfer begins (and the header is written to the stream) - for example when the image is scanned using automatic border detection - the minidriver should be required to fill in this field at the end of the image data transfer, similar to how the XExtent and YExtent fields are handled.

<a href="" id="dword-paletteoffset"></a>DWORD *PaletteOffset*  
Contains the offset, in bytes where the color palette starts in the data stream; this offset starts (at position zero) where the header ends.. The palette and raw image data can follow the raw header in any order and the palette can be omitted when not needed.

<a href="" id="dword-palettesize"></a>DWORD *PaletteSize*  
Contains the size, in bytes, of the color palette. When no palette is required to be attached to the raw image data, minidriver should set this field to 0. This field is not related to the number of entries in the palette.

Black and white and grayscale data can omit the palette (because the information required to build the palette is contained in the *PhotometricInterpretation* field) or supply an optimized palette along with the *PhotometricInterpretation* field.

For indexed images, the number of entries in the color palette is dictated by the current *BitsPerPixel* value (2 ^ *BitsPerPixel*. For example, 2 entries for 1bpp, 16 entries for 4bpp, 256 entries for 8bpp). The format of the palette entries would be dictated by the number of entries in *BitsPerChannel* field (the number of fields/channels in each palette entry) and *BitsPerChannel* values (each field would contain exactly the value specified in the *BitsPerChannel* field for the respective channel). Each palette entry field must be BYTE-aligned.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20RAW%20Data%20Header%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


