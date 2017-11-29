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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

## <span id="see_also"></span>See also


[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](wia-ipa-channels-per-pixel.md)

[**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md)

[**WIA\_IPA\_FORMAT**](wia-ipa-format.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_RAW_BITS_PER_CHANNEL%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





