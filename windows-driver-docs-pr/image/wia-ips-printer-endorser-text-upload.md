---
title: WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD
description: The WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD property is used to report whether the Imprinter/Endorser item supports upload text data transfers. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD

The **WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD** property is used to report whether the Imprinter/Endorser item supports upload text data transfers. The WIA minidriver creates and maintains this property.

Property Type: VT_I4 (Boolean)

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If the current value of this property is set to a value of True (nonzero), the WIA minidriver supports receiving text data that is uploaded by the application client. The transfer file format is described by the [**WIA_IPA_FORMAT**](wia-ipa-format.md) and [**WIA_IPA_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

This property is required for all Imprinter/Endorser items, but it can be implemented to always report a value of 0 (False). Also, if the Imprinter/Endorser item reports WiaItemTypeFile and WiaItemTypeTransfer, this property is required and must report a nonzero value (True).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
