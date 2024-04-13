---
title: WIA_IPS_SCAN_AHEAD
description: The WIA_IPS_SCAN_AHEAD property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_SCAN_AHEAD Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SCAN_AHEAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SCAN_AHEAD

The **WIA_IPS_SCAN_AHEAD** property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.

**Note**  This property replaces [**WIA_DPS_SCAN_AHEAD_PAGES**](wia-dps-scan-ahead-pages.md), which is now obsolete.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_SCAN_AHEAD** property.

| Value | Definition |
|--|--|
| WIA_SCAN_AHEAD_DISABLED | Scan ahead is disabled. This is the required default value if the property is supported. |
| WIA_SCAN_AHEAD_ENABLED | Scan ahead is enabled. The WIA client application must download images as fast as it can. If the scan job is canceled before it is finished, some scanned documents may be lost (not yet transferred to the application). |

This property is valid only for the Feeder item (WIA_CATEGORY_FEEDER) and is optional.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_SCAN_AHEAD_PAGES**](wia-dps-scan-ahead-pages.md)
