---
title: WIA\_IPA\_PLANAR
description: The WIA\_IPA\_PLANAR property contains image data packing options. The WIA minidriver creates and maintains this property.
ms.assetid: df4013db-8f9e-428a-83dd-c344f7998034
keywords: ["WIA_IPA_PLANAR Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_PLANAR
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPA\_PLANAR


The WIA\_IPA\_PLANAR property contains image data packing options. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_planar_si"></span><span id="DDK_WIA_IPA_PLANAR_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_NONE

Access Rights: Read/write or read-only

Remarks
-------

An application reads WIA\_IPA\_PLANAR to determine the image packing options or sets the current image packing options.

The following table describes the constants that are valid with WIA\_IPA\_PLANAR.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_PACKED_PIXEL</p></td>
<td><p>Image data is in packed-pixel format.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PLANAR</p></td>
<td><p>Image data is in planar format.</p></td>
</tr>
</tbody>
</table>

 

If a device can be set to only a single value, you can implement the WIA\_IPA\_PLANAR property as WIA\_PROP\_NONE and read-only.

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
<td><p>Obsolete in Windows Vista and later operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_PLANAR%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




