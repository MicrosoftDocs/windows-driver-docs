---
title: WIA_IPS_PRINTER_ENDORSER_ORDER
description: The WIA_IPS_PRINTER_ENDORSER_ORDER property is used to configure the order in which the scan and imprinting/endorsing operations are to be executed relative to each other. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_ORDER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_ORDER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_ORDER

The **WIA_IPS_PRINTER_ENDORSER_ORDER** property is used to configure the order in which the scan and imprinting/endorsing operations are to be executed relative to each other. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid with the [**WIA_IPS_PREVIEW_TYPE**](wia-ips-preview-type.md) property.

| Value | Definition |
|--|--|
| WIA_PRINTER_ENDORSER_BEFORE_SCAN | Printing/endorsing is performed on a document page before this document page is scanned. |
| WIA_PRINTER_ENDORSER_AFTER_SCAN | Printing/endorsing is performed on a document page after this document page is scanned. |

This property must be supported by all Imprinter/Endorser data source items. There is no required default value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
