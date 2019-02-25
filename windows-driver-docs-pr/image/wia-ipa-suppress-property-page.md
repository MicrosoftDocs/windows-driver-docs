---
title: WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE
description: The WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE property specifies whether to suppress the general property pages for items on a device.
ms.assetid: cce8f6f9-ec35-4d07-89b0-08c437eb689c
keywords: ["WIA_IPA_SUPPRESS_PROPERTY_PAGE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_SUPPRESS_PROPERTY_PAGE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE


The WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE property specifies whether to suppress the general property pages for items on a device.

## <span id="ddk_wia_ipa_suppress_property_page_si"></span><span id="DDK_WIA_IPA_SUPPRESS_PROPERTY_PAGE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with the WIA\_IPA\_SUPPRESS\_PROPERTY\_PAGE property.

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
<td><p>WIA_PROPPAGE_CAMERA_ITEM_GENERAL</p></td>
<td><p>Suppress the general item property page for a camera.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PROPPAGE_SCANNER_ITEM_GENERAL</p></td>
<td><p>Suppress the general item property page for a scanner.</p></td>
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
<td><p>Version</p></td>
<td><p>Available on Microsoft Windows XP and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





