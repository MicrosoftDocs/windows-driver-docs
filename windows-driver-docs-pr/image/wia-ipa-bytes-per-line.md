---
title: WIA\_IPA\_BYTES\_PER\_LINE
description: The WIA\_IPA\_BYTES\_PER\_LINE property contains the number of bytes in one scan line of an image. The WIA minidriver creates and maintains this property.
ms.assetid: f746ce05-5dfe-47fe-857a-967a6144de16
keywords: ["WIA_IPA_BYTES_PER_LINE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_BYTES_PER_LINE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_BYTES\_PER\_LINE


The WIA\_IPA\_BYTES\_PER\_LINE property contains the number of bytes in one scan line of an image. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_bytes_per_line_si"></span><span id="DDK_WIA_IPA_BYTES_PER_LINE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_IPA\_BYTES\_PER\_LINE property is optional for Windows Vista drivers for all transfer-enabled items. If this property, together with the [**WIA\_IPA\_NUMBER\_OF\_LINES**](wia-ipa-number-of-lines.md) and [**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md) properties are implemented, applications designed for Windows Server 2003, Windows XP, and previous versions of Windows can estimate the number of pixels for each line, the number of bytes that are required for each scan line, and the total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values that these properties represent.

If the Windows Vista driver does not supply these properties, the compatibility layer in a WIA service will add these properties. When the WIA service adds these properties, they will be updated by using the [**WIA\_IPA\_DEPTH**](wia-ipa-depth.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties.

Windows Vista applications should always parse the image header data to get more accurate information on the image then is available from these properties.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Optional for Windows Vista drivers for all transfer-enabled items.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPA\_DEPTH**](wia-ipa-depth.md)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](wia-ipa-number-of-lines.md)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

 

 






