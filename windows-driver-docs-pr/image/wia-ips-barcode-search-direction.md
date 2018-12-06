---
title: WIA\_IPS\_BARCODE\_SEARCH\_DIRECTION
description: The WIA\_IPS\_BARCODE\_SEARCH\_DIRECTION property is used to configure the direction (relative to the scan direction) in which the device searches for barcodes on each scanned document page.
ms.assetid: 8A328AEE-EAFD-4282-B902-D29BB8175461
keywords: ["WIA_IPS_BARCODE_SEARCH_DIRECTION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BARCODE_SEARCH_DIRECTION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_BARCODE\_SEARCH\_DIRECTION


The **WIA\_IPS\_BARCODE\_SEARCH\_DIRECTION** property is used to configure the direction (relative to the scan direction) in which the device searches for barcodes on each scanned document page.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_BARCODE\_SEARCH\_DIRECTION** property.

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
<td><p>WIA_BARCODE_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for barcodes horizontally.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_VERTICAL_SEARCH</p></td>
<td><p>Device searches for barcodes vertically.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_HORIZONTAL_VERTICAL_SEARCH</p></td>
<td><p>Device searches for barcodes first horizontally then vertically.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_VERTICAL_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for barcodes first vertically then horizontally.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_AUTO_SEARCH</p></td>
<td><p>Device searches for barcodes in its own direction that is automatically detected at run time or predefined.</p></td>
</tr>
</tbody>
</table>

 

This property is required for all Barcode Reader items, but it can be implemented to support only the WIA\_BARCODE\_AUTO\_SEARCH value.

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

 

 





