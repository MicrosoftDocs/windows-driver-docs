---
title: WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE
description: The WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE property contains the physical horizontal dimensions of the smallest page that a scanner's document feeder can scan, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE

The WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE property contains the physical horizontal dimensions of the smallest page that a scanner's document feeder can scan, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Requirements

**Version:** Beginning with Windows Vista, the WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE property is still available at the root level of the WIA driver, but it has been replaced by the WIA_IPS_MIN_HORIZONTAL_SIZE property, so you should consider it optional.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE**](wia-dps-min-vertical-sheet-feed-size.md)

[**WIA_IPS_MIN_HORIZONTAL_SIZE**](wia-ips-min-horizontal-size.md)
