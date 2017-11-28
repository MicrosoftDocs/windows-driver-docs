---
title: WIA\_IPS\_PREVIEW\_TYPE
description: The WIA\_IPS\_PREVIEW\_TYPE property indicates if WIA\_IPA\_DATATYPE and WIA\_IPA\_DEPTH are changed, without having to request a new preview scan. The WIA minidriver creates and maintains this property.
ms.assetid: 2d4f1052-da7a-404e-b462-9a7c2e2caf80
keywords: ["WIA_IPS_PREVIEW_TYPE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PREVIEW_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PREVIEW\_TYPE


The WIA\_IPS\_PREVIEW\_TYPE property indicates if [**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md) and [**WIA\_IPA\_DEPTH**](wia-ipa-depth.md) are changed, without having to request a new preview scan. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with the WIA\_IPS\_PREVIEW\_TYPE property.

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
<td><p>WIA_ADVANCED_PREVIEW</p></td>
<td><p>Live preview updates are supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BASIC_PREVIEW</p></td>
<td><p>Preview images can be updated only with a new preview scan.</p></td>
</tr>
</tbody>
</table>

 

**Note**   WIA\_IPS\_PREVIEW\_TYPE should describe only the [**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md) and [**WIA\_IPA\_DEPTH**](wia-ipa-depth.md) properties.

 

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


[**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md)

[**WIA\_IPA\_DEPTH**](wia-ipa-depth.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PREVIEW_TYPE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





