---
title: WIA_IPS_PRINTER_ENDORSER_GRAPHICS
description: The WIA_IPS_PRINTER_ENDORSER_GRAPHICS property is used to report whether the Imprinter/Endorser item supports graphics and image data along with text.
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_GRAPHICS

The **WIA_IPS_PRINTER_ENDORSER_GRAPHICS** property is used to report whether the Imprinter/Endorser item supports graphics and image data along with text. Graphics are typically used by the device to print/endorse near the text, or as a background image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4 (Boolean)

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If **WIA_IPS_PRINTER_ENDORSER_GRAPHICS** is supported and set to a value of nonzero (True), the Imprinter/Endorser supports graphic data.

This property is required for all Imprinter/Endorser items, but it can be implemented to always report a value of 0 (False).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
