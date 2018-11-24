---
title: WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION
description: The WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.
ms.assetid: 24541B0D-4B9B-439F-8454-AFDD3D16A448
keywords: ["WIA_IPS_PATCH_CODE_SEARCH_DIRECTION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PATCH_CODE_SEARCH_DIRECTION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION


The **WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION** property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

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
<td><p>WIA_PATCH_CODE_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for patch codes horizontally.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_VERTICAL_SEARCH</p></td>
<td><p>Device searches for patch codes vertically.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_HORIZONTAL_VERTICAL_SEARCH</p></td>
<td><p>Device searches for patch codes first horizontally then vertically.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_VERTICAL_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for patch codes first vertically then horizontally.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_AUTO_SEARCH</p></td>
<td><p>Device searches for patch codes in its own direction that is automatically detected at run-time or predefined.</p></td>
</tr>
</tbody>
</table>

 

This property is required for all Patch Code Reader items but it can be implemented to support only the WIA\_PATCH\_CODE\_AUTO\_SEARCH value.

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

 

 





