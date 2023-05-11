---
title: WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS
description: The WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS property describes the maximum number of characters (excluding the NULL terminator) that the Imprinter/Endorser item can print or endorse on each page.
keywords: ["WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS

The **WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS** property describes the maximum number of characters (excluding the NULL terminator) that the Imprinter/Endorser item can print or endorse on each page. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT_UI4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The **WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS** property must be supported by all Imprinter/Endorser items. When implemented, the property value **must be** greater than zero (0).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
