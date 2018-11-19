---
title: WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES
description: The WIA minidriver uses the WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES property to list all patch code types that are supported (understood) by the Patch Code Reader.
ms.assetid: DA55BFFD-64E9-4D96-AB04-F2112E1F117B
keywords: ["WIA_IPS_SUPPORTED_PATCH_CODE_TYPES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SUPPORTED_PATCH_CODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES


The WIA minidriver uses the **WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES** property to list all patch code types that are supported (understood) by the Patch Code Reader. The supported barcode types are reported in a VT\_VECTOR array as a single value that contains multiple entries.




Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE (single 'array'/vector value)

Access Rights: Read-only

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_SUPPORTED\_PATCH\_CODE\_TYPES** property.

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
<td><p>WIA_PATCH_CODE_1</p></td>
<td><p>Patch code 1</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_2</p></td>
<td><p>Patch code 2</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_3</p></td>
<td><p>Patch code 3</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_4</p></td>
<td><p>Patch code 4</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_6</p></td>
<td><p>Patch code 6</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_T</p></td>
<td><p>Patch code T</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_CUSTOM_BASE + N</p></td>
<td><p>WIA_PATCH_CODE_CUSTOM_BASE is the offset to all custom patch code values the WIA minidriver may add. N is a positive integer.</p></td>
</tr>
</tbody>
</table>

 

The WIA minidriver can extend this list with additional custom values defined as WIA\_PATCH\_CODE\_CUSTOM\_BASE + N, where N is a positive integer.

This property is required for all Patch Code Reader items.

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

 

 





