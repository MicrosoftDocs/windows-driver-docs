---
title: WIA\_IPA\_NUMBER\_OF\_LINES
description: The WIA\_IPA\_NUMBER\_OF\_LINES property contains the number of lines that are contained in an image (that is, the vertical height of the image, in pixels). The WIA minidriver creates and maintains this property.
ms.assetid: 80f69a99-7008-40f1-8d12-1b7e4cf063b4
keywords: ["WIA_IPA_NUMBER_OF_LINES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_NUMBER_OF_LINES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_NUMBER\_OF\_LINES


The WIA\_IPA\_NUMBER\_OF\_LINES property contains the number of lines that are contained in an image (that is, the vertical height of the image, in pixels). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_number_of_lines_si"></span><span id="DDK_WIA_IPA_NUMBER_OF_LINES_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_IPA\_NUMBER\_OF\_LINES property is optional for Windows Vista drivers for all transfer-enabled items. If WIA\_IPA\_NUMBER\_OF\_LINES, [**WIA\_IPA\_BYTES\_PER\_LINE**](wia-ipa-bytes-per-line.md), and [**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md) are implemented, applications written for Windows Server 2003, Windows XP, and previous Windows versions can estimate the number of pixels per line, the number of bytes that are required for each scan line, and the total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values, which WIA\_IPA\_NUMBER\_OF\_LINES, WIA\_IPA\_BYTES\_PER\_LINE, and WIA\_IPA\_PIXELS\_PER\_LINE represent.

If a Windows Vista driver does not supply these properties, the compatibility layer in the WIA service will add these properties. When the WIA service adds these properties, they will be updated by using the [**WIA\_IPA\_DEPTH**](wia-ipa-depth.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties.

Windows Vista applications should always parse the image header data to get information about the image that is more accurate than the information that is available from the preceding properties.

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


[**WIA\_IPA\_BYTES\_PER\_LINE**](wia-ipa-bytes-per-line.md)

[**WIA\_IPA\_DEPTH**](wia-ipa-depth.md)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

 

 






