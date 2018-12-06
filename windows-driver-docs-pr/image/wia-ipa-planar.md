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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





