---
title: WIA_IPA_BYTES_PER_LINE
description: The WIA_IPA_BYTES_PER_LINE property contains the number of bytes in one scan line of an image. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_BYTES_PER_LINE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_BYTES_PER_LINE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
ms.localizationpriority: medium
---

# WIA_IPA_BYTES_PER_LINE

The WIA_IPA_BYTES_PER_LINE property contains the number of bytes in one scan line of an image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA_IPA_BYTES_PER_LINE property is optional for Windows Vista drivers for all transfer-enabled items. If this property, together with the [**WIA_IPA_NUMBER_OF_LINES**](wia-ipa-number-of-lines.md) and [**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md) properties are implemented, applications designed for Windows Server 2003, Windows XP, and previous versions of Windows can estimate the number of pixels for each line, the number of bytes that are required for each scan line, and the total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values that these properties represent.

If the Windows Vista driver does not supply these properties, the compatibility layer in a WIA service will add these properties. When the WIA service adds these properties, they will be updated by using the [**WIA_IPA_DEPTH**](wia-ipa-depth.md), [**WIA_IPS_XEXTENT**](wia-ips-xextent.md), and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties.

Windows Vista applications should always parse the image header data to get more accurate information on the image then is available from these properties.

## Requirements

**Version:** Optional for Windows Vista drivers for all transfer-enabled items.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_DEPTH**](wia-ipa-depth.md)

[**WIA_IPA_NUMBER_OF_LINES**](wia-ipa-number-of-lines.md)

[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)
