---
title: WIA_IPS_FILM_SCAN_MODE
description: The WIA_IPS_FILM_SCAN_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_FILM_SCAN_MODE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_FILM_SCAN_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_FILM_SCAN_MODE

The WIA_IPS_FILM_SCAN_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the WIA_IPS_FILM_SCAN_MODE property.

| Scan type | Definition |
|--|--|
| WIA_FILM_COLOR_SLIDE | The scan will be a color scan. |
| WIA_FILM_COLOR_NEGATIVE | The scan will be a color scan of a negative. |
| WIA_FILM_BW_NEGATIVE | The scan will be black and white (grayscale) scan. |

This property is required for the root item in the WIA item tree of film scanners and transparency adapters.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
