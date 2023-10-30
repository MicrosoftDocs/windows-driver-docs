---
title: WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION
description: The WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION

The **WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION** property is used to configure the position of the image (graphics) relative to the text content to be printed/endorsed. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the constants that are valid with **WIA_IPS_PRINTER_ENDORSER_GRAPHICS_POSITION**.

| Value | Definition |
|--|--|
| WIA_PRINTER_ENDORSER_GRAPHICS_LEFT | The image is printed/endorsed at the left side of the of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_RIGHT | The image is printed/endorsed at the right side of the of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_TOP | The image is printed/endorsed at the top of the of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM | The image is printed/endorsed at the bottom of the of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_TOP_LEFT | The image is printed/endorsed at the top-left corner of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_TOP_RIGHT | The image is printed/endorsed at the top-right corner of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM_LEFT | The image is printed/endorsed at the bottom-left corner of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_BOTTOM_RIGHT | The image is printed/endorsed at the bottom-right corner of the imprinter/endorser area. |
| WIA_PRINTER_ENDORSER_GRAPHICS_BACKGROUND | The image is printed/endorsed as background and the text is printed/endorsed over the image. |
| WIA_PRINTER_ENDORSER_GRAPHICS_RANDOM | The image is printed/endorsed at a random position chosen by the device. |
| WIA_PRINTER_ENDORSER_GRAPHICS_DEVICE_DEFAULT | The image is printed/endorsed at the default (preferred) position chosen by the device. |

The WIA_PRINTER_ENDORSER_ GRAPHICS_DEVICE_DEFAULT value is the required default value that all Imprinter/Endorser items must support when this property is supported.

This property is required and valid for all Imprinter/Endorser items that report a value of nonzero (True) for [**WIA_IPS_PRINTER_ENDORSER_GRAPHICS**](wia-ips-printer-endorser-graphics.md). The property is invalid otherwise.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
