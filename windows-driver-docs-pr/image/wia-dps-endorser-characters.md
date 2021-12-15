---
title: WIA_DPS_ENDORSER_CHARACTERS
description: The WIA_DPS_ENDORSER_CHARACTERS property contains all of the valid characters that an application can use to create valid endorser strings.
keywords: ["WIA_DPS_ENDORSER_CHARACTERS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_ENDORSER_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_ENDORSER_CHARACTERS

The WIA_DPS_ENDORSER_CHARACTERS property contains all of the valid characters that an application can use to create valid endorser strings.

> [!NOTE]
> This property is now obsolete. Use [**WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md) instead.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

An "endorser" is a printer that is installed on a scanner that imprints a text message on every page that is scanned. The WIA minidriver should validate the setting of the [**WIA_DPS_ENDORSER_STRING**](wia-dps-endorser-string.md) property against the valid character set in the WIA_DPS_ENDORSER_CHARACTERS property. The minidriver creates and maintains this property.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_ENDORSER_STRING**](wia-dps-endorser-string.md)

[**WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md)
