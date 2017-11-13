---
title: WIA\_IPA\_PIXELS\_PER\_LINE
description: The WIA\_IPA\_PIXELS\_PER\_LINE property contains the number of pixels in each line of an image (that is, the width of the image, in pixels). The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_df4be0ed-73b9-4d3a-87a7-a3c6c13b1020.xml'
- 'image.wia\_ipa\_pixels\_per\_line'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ec845e34-d883-4960-a1cd-39b99e2f5941
keywords: ["WIA_IPA_PIXELS_PER_LINE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_PIXELS_PER_LINE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPA\_PIXELS\_PER\_LINE


The WIA\_IPA\_PIXELS\_PER\_LINE property contains the number of pixels in each line of an image (that is, the width of the image, in pixels). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_pixels_per_line_si"></span><span id="DDK_WIA_IPA_PIXELS_PER_LINE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_IPA\_PIXELS\_PER\_LINE property is optional for Windows Vista drivers for all transfer-enabled items. If WIA\_IPA\_PIXELS\_PER\_LINE, [**WIA\_IPA\_BYTES\_PER\_LINE**](wia-ipa-bytes-per-line.md), and [**WIA\_IPA\_NUMBER\_OF\_LINES**](wia-ipa-number-of-lines.md) are implemented, applications written for Windows Server 2003, Windows XP, and previous Windows versions can estimate the number of pixels per line, the number of bytes that are required for each scan line, and the total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values, which WIA\_IPA\_PIXELS\_PER\_LINE, WIA\_IPA\_BYTES\_PER\_LINE, and WIA\_IPA\_NUMBER\_OF\_LINES represent.

If Windows Vista driver does not supply these properties, the compatibility layer in the WIA service will add these properties. When the WIA service adds these properties, they will be updated by using the [**WIA\_IPA\_DEPTH**](wia-ipa-depth.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties.

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

## <span id="see_also"></span>See also


[**WIA\_IPA\_BYTES\_PER\_LINE**](wia-ipa-bytes-per-line.md)

[**WIA\_IPA\_DEPTH**](wia-ipa-depth.md)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](wia-ipa-number-of-lines.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_PIXELS_PER_LINE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





