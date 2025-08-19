---
title: WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS
description: The WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS property lists the valid special formatting character sequences that can be embedded in the character string values for the WIA_IPS_PRINTER_ENDORSER_STRING property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS

The **WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS** property lists the valid special formatting character sequences that can be embedded in the character string values for the [**WIA_IPS_PRINTER_ENDORSER_STRING**](wia-ips-printer-endorser-string.md) property. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-only

## Remarks

The following table describes the constants that are valid for the **WIA_IPS_PRINTER_ENDORSER_VALID_FORMAT_SPECIFIERS** property.

| Value | Format string | Description |
|--|--|--|
| WIA_PRINT_DATE | L"\$DATE\$" | The current date in machine locale format. |
| WIA_PRINT_YEAR | L"\$YEAR\$" | The current year (4 digits). |
| WIA_PRINT_MONTH | L"\$MONTH\$" | The current month (1 - 12). |
| WIA_PRINT_DAY | L"\$DAY\$" | The current day of the month (1 - 31). |
| WIA_PRINT_WEEK_DAY | L"\$WEEK_DAY\$" | The name of the current day of the week in machine locale language (for example, "Wednesday"). |
| WIA_PRINT_TIME_24H | L"\$HOUR_24H\$" | The current hour in 24-hour format (0 - 23). |
| WIA_PRINT_TIME_12H | L"\$ TIME_12H\$" | The current time in machine locale format, 12 hours (A.M./P.M.). |
| WIA_PRINT_HOUR_12H | L"\$HOUR_12H\$" | The current A.M./P.M. hour (0 - 11). |
| WIA_PRINT_AM_PM | L"\$AM_PM\$" | "AM" or "PM". |
| WIA_PRINT_MINUTE | L"\$MINUTE\$" | The current minute (0 - 59). |
| WIA_PRINT_SECOND | L"\$SECOND\$" | The current second (0 - 59). |
| WIA_PRINT_PAGE_COUNT | L"\$PAGE_COUNT\$" | The value of the page counter (per job). |

The special sequence L"$$" means the '$' character.

This property is optional for the Imprinter/Endorser data source items. Not supported means that the printer/endorser device does not support any special format sequences.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
