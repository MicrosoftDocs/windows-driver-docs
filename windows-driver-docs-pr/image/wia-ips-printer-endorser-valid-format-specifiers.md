---
title: WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS
description: The WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS property lists the valid special formatting character sequences that can be embedded in the character string values for the WIA\_IPS\_PRINTER\_ENDORSER\_STRING property.
ms.assetid: D7D6BA47-623A-4F8F-9E29-2C9043AD4C2F
keywords: ["WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS


The **WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS** property lists the valid special formatting character sequences that can be embedded in the character string values for the [**WIA\_IPS\_PRINTER\_ENDORSER\_STRING**](wia-ips-printer-endorser-string.md) property. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid for the **WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS** property.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Format string</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_PRINT_DATE</p></td>
<td><p>L&quot;$DATE$&quot;</p></td>
<td><p>The current date in machine locale format.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_YEAR</p></td>
<td><p>L&quot;$YEAR$&quot;</p></td>
<td><p>The current year (4 digits).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINT_MONTH</p></td>
<td><p>L&quot;$MONTH$&quot;</p></td>
<td><p>The current month (1 - 12).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_DAY</p></td>
<td><p>L&quot;$DAY$&quot;</p></td>
<td><p>The current day of the month (1 - 31).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINT_WEEK_DAY</p></td>
<td><p>L&quot;$WEEK_DAY$&quot;</p></td>
<td><p>The name of the current day of the week in machine locale language (for example, &quot;Wednesday&quot;).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_TIME_24H</p></td>
<td><p>L&quot;$HOUR_24H$&quot;</p></td>
<td><p>The current hour in 24-hour format (0 - 23).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINT_TIME_12H</p></td>
<td><p>L&quot;$ TIME_12H$&quot;</p></td>
<td><p>The current time in machine locale format, 12 hours (A.M./P.M.).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_HOUR_12H</p></td>
<td><p>L&quot;$HOUR_12H$&quot;</p></td>
<td><p>The current A.M./P.M. hour (0 - 11).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINT_AM_PM</p></td>
<td><p>L&quot;$AM_PM$&quot;</p></td>
<td><p>&quot;AM&quot; or &quot;PM&quot;.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_MINUTE</p></td>
<td><p>L&quot;$MINUTE$&quot;</p></td>
<td><p>The current minute (0 - 59).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PRINT_SECOND</p></td>
<td><p>L&quot;$SECOND$&quot;</p></td>
<td><p>The current second (0 - 59).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PRINT_PAGE_COUNT</p></td>
<td><p>L&quot;$PAGE_COUNT$&quot;</p></td>
<td><p>The value of the page counter (per job).</p></td>
</tr>
</tbody>
</table>

 

The special sequence L"$$" means the '$' character.

This property is optional for the Imprinter/Endorser data source items. Not supported means that the printer/endorser device does not support any special format sequences.

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

 

 





