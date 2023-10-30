---
title: WIA_IPS_AUTO_CROP
description: The WIA_IPS_AUTO_CROP property is used to enable automatic detection and cropping by the device of the scan region.
keywords: ["WIA_IPS_AUTO_CROP Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_AUTO_CROP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_AUTO_CROP

The **WIA_IPS_AUTO_CROP** property is used to enable automatic detection and cropping by the device of the scan region. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/Write

## Remarks

The following table describes the valid values for the **WIA_IPS_AUTO_CROP** property.

| Value | Definition |
|--|--|
| WIA_AUTO_CROP_DISABLED | Auto-crop is disabled. This is the required default value if the property is supported. |
| WIA_AUTO_CROP_SINGLE | Auto-crop is enabled. One scan region is detected and cropped on each document page. |
| WIA_AUTO_CROP_MULTI | Auto-crop is enabled. One or multiple scan regions are detected and cropped on each document page. Each cropped scan region is transferred to the WIA application client as one single-page file or as a new page in a multi-page file. |

This property is valid and optional for the Feeder (WIA_CATEGORY_FEEDER) item, where it can be implemented with or without the WIA_PAGE_AUTO value for the [**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md) property. This property is also valid (and optional) for the Flatbed (WIA_CATEGORY_FLATBED) and Film (WIA_CATEGORY_FILM) items, but only if segmentation isn't supported by the WIA mini-driver for the WIA_CATEGORY_FLATBED and WIA_CATEGORY_FILM input sources. If WIA_IPS_SEGMENTATION is supported, then WIA_IPS_AUTO_CROP is invalid and can't be supported at the same time.

When the property is supported, WIA_AUTO_CROP_DISABLED and at least one of the other two possible values (WIA_AUTO_CROP_SINGLE and/or WIA_AUTO_CROP_MULTI) are required, with WIA_AUTO_CROP_DISABLED being the required default.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
