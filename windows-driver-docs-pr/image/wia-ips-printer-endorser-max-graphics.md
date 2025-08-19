---
title: WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS
description: The WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS property describes the maximum number of images that the Imprinter/Endorser item can print or endorse on each page.
keywords: ["WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS

The **WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS** property describes the maximum number of images that the Imprinter/Endorser item can print or endorse on each page. This property is useful when the Imprinter/Endorser item supports graphics upload via multi-page (TYMED_MULTIPAGE_FILE) file format transfers. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT_UI4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The **WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS** property is optional for the Imprinter/Endorser items that support graphics upload. When implemented, the property value **must be** greater than zero (0).

For more information about the TYMED_MULTIPAGE_FILE constant, see [**WIA_IPA_TYMED**](wia-ipa-tymed.md).

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_TYMED**](wia-ipa-tymed.md)
