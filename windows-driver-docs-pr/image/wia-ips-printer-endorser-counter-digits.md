---
title: WIA_IPS_PRINTER_ENDORSER_COUNTER_DIGITS
description: The WIA_IPS_PRINTER_ENDORSER_COUNTER_DIGITS property describes the minimum number of digits to be always printed for the page counter.
keywords: ["WIA_IPS_PRINTER_ENDORSER_COUNTER_DIGITS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_COUNTER_DIGITS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/17/2019
---

# WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER\_DIGITS

The **WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER\_DIGITS** property describes the minimum number of digits to be always printed for the page counter. The remaining empty digits, if any, must be filled with the padding character specified by the [**WIA\_IPS\_PRINTER\_ENDORSER\_PADDING**](./wia-ips-printer-endorser-padding.md) property, if supported, or with zero (0) otherwise.

This property is initialized and maintained by the WIA mini-driver.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

## Remarks

This property is optional and valid for the Imprinter/Endorser items that support the [**WIA\_IPS\_PRINTER\_ENDORSER\_VALID\_FORMAT\_SPECIFIERS**](./wia-ips-printer-endorser-valid-format-specifiers.md) property with the **WIA\_PRINT\_PAGE\_COUNT** value. When implemented, the property value must be strictly greater than zero (0).

## Requirements

| &nbsp; | &nbsp; |
| --- |:--- |
| **Header** | Wiadef.h (include Wiadef.h) |
