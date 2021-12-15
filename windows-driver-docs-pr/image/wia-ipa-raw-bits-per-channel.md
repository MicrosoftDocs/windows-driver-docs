---
title: WIA_IPA_RAW_BITS_PER_CHANNEL
description: The WIA_IPA_RAW_BITS_PER_CHANNEL property contains the number of bits in each color channel.
keywords: ["WIA_IPA_RAW_BITS_PER_CHANNEL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_RAW_BITS_PER_CHANNEL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_RAW_BITS_PER_CHANNEL

The WIA_IPA_RAW_BITS_PER_CHANNEL property contains the number of bits in each color channel.

Property Type: VT_UI1 | VT_VECTOR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA_IPA_RAW_BITS_PER_CHANNEL property should be reported as a vector that contains as many byte values as there are channels, where the first byte corresponds to the number of bits in the first channel, the second byte to the number of bits in the second channel, and so on. The vector must contain as many entries as the [**WIA_IPA_CHANNELS_PER_PIXEL**](wia-ipa-channels-per-pixel.md) property reports there are channels. The driver sets WIA_IPA_CHANNELS PER_PIXEL when the application sets [**WIA_IPA_FORMAT**](wia-ipa-format.md) to WiaImgFmt_RAW.

WIA_IPA_RAW_BITS_PER_CHANNEL is similar to the [**WIA_IPA_BITS_PER_CHANNEL**](wia-ipa-bits-per-channel.md) property (which is used for formats other than RAW).

The following table describes the required number of entries in WIA_IPA_RAW_BITS_PER_CHANNEL for defined WIA_IPA_DATATYPE values.

| WIA_IPA_DATATYPE value | Required number of entries in WIA_IPA_RAW_BITS_PER_CHANNEL |
|--|--|
| WIA_DATA_DITHER | 1 |
| WIA_DATA_GRAYSCALE | 1 |
| WIA_DATA_RAW_BGR | 3 |
| WIA_DATA_RAW_CMY | 3 |
| WIA_DATA_RAW_CMYK | 4 |
| WIA_DATA_RAW_RGB | 3 |
| WIA_DATA_RAW_YUV | 3 |
| WIA_DATA_RAW_YUVK | 4 |
| WIA_DATA_THRESHOLD | 1 |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_CHANNELS_PER_PIXEL**](wia-ipa-channels-per-pixel.md)

[**WIA_IPA_DATATYPE**](wia-ipa-datatype.md)

[**WIA_IPA_FORMAT**](wia-ipa-format.md)
