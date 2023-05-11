---
title: WIA_DPS_SERVICE_ID
description: The WIA_DPS_SERVICE_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_SERVICE_ID Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_SERVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_DPS_SERVICE_ID

The WIA_DPS_SERVICE_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA minidriver initializes this property at run time by reading the PKEY_PNPX_ServiceId device property from the Function Instance object.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_DEVICE_ID**](wia-dps-device-id.md)

[**WIA_DPS_GLOBAL_IDENTITY**](wia-dps-global-identity.md)
