---
title: WIA_DPS_SCAN_AHEAD_PAGES
description: The WIA_DPS_SCAN_AHEAD_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.
keywords: ["WIA_DPS_SCAN_AHEAD_PAGES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_SCAN_AHEAD_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_SCAN_AHEAD_PAGES

The WIA_DPS_SCAN_AHEAD_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.

> [!NOTE]
> This property is obsolete. Use [**WIA_IPS_SCAN_AHEAD**](wia-ips-scan-ahead.md) instead.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE (from zero through the maximum number of pages that the document feeder can hold)

Access Rights: Read/write

## Remarks

If the WIA_DPS_SCAN_AHEAD_PAGES property is zero, scan ahead is disabled, and the scanner will not scan ahead any pages.

If the scanner performs data transfers on the buffered scan-ahead item, the scanner will retrieve the buffered pages. WIA properties cannot be changed during a scan-ahead operation. WIA_DPS_SCAN_AHEAD_PAGES is optional.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPS_SCAN_AHEAD**](wia-ips-scan-ahead.md)
