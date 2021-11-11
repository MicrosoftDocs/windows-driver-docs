---
title: WIA_DPS_DEVICE_ID
description: The WIA_DPS_DEVICE_ID property contains a unique Function Instance identifier for a web services scanner device.
keywords: ["WIA_DPS_DEVICE_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DEVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPS_DEVICE_ID

The WIA_DPS_DEVICE_ID property contains a unique Function Instance identifier for a web services scanner device. This identifier represents the web service on the scanner device with which the WIA minidriver is communicating. No assumptions about the form of this identifier should be made. The WIA minidriver creates and maintains this property.

WIA applications can use the value of WIA_DPS_DEVICE_ID to find, using the Function Discovery API, the Function Instance object that represents the web services scanner device used in the current WIA session.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The WIA minidriver initializes this property at run time by reading the PKEY_PNPX_ID device property from the Function Instance object.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPS_GLOBAL_IDENTITY**](wia-dps-global-identity.md)

[**WIA_DPS_SERVICE_ID**](wia-dps-service-id.md)
