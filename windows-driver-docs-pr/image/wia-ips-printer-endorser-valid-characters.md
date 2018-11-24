---
title: WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS
description: The WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS property lists the characters (letters, digits, punctuation marks, and so on) that are valid for the WIA\_IPS\_PRINTER\_ENDORSER\_STRING values that can be configured for the Imprinter/Endorser.
ms.assetid: 763355B8-7CA0-4B3F-87B1-BD51F24CF78C
keywords: ["WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS


The **WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS** property lists the characters (letters, digits, punctuation marks, and so on) that are valid for the [**WIA\_IPS\_PRINTER\_ENDORSER\_STRING**](wia-ips-printer-endorser-string.md) values that can be configured for the Imprinter/Endorser. The set of valid characters is specified as a NULL-terminated character string. The WIA minidriver creates and maintains this property.




**Note**  This property replaces [**WIA\_DPS\_ENDORSER\_CHARACTERS**](wia-dps-endorser-characters.md), which is now obsolete.

 

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

All Imprinter/Endorser items must support all characters that occur in the [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md) values (if any), including the '$' character. If the Imprinter/Endorser supports the WiaImgFmt\_CSV value for [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md), the ',' (comma) character must not be listed by **WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_CHARACTERS**.

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


[**WIA\_DPS\_ENDORSER\_CHARACTERS**](wia-dps-endorser-characters.md)

[**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md)

 

 






