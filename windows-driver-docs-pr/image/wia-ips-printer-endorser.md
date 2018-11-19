---
title: WIA\_IPS\_PRINTER\_ENDORSER
description: The WIA\_IPS\_PRINTER\_ENDORSER property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing.
ms.assetid: A9BAC8D3-AB06-4600-9EF7-E9F4846B5215
keywords: ["WIA_IPS_PRINTER_ENDORSER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER


The **WIA\_IPS\_PRINTER\_ENDORSER** property is used by the WIA minidriver to list the locations where a printer/endorser device is available, and is used by an application to select one of these locations to enable imprinting/endorsing. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the required values for the **WIA\_IPS\_PRINTER\_ENDORSER** property.

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
<td><p>WIA_PRINTER_ENDORSER_DISABLED</p></td>
<td><p>Printing/endorsing is disabled. This is the required default value for the property.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_AUTO</p></td>
<td><p>Printing/endorsing is enabled. The location (if there are multiple locations available for this imprinter/endorser) is automatically selected by the device at run time depending on the active scan input source.</p></td>
</tr>
</tbody>
</table>

 

The WIA minidriver is allowed to accept property configuration, but at scan time it ignores requests to enable printing/endorsing to an inactive scan input source.

The following table describes the optional values for the **WIA\_IPS\_PRINTER\_ENDORSER** property.

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
<td><p>WIA_PRINTER_ENDORSER_FLATBED</p></td>
<td><p>Printing/endorsing is enabled for the documents scanned on a flatbed scanner.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_FRONT</p></td>
<td><p>Printing/endorsing is enabled for the front side of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_BACK</p></td>
<td><p>Printing/endorsing is enabled for the back side of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINTER_ENDORSER_FEEDER_DUPLEX</p></td>
<td><p>Printing/endorsing is enabled for both sides of the documents scanned through a feeder (either in simplex or duplex image scan mode).</p></td>
</tr>
</tbody>
</table>

 

This property must be supported by all Imprinter/Endorser data source items. The required default value is **WIA\_PRINTER\_ENDORSER\_DISABLED**.

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

 

 





