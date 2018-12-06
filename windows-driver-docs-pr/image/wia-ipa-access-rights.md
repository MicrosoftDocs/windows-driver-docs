---
title: WIA\_IPA\_ACCESS\_RIGHTS
description: The WIA\_IPA\_ACCESS\_RIGHTS property contains the access rights for a WIA item.
ms.assetid: 5bfa9406-2cb6-4c8b-ab25-6f8f55d941d4
keywords: ["WIA_IPA_ACCESS_RIGHTS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ACCESS_RIGHTS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_ACCESS\_RIGHTS


The WIA\_IPA\_ACCESS\_RIGHTS property contains the access rights for a WIA item.

## <span id="ddk_wia_ipa_access_rights_si"></span><span id="DDK_WIA_IPA_ACCESS_RIGHTS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_FLAG

Access Rights: Read/write or read-only (depending on the item's ability to have its access rights changed)

Remarks
-------

*Access rights* control the ability of an application to delete items in the WIA item tree. The WIA minidriver creates and maintains the WIA\_IPA\_ACCESS\_RIGHTS property.

The following table describes the constants that are valid with WIA\_IPA\_ACCESS\_RIGHTS.

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
<td><p>WIA_ITEM_CAN_BE_DELETED</p></td>
<td><p>This WIA item can be deleted.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ITEM_READ</p></td>
<td><p>Access to the item is read-only.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_ITEM_WRITE</p></td>
<td><p>Access to the item is read/write.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ITEM_RD</p></td>
<td><p>WIA_ITEM_READ | WIA_ITEM_CAN_BE_DELETED</p></td>
</tr>
<tr class="odd">
<td><p>WIA_ITEM_RWD</p></td>
<td><p>WIA_ITEM_READ | WIA_ITEM_WRITE | WIA_ITEM_CAN_BE_DELETED</p></td>
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

 

 





