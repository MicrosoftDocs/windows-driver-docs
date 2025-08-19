---
title: WIA_IPS_SCAN_AHEAD_CAPACITY
description: The WIA_IPS_SCAN_AHEAD_CAPACITY describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_SCAN_AHEAD_CAPACITY Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SCAN_AHEAD_CAPACITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SCAN_AHEAD_CAPACITY

The **WIA_IPS_SCAN_AHEAD_CAPACITY** describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_NONE

Access Rights: Read/Write

## Remarks

When the [**WIA_IPS_SCAN_AHEAD**](wia-ips-scan-ahead.md) property is supported, this property is valid only for the Feeder item (WIA_CATEGORY_FEEDER), and is optional.

A value of 0 means "undefined/unknown number of pages."

## Requirements

**Header:** wiadef.h (include Wiadef.h)
