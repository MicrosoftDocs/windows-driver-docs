---
title: WIA_IPS_OVER_SCAN_RIGHT
description: The WIA_IPS_OVER_SCAN_RIGHT property along with WIA_IPS_OVER_SCAN_LEFT, WIA_IPS_OVER_SCAN_TOP, and WIA_IPS_OVER_SCAN_BOTTOM are used to configure the amount of over scanning, in thousandths of an inch (0.001 \ 0034;) units, relative to the physical document.
keywords: ["WIA_IPS_OVER_SCAN_RIGHT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_OVER_SCAN_RIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_OVER_SCAN_RIGHT

The **WIA_IPS_OVER_SCAN_RIGHT** property along with [**WIA_IPS_OVER_SCAN_LEFT**](wia-ips-over-scan-left.md), [**WIA_IPS_OVER_SCAN_TOP**](wia-ips-over-scan-top.md), and [**WIA_IPS_OVER_SCAN_BOTTOM**](wia-ips-over-scan-bottom.md) are used to configure the amount of over scanning, in thousandths of an inch (0.001") units, relative to the physical document. The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

This property is valid for all programmable image data source items, including Flatbed (WIA_CATEGORY_FLATBED) and Feeder (WIA_CATEGORY_FEEDER) but only when the [**WIA_IPS_OVER_SCAN**](wia-ips-over-scan.md) property is supported. When it is supported, this property is required.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
