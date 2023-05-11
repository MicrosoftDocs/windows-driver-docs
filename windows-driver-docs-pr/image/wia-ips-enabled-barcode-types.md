---
title: WIA_IPS_ENABLED_BARCODE_TYPES
description: The WIA_IPS_ENABLED_BARCODE_TYPES property is used to select the enabled barcodes for which the Bar Code Reader will search in the current session.
keywords: ["WIA_IPS_ENABLED_BARCODE_TYPES Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_ENABLED_BARCODE_TYPES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/05/2023
---

# WIA_IPS_ENABLED_BARCODE_TYPES

The **WIA_IPS_ENABLED_BARCODE_TYPES** property is used to select the enabled barcodes for which the Bar Code Reader will search in the current session. These barcodes can be some or all the values that the WIA minidriver reports for [**WIA_IPS_SUPPORTED_BARCODE_TYPES**](wia-ips-supported-barcode-types.md). The order of the values in the array specifies the priority order in which the respective barcodes are to be searched.

Property Type: VT_I4 | VT_VECTOR

Valid Values: WIA_PROP_NONE (single 'array'/vector value)

Access Rights: Read/Write

## Remarks

The valid values for the **WIA_IPS_ENABLED_BARCODE_TYPES** property are the same WIA_BARCODE_ values that are defined for the [**WIA_IPS_SUPPORTED_BARCODE_TYPES**](wia-ips-supported-barcode-types.md) property.

This property is required for all Barcode Reader items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
