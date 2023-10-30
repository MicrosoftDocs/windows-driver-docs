---
title: WIA_IPS_PRINTER_ENDORSER_PADDING
description: The WIA_IPS_PRINTER_ENDORSER_PADDING property configures the valid special padding characters that are printed or endorsed to fill blank spaces in counters, data and time sequences.
keywords: ["WIA_IPS_PRINTER_ENDORSER_PADDING Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_PADDING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_PADDING

The **WIA_IPS_PRINTER_ENDORSER_PADDING** property configures the valid special padding characters that are printed or endorsed to fill blank spaces in counters, data and time sequences. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-Write

## Remarks

The valid values for this property are shown in the following table.

| Value | Description |
|--|--|
| WIA_PRINT_PADDING_NONE | No padding. |
| WIA_PRINT_PADDING_ZERO | The zero (0) digit is used as a padding character. |
| WIA_PRINT_PADDING_BLANK | The space (blank) character is used for padding. |

The **WIA_IPS_PRINTER_ENDORSER_PADDING** property is optional for the Imprinter/Endorser items. When this property is not supported, the printer/endorser device does not support padding.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
