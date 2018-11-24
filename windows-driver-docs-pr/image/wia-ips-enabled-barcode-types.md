---
title: WIA\_IPS\_ENABLED\_BARCODE\_TYPES
description: The WIA\_IPS\_ENABLED\_BARCODE\_TYPES property is used to select the enabled barcodes for which the Bar Code Reader will search in the current session.
ms.assetid: 7CB9FE6D-5E22-48ED-B948-01CC906CA46D
keywords: ["WIA_IPS_ENABLED_BARCODE_TYPES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ENABLED_BARCODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_ENABLED\_BARCODE\_TYPES


The **WIA\_IPS\_ENABLED\_BARCODE\_TYPES** property is used to select the enabled barcodes for which the Bar Code Reader will search in the current session. These barcodes can be some or all the values that the WIA minidriver reports for [**WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES**](wia-ips-supported-barcode-types.md). The order of the values in the array specifies the priority order in which the respective barcodes are to be searched.




Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE (single 'array'/vector value)

Access Rights: Read/Write

Remarks
-------

The valid values for the **WIA\_IPS\_ENABLED\_BARCODE\_TYPES** property are the same WIA\_BARCODE\_ values that are defined for the [**WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES**](wia-ips-supported-barcode-types.md) property.

This property is required for all Barcode Reader items.

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

 

 





