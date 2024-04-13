---
title: WIA_DPS_GLOBAL_IDENTITY
description: The WIA_DPS_GLOBAL_IDENTITY property contains the SOAP address of a web services scanner device. The WIA minidriver creates and maintains this property.
keywords: ["WIA_DPS_GLOBAL_IDENTITY Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_GLOBAL_IDENTITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_DPS_GLOBAL_IDENTITY

The WIA_DPS_GLOBAL_IDENTITY property contains the SOAP address of a web services scanner device. The WIA minidriver creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA minidriver initializes this property at run time by reading the PKEY_PNPX_GlobalIdentity device property from the Function Instance object.

Both PKEY_PNPX_GlobalIdentity and PKEY_PNPX_ID contain a unique ID of the UPnP Device. The difference is that PKEY_PNPX_GlobalIdentity always contains the UUID of the root device for all Function Instances, while PKEY_PNPX_ID contains the UUID of the Device/Sub-Device that the Function Instance represents.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_DEVICE_ID**](wia-dps-device-id.md)

[**WIA_DPS_SERVICE_ID**](wia-dps-service-id.md)
