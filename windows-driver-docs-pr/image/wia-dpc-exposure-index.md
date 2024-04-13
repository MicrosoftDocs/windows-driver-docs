---
title: WIA_DPC_EXPOSURE_INDEX
description: The WIA_DPC_EXPOSURE_INDEX property enables you to emulate film speed settings on a digital camera.
keywords: ["WIA_DPC_EXPOSURE_INDEX Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_EXPOSURE_INDEX
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_EXPOSURE_INDEX

The WIA_DPC_EXPOSURE_INDEX property enables you to emulate film speed settings on a digital camera.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

Film speed settings correspond to the ISO designations (ASA/DIN). Typically, a device supports discrete enumerated values, but continuous control over a range of values is possible. A value of 0xFFFF for the WIA_DPC_EXPOSURE_INDEX property corresponds to the Automatic ISO setting.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
