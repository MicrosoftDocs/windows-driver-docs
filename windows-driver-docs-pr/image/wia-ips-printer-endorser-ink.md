---
title: WIA_IPS_PRINTER_ENDORSER_INK
description: The WIA_IPS_PRINTER_ENDORSER_INK property is used to report the current ink or toner status for the Imprinter/Endorser device.
keywords: ["WIA_IPS_PRINTER_ENDORSER_INK Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_INK
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_INK

The **WIA_IPS_PRINTER_ENDORSER_INK** property is used to report the current ink or toner status for the Imprinter/Endorser device. The property value indicates the remaining available ink, as a percentage of the total capacity. For example, a value of 50 indicates that there is half or 50% ink remaining. This property is initialized and maintained by the WIA mini-driver. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-Write

## Remarks

The **WIA_IPS_PRINTER_ENDORSER_INK** property is optional for the Imprinter/Endorser items. The valid values for this property are between 0 and 100, inclusive.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
