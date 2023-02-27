---
title: WIA_DIP_VEND_DESC
description: The WIA_DIP_VEND_DESC property contains a vendor description string for the WIA minidriver. The WIA service creates and maintains this property.
keywords: ["WIA_DIP_VEND_DESC Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DIP_VEND_DESC
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DIP_VEND_DESC

The WIA_DIP_VEND_DESC property contains a vendor description string for the WIA minidriver. The WIA service creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The vendor description is obtained from the INF file. An application reads the WIA_DIP_VEND_DESC property to get a description of the device vendor.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
