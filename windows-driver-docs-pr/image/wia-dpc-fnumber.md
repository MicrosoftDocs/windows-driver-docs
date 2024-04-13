---
title: WIA_DPC_FNUMBER
description: The WIA_DPC_FNUMBER property corresponds to the aperture of the lens, in units of the f-stop number scaled by 100.
keywords: ["WIA_DPC_FNUMBER Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_FNUMBER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_FNUMBER

The WIA_DPC_FNUMBER property corresponds to the aperture of the lens, in units of the f-stop number scaled by 100.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The setting of the WIA_DPC_FNUMBER property is typically valid only when the [**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md) property is set to EXPOSUREMODE_MANUAL or EXPOSUREMODE_APERTURE_PRIORITY.

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_EXPOSURE_MODE**](wia-dpc-exposure-mode.md)
