---
title: WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT
description: The WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT property along with WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_HEIGHT, WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_WIDTH, and WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT

The **WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT** property along with [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md), [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md), and [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH**](wia-ips-printer-endorser-graphics-min-width.md) are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.

Property Type: VT_UI4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The value reported for [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md) must be less than or equal to the value reported for **WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_HEIGHT**. The value reported for[**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH**](wia-ips-printer-endorser-graphics-min-width.md) must be less than or equal to the value reported for [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MAX_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md). The WIA minidriver can report a 0 value for all these properties to indicate that images of any size are accepted.

If nonzero values are reported, the WIA application client should not attempt and must not expect success in uploading an image that is smaller than the minimum or larger than the maximum sizes reported by the WIA minidriver through these properties. The WIA minidriver must fail image upload requests when the image size doesn't match the supported range.

This property is required and valid for all Imprinter/Endorser items that report a nonzero value (True) for [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS**](wia-ips-printer-endorser-graphics.md). These properties are invalid otherwise.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
