---
title: WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD
description: The WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD property is used to report whether the Imprinter/Endorser item supports download image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD

The **WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD** property is used to report whether the Imprinter/Endorser item supports download image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.

Property Type: VT_I4 (Boolean)

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If the current value of this property is set to a nonzero value (True), it means that the WIA minidriver supports transferring image data that is downloaded to it by the WIA application client. The transfer file format is described by the [**WIA_IPA_FORMAT**](wia-ipa-format.md) and [**WIA_IPA_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

This property is required and valid for all Imprinter/Endorser items that report a nonzero value (True) for [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS**](wia-ips-printer-endorser-graphics.md), but it can be implemented to always report a 0 value (False). The property is invalid otherwise.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
