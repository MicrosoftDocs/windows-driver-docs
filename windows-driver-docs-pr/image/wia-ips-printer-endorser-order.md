---
title: WIA\_IPS\_PRINTER\_ENDORSER\_ORDER
description: The WIA\_IPS\_PRINTER\_ENDORSER\_ORDER property is used to configure the order in which the scan and imprinting/endorsing operations are to be executed relative to each other. The WIA minidriver creates and maintains this property.
ms.assetid: DE146E16-C956-497D-BAF5-F7CE6FAF382B
keywords: ["WIA_IPS_PRINTER_ENDORSER_ORDER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_ORDER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_ORDER


The **WIA\_IPS\_PRINTER\_ENDORSER\_ORDER** property is used to configure the order in which the scan and imprinting/endorsing operations are to be executed relative to each other. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with the [**WIA\_IPS\_PREVIEW\_TYPE**](wia-ips-preview-type.md) property.

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
<td><p>WIA_PRINTER_ENDORSER_BEFORE_SCAN</p></td>
<td><p>Printing/endorsing is performed on a document page before this document page is scanned.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_AFTER_SCAN</p></td>
<td><p>Printing/endorsing is performed on a document page after this document page is scanned.</p></td>
</tr>
</tbody>
</table>

 

This property must be supported by all Imprinter/Endorser data source items. There is no required default value.

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

 

 





