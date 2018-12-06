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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

## See also


[**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md)

[**WIA\_IPA\_DEPTH**](wia-ipa-depth.md)

 

 






