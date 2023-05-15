---
title: WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS
description: The WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS property lists the characters (letters, digits, punctuation marks, and so on) that are valid for the WIA_IPS_PRINTER_ENDORSER_STRING values that can be configured for the Imprinter/Endorser.
keywords: ["WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS

The **WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS** property lists the characters (letters, digits, punctuation marks, and so on) that are valid for the [**WIA_IPS_PRINTER_ENDORSER_STRING**](wia-ips-printer-endorser-string.md) values that can be configured for the Imprinter/Endorser. The set of valid characters is specified as a NULL-terminated character string. The WIA minidriver creates and maintains this property.

This property replaces [**WIA_DPS_ENDORSER_CHARACTERS**](wia-dps-endorser-characters.md), which is obsolete.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

All Imprinter/Endorser items must support all characters that occur in the [**WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md) values (if any), including the '$' character. If the Imprinter/Endorser supports the WiaImgFmt_CSV value for [**WIA_IPA_TYMED**](wia-ipa-tymed.md), the ',' (comma) character must not be listed by **WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS**.

This property is optional for all Imprinter/Endorser data source items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_ENDORSER_CHARACTERS**](wia-dps-endorser-characters.md)

[**WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md)
