---
title: WIA_IPS_PRINTER_ENDORSER_NUM_LINES
description: The WIA_IPS_PRINTER_ENDORSER_NUM_LINES property specifies the maximum number of lines of text that can be printed or endorsed on each side of a document by the Imprinter/Endorser unit.
keywords: ["WIA_IPS_PRINTER_ENDORSER_NUM_LINES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_NUM_LINES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_NUM_LINES

The **WIA_IPS_PRINTER_ENDORSER_NUM_LINES** property specifies the maximum number of lines of text that can be printed or endorsed on each side of a document by the Imprinter/Endorser unit. This property is initialized and maintained by the WIA mini-driver, and it is available with Windows 8 and later versions of Windows.

Property Type: VT_UI4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The **WIA_IPS_PRINTER_ENDORSER_NUM_LINES** property is optional for the Imprinter/Endorser items. When this property is not supported, only a single line of text is allowed on each side of a document.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
