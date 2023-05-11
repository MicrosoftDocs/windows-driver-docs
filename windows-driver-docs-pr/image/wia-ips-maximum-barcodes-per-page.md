---
title: WIA_IPS_MAXIMUM_BARCODES_PER_PAGE
description: The WIA_IPS_MAXIMUM_BARCODES_PER_PAGE property describes the maximum number of barcodes that the device can and should detect on one document page side when barcode detection is enabled.
keywords: ["WIA_IPS_MAXIMUM_BARCODES_PER_PAGE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_MAXIMUM_BARCODES_PER_PAGE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_MAXIMUM_BARCODES_PER_PAGE

The **WIA_IPS_MAXIMUM_BARCODES_PER_PAGE** property describes the maximum number of barcodes that the device can and should detect on one document page side when barcode detection is enabled.

Property Type: VT_UI4

Valid Values: WIA_PROP_RANGE

Access Rights: Read/Write

## Remarks

A value of 0 means "no maximum." The application can decrease the current value of this property in order to reduce the time spent on barcode detection and increase the scan speed.

This property is required for all Barcode Reader items, but it can be implemented as a range container containing only the value of 0 (minimum equal with maximum and set to 0, step size of 0).

## Requirements

**Header:** wiadef.h (include Wiadef.h)
