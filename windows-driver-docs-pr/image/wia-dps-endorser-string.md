---
title: WIA_DPS_ENDORSER_STRING
description: The WIA_DPS_ENDORSER_STRING property contains a string that is to be endorsed (that is, printed) on each page that the minidriver scans.
keywords: ["WIA_DPS_ENDORSER_STRING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_ENDORSER_STRING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPS_ENDORSER_STRING

The WIA_DPS_ENDORSER_STRING property contains a string that is to be endorsed (that is, printed) on each page that the minidriver scans.

> [!NOTE]
> This property is now obsolete. Use [**WIA_IPS_PRINTER_ENDORSER_STRING**](wia-ips-printer-endorser-string.md) instead.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read/write

## Remarks

An application sets the WIA_DPS_ENDORSER_STRING property by using the valid character set that is reported in the [**WIA_DPS_ENDORSER_CHARACTERS**](wia-dps-endorser-characters.md) property. The WIA minidriver should endorse documents only if a string is set in WIA_DPS_ENDORSER_STRING. An empty string means that the endorser functionality is disabled.

Because the driver must interpret the endorser string, your driver can use special characters in WIA_DPS_ENDORSER_STRING. However, only your applications will understand these characters.

A driver that supports the WIA_DPS_ENDORSER_STRING property must support the following tokens:

| Value | Description |
|--|--|
| $DATE$ | The date in the form YYYY/MM/DD. |
| $DAY$ | The day, in the form DD. |
| $MONTH$ | The month of the year, in the form MM. |
| $PAGE_COUNT$ | The number of pages that are transferred. |
| $TIME$ | The time of day, in the form HH:MM:SS. |
| $YEAR$ | The year, in the form YYYY. |

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_ENDORSER_CHARACTERS**](wia-dps-endorser-characters.md)

[**WIA_IPS_PRINTER_ENDORSER_STRING**](wia-ips-printer-endorser-string.md)
