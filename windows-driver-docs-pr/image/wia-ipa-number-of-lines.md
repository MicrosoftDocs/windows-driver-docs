---
title: WIA_IPA_NUMBER_OF_LINES
description: The WIA_IPA_NUMBER_OF_LINES property contains the number of lines that are contained in an image (that is, the vertical height of the image, in pixels). The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_NUMBER_OF_LINES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_NUMBER_OF_LINES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPA_NUMBER_OF_LINES

The WIA_IPA_NUMBER_OF_LINES property contains the number of lines that are contained in an image (that is, the vertical height of the image, in pixels). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA_IPA_NUMBER_OF_LINES property is optional for Windows Vista drivers for all transfer-enabled items. If WIA_IPA_NUMBER_OF_LINES, [**WIA_IPA_BYTES_PER_LINE**](wia-ipa-bytes-per-line.md), and [**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md) are implemented, applications written for Windows Server 2003, Windows XP, and previous Windows versions can estimate the number of pixels per line, the number of bytes that are required for each scan line, and the total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values, which WIA_IPA_NUMBER_OF_LINES, WIA_IPA_BYTES_PER_LINE, and WIA_IPA_PIXELS_PER_LINE represent.

If a Windows Vista driver does not supply these properties, the compatibility layer in the WIA service will add these properties. When the WIA service adds these properties, they will be updated by using the [**WIA_IPA_DEPTH**](wia-ipa-depth.md), [**WIA_IPS_XEXTENT**](wia-ips-xextent.md), and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties.

Windows Vista applications should always parse the image header data to get information about the image that is more accurate than the information that is available from the preceding properties.

## Requirements

**Version:** Optional for Windows Vista drivers for all transfer-enabled items.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_BYTES_PER_LINE**](wia-ipa-bytes-per-line.md)

[**WIA_IPA_DEPTH**](wia-ipa-depth.md)

[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)
