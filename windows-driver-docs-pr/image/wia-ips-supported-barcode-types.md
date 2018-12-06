---
title: WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES
description: The WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES property is used by the WIA minidriver to list all barcode types supported (understood) by the Barcode Reader.
ms.assetid: 38CA1167-25DB-4495-B31A-F996671E2686
keywords: ["WIA_IPS_SUPPORTED_BARCODE_TYPES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SUPPORTED_BARCODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES


The **WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES** property is used by the WIA minidriver to list all barcode types supported (understood) by the Barcode Reader. The supported barcode types are reported in a VT\_VECTOR array as a single value that contains multiple entries.




Property Type: VT\_I4 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE (single array/vector value)

Access Rights: Read-only

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_SUPPORTED\_BARCODE\_TYPES** property.

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
<td><p>WIA_BARCODE_UPCA</p></td>
<td><p>Universal Product Code UPC-A</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_UPCE</p></td>
<td><p>Universal Product Code UPC-E</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CODABAR</p></td>
<td><p>Codabar code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_NONINTERLEAVED_2OF5</p></td>
<td><p>Two-out-of-five code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_INTERLEAVED_2OF5</p></td>
<td><p>Interleaved 2 of 5 code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_CODE39</p></td>
<td><p>Code 39</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CODE39_MOD43</p></td>
<td><p>Code 39 mod 43</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_CODE39_FULLASCII</p></td>
<td><p>Full ASCII Code 39</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CODE93</p></td>
<td><p>Code 93</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_CODE128</p></td>
<td><p>Code 128</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CODE128A</p></td>
<td><p>Code 128A</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_CODE128B</p></td>
<td><p>Code 128B</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CODE128C</p></td>
<td><p>Code 128C</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_GS1128</p></td>
<td><p>GS1-128 (formerly known as UCC/EAN-128)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_GS1DATABAR WIA_BARCODE_ITF14</p></td>
<td><p>GS1 DataBar code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_ITF14</p></td>
<td><p>ITF-14 code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_EAN8</p></td>
<td><p>EAN-8 code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_EAN13</p></td>
<td><p>EAN-13 code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_POSTNETA</p></td>
<td><p>POSTNET (Postal Numeric Encoding Technique) &quot;A&quot; code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_POSTNETB</p></td>
<td><p>POSTNET (Postal Numeric Encoding Technique) &quot;B&quot; code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_POSTNETC</p></td>
<td><p>POSTNET (Postal Numeric Encoding Technique) &quot;C&quot; code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_POSTNET_DPBC</p></td>
<td><p>POSTNET (Postal Numeric Encoding Technique) DPBC (Delivery Point Bar Code) code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_PLANET</p></td>
<td><p>Postal Alpha Numeric Encoding Technique (PLANET) code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_INTELLIGENT_MAIL</p></td>
<td><p>Intelligent Mail Barcode (replaces POSTNET and PLANET barcodes)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_POSTBAR</p></td>
<td><p>PostBar (also known as CPC 4-State)</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_RM4SCC</p></td>
<td><p>RM4SCC barcode</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_HIGH_CAPACITY_COLOR</p></td>
<td><p>Microsoft High Capacity Color Barcode (HCCB)</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_MAXICODE</p></td>
<td><p>MaxiCode</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_PDF417</p></td>
<td><p>PDF417</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_CPCBINARY</p></td>
<td><p>CPC Binary Barcode (Canada Post)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_FIM</p></td>
<td><p>Face Identification Mark (FIM) barcode (USPS)</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_PHARMACODE</p></td>
<td><p>Pharmaceutical Binary Code (Pharmacode)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_PLESSEY</p></td>
<td><p>Plessey Code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_MSI</p></td>
<td><p>MSI (Modified Plessey) code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_JAN</p></td>
<td><p>Japanese Article Number (JAN) code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_TELEPEN</p></td>
<td><p>Telepen code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_AZTEC</p></td>
<td><p>Aztec Code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_SMALLAZTEC</p></td>
<td><p>Small Aztec Code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_DATAMATRIX</p></td>
<td><p>Data Matrix code</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_DATASTRIP</p></td>
<td><p>Datastrip code (Cauzin Softstrip)</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_EZCODE</p></td>
<td><p>Ezcode</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_QRCODE</p></td>
<td><p>QR Code</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_SHOTCODE</p></td>
<td><p>ShotCode</p></td>
</tr>
<tr class="even">
<td><p>WIA_BARCODE_SPARQCODE</p></td>
<td><p>SPARQCode</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BARCODE_CUSTOM_BASE + N</p></td>
<td><p>WIA_BARCODE_CUSTOM_BASE is the offset to all custom barcode values that the WIA minidriver may add. N is a positive integer.</p></td>
</tr>
</tbody>
</table>

 

The WIA minidriver can extend this list with additional custom values defined as WIA\_BARCODE\_CUSTOM\_BASE + N, where N is a positive integer.

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

 

 





