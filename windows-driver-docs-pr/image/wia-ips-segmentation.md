---
title: WIA_IPS_SEGMENTATION
description: The WIA_IPS_SEGMENTATION property indicates if segmentation is to be performed during a scan. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_SEGMENTATION Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_SEGMENTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/08/2023
---

# WIA_IPS_SEGMENTATION

The WIA_IPS_SEGMENTATION property indicates if segmentation is to be performed during a scan. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The following table describes the values that are defined for the WIA_IPS_SEGMENTATION property.

| Value | Definition |
|--|--|
| WIA_USE_SEGMENTATION_FILTER | The application should use the segmentation filter for multi-region scanning. |
| WIA_DONT_USE_SEGMENTATION_FILTER | The driver creates the child items itself for multi-region scanning. This situation typically occurs if a scanner uses fixed frames for multi-region scanning. |

You must implement WIA_IPS_SEGMENTATION for scanner flatbed and film items if they support the creation of child items with a segmentation filter or if the driver itself creates child items for fixed frames.

You can package a driver with a segmentation filter and still have WIA_IPS_SEGMENTATION set to WIA_DONT_USE_SEGMENTATION_FILTER for one of its items (for example, the film item). This situation could occur if the scanner uses fixed frames for film scanning, but not for scanning from the flatbed.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
