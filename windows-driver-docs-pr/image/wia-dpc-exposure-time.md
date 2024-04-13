---
title: WIA_DPC_EXPOSURE_TIME
description: The WIA_DPC_EXPOSURE_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.
keywords: ["WIA_DPC_EXPOSURE_TIME Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_EXPOSURE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_EXPOSURE_TIME

The WIA_DPC_EXPOSURE_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.

Property Type: VT_I4

Valid Values: WIA_PROP_RANGE or WIA_PROP_LIST

Access Rights: Read/write

## Remarks

Typically, a device uses the WIA_DPC_EXPOSURE_TIME property only when the [**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md) property is set to EXPOSUREMODE_MANUAL or EXPOSUREMODE_SHUTTER_PRIORITY.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md)
