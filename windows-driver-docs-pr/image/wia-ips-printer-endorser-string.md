---
title: WIA_IPS_PRINTER_ENDORSER_STRING
description: The WIA_IPS_PRINTER_ENDORSER_STRING property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_STRING Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_STRING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_STRING

The **WIA_IPS_PRINTER_ENDORSER_STRING** property is used to configure the text to be printed/endorsed. The WIA minidriver creates and maintains this property.

**Note**  This property replaces [**WIA_DPS_ENDORSER_STRING**](wia-dps-endorser-string.md), which is now obsolete.

Property Type: VT_BSTR

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The text to be printed/endorsed can be represented by one or multiple character strings. Each character string can contain one or more special character formatting sequences described by the [**WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS**](wia-ips-printer-endorser-valid-format-specifiers.md) property. The character strings must contain only characters specified by [**WIA_IPS_PRINTER_ENDORSER_VALID_CHARACTERS**](wia-ips-printer-endorser-valid-characters.md) and must be NULL terminated. When multiple character strings are configured, the WIA minidriver must print/endorse each string on a new page (cycling through the list of strings).

This property is optional for all Imprinter/Endorser data source items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_ENDORSER_STRING**](wia-dps-endorser-string.md)
