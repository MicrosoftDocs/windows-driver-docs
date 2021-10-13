---
title: WIA_DPC_FLASH_MODE
description: The WIA_DPC_FLASH_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.
keywords: ["WIA_DPC_FLASH_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FLASH_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DPC_FLASH_MODE

The WIA_DPC_FLASH_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the six that are valid with this property.

| Value | Definition |
|--|--|
| FLASHMODE_AUTO | The camera device determines the proper flash settings. |
| FLASHMODE_EXTERNALSYNC | The camera device is configured to synchronize with external flash units. |
| FLASHMODE_FILL | The camera device is configured to flash regardless of current lighting conditions. |
| FLASHMODE_OFF | The camera device is configured *not* to flash for any picture taken. |
| FLASHMODE_REDEYE_AUTO | The camera device determines the proper flash settings by using red-eye reduction, regardless of current lighting conditions. |
| FLASHMODE_REDEYE_FILL | The camera device is configured to use red-eye reduction and flash regardless of current lighting conditions. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)
