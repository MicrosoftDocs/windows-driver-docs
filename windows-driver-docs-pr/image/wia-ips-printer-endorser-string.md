---
title: WIA\_IPS\_PRINTER\_ENDORSER\_STRING
description: The WIA\_IPS\_PRINTER\_ENDORSER\_STRING property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.
ms.assetid: DF4B1361-EC9C-4BEA-97F5-9179DCB77044
keywords: ["WIA_IPS_PRINTER_ENDORSER_STRING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_STRING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_STRING


The **WIA\_IPS\_PRINTER\_ENDORSER\_STRING** property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.




**Note**  This property replaces [**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md), which is now obsolete.

 

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The text to be printed/endorsed can be represented by one or multiple character strings. Each character string can contain one or more special character formatting sequences described by the [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md) property. The character strings must contain only characters specified by [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md) and must be NULL terminated. When multiple character strings are configured, the WIA minidriver must print/endorse each string on a new page (cycling through the list of strings).

This property is optional for all Imprinter/Endorser data source items.

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

## See also


[**WIA\_DPS\_ENDORSER\_STRING**](wia-dps-endorser-string.md)

 

 






