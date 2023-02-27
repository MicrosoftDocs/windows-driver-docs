---
title: WIA_DPC_EXPOSURE_MODE
description: The WIA_DPC_EXPOSURE_MODE property indicates a camera's current exposure mode.
keywords: ["WIA_DPC_EXPOSURE_MODE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPC_EXPOSURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_EXPOSURE_MODE

The WIA_DPC_EXPOSURE_MODE property indicates a camera's current exposure mode.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application changes the WIA_DPC_EXPOSURE_MODE property to control the exposure mode of the camera device.

The following table describes the constants that are valid with WIA_DPC_EXPOSURE_MODE.

| Value | Definition |
|--|--|
| EXPOSUREMODE_APERTURE_PRIORITY | A user manually sets the aperture, and the camera device automatically sets the shutter speed. |
| EXPOSUREMODE_AUTO | The camera device automatically sets the aperture and shutter speed. |
| EXPOSUREMODE_MANUAL | A user manually sets the aperture and shutter speed. |
| EXPOSUREMODE_PROGRAM_ACTION | The camera device automatically sets the aperture and shutter speed, and it optimizes them for moving subject matter (in other words, scenes that contain fast motion). |
| EXPOSUREMODE_PROGRAM_CREATIVE | The camera device automatically sets the aperture and shutter speed, and it optimizes them for still subject matter. |
| EXPOSUREMODE_PORTRAIT | The camera device automatically sets the aperture and shutter speed, and it optimizes them for portrait photography. |
| EXPOSUREMODE_SHUTTER_PRIORITY | A user manually sets the shutter speed, and the camera device automatically sets the aperture. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
