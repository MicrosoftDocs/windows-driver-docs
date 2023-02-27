---
title: WIA_DPC_EXPOSURE_METERING_MODE
description: The WIA_DPC_EXPOSURE_METERING_MODE property specifies the mode that a camera uses to automatically adjust the exposure setting.
keywords: ["WIA_DPC_EXPOSURE_METERING_MODE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_EXPOSURE_METERING_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_EXPOSURE_METERING_MODE

The WIA_DPC_EXPOSURE_METERING_MODE property specifies the mode that a camera uses to automatically adjust the exposure setting.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the constants that are valid with the WIA_DPC_EXPOSURE_METERING_MODE property.

| Value | Definition |
|--|--|
| EXPOSUREMETERING_AVERAGE | Set the exposure based on an average of the entire scene. |
| EXPOSUREMETERING_CENTERSPOT | Set the exposure based on a center spot. |
| EXPOSUREMETERING_CENTERWEIGHT | Set the exposure based on a center-weighted average. |
| EXPOSUREMETERING_MULTISPOT | Set the exposure based on a multispot pattern. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
