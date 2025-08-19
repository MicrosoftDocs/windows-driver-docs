---
title: WIA_IPS_PRINTER_ENDORSER_FONT_TYPE
description: The WIA_IPS_PRINTER_ENDORSER_FONT_TYPE property configures the font type that is used by the printer/endorser device.
keywords: ["WIA_IPS_PRINTER_ENDORSER_FONT_TYPE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_FONT_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_FONT_TYPE

The **WIA_IPS_PRINTER_ENDORSER_FONT_TYPE** property configures the font type that is used by the printer/endorser device. This property is initialized and maintained by the WIA mini-driver. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-Write

## Remarks

The accepted values for the **WIA_IPS_PRINTER_ENDORSER_FONT_TYPE** property are shown in the following table.

| Value | Description |
|--|--|
| WIA_PRINT_FONT_NORMAL | Normal font. |
| WIA_PRINT_FONT_BOLD | Bold font. |
| WIA_PRINT_FONT_EXTRA_BOLD | Extra bold font. |
| WIA_PRINT_FONT_ITALIC_BOLD | Italic, bold font. |
| WIA_PRINT_FONT_ITALIC_EXTRA_BOLD | Italic, extra bold font. |
| WIA_PRINT_FONT_ITALIC | Italic font. |
| WIA_PRINT_FONT_SMALL | Small font. |
| WIA_PRINT_FONT_SMALL_BOLD | Small bold font. |
| WIA_PRINT_FONT_SMALL_EXTRA_BOLD | Small extra bold font. |
| WIA_PRINT_FONT_SMALL_ITALIC_BOLD | Small italic and bold font. |
| WIA_PRINT_FONT_SMALL_ITALIC_EXTRA_BOLD | Small italic and extra bold font. |
| WIA_PRINT_FONT_SMALL_ITALIC | Small italic font. |
| WIA_PRINT_FONT_LARGE | Large font. |
| WIA_PRINT_FONT_LARGE_BOLD | Large bold font. |
| WIA_PRINT_FONT_LARGE_EXTRA_BOLD | Large extra bold font. |
| WIA_PRINT_FONT_LARGE_ITALIC_BOLD | Large italic and bold font. |
| WIA_PRINT_FONT_LARGE_ITALIC_EXTRA_BOLD | Large italic and extra bold font. |
| WIA_PRINT_FONT_LARGE_ITALIC | Large italic font. |

The **WIA_IPS_PRINTER_ENDORSER_FONT_TYPE** property is optional for the Imprinter/Endorser items. When this is not supported, the printer/endorser device does not support font configuration.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
