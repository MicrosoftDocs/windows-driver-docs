---
title: WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL
description: The WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL property contains the number of bits in each color channel.
ms.assetid: 541d5409-b095-4bf0-bdc7-cc56d416ed43
keywords: ["WIA_IPA_RAW_BITS_PER_CHANNEL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_RAW_BITS_PER_CHANNEL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL


The WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL property contains the number of bits in each color channel.

## <span id="ddk_wia_ipa_raw_bits_per_channel_si"></span><span id="DDK_WIA_IPA_RAW_BITS_PER_CHANNEL_SI"></span>


Property Type: VT\_UI1 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL property should be reported as a vector that contains as many byte values as there are channels, where the first byte corresponds to the number of bits in the first channel, the second byte to the number of bits in the second channel, and so on. The vector must contain as many entries as the [**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](wia-ipa-channels-per-pixel.md) property reports there are channels. The driver sets WIA\_IPA\_CHANNELS PER\_PIXEL when the application sets [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) to WiaImgFmt\_RAW.

WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL is similar to the [**WIA\_IPA\_BITS\_PER\_CHANNEL**](wia-ipa-bits-per-channel.md) property (which is used for formats other than RAW).

The following table describes the required number of entries in WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL for defined WIA\_IPA\_DATATYPE values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>WIA_IPA_DATATYPE value</th>
<th>Required number of entries in WIA_IPA_RAW_BITS_PER_CHANNEL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_DATA_DITHER</p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p>WIA_DATA_GRAYSCALE</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DATA_RAW_BGR</p></td>
<td><p>3</p></td>
</tr>
<tr class="even">
<td><p>WIA_DATA_RAW_CMY</p></td>
<td><p>3</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DATA_RAW_CMYK</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p>WIA_DATA_RAW_RGB</p></td>
<td><p>3</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DATA_RAW_YUV</p></td>
<td><p>3</p></td>
</tr>
<tr class="even">
<td><p>WIA_DATA_RAW_YUVK</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p>WIA_DATA_THRESHOLD</p></td>
<td><p>1</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](wia-ipa-channels-per-pixel.md)

[**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md)

[**WIA\_IPA\_FORMAT**](wia-ipa-format.md)

 

 






