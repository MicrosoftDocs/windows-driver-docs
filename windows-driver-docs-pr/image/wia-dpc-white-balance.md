---
title: WIA_DPC_WHITE_BALANCE
description: The WIA_DPC_WHITE_BALANCE property specifies how a digital camera blends color channels.
keywords: ["WIA_DPC_WHITE_BALANCE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_WHITE_BALANCE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
ms.localizationpriority: medium
---

# WIA_DPC_WHITE_BALANCE

The WIA_DPC_WHITE_BALANCE property specifies how a digital camera blends color channels.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes possible values for the WIA_DPC_WHITE_BALANCE property:

| Value | Definition |
|--|--|
| WHITEBALANCE_AUTO | The camera uses an automatic mechanism to set the white balance. |
| WHITEBALANCE_DAYLIGHT | The camera sets the white balance to a value that is appropriate for use in daylight conditions. |
| WHITEBALANCE_FLASH | The camera sets the white balance to a value that is appropriate for use with an electronic flash. |
| WHITEBALANCE_FLORESCENT | The camera sets the white balance to a value that is appropriate for use with a fluorescent light source. |
| WHITEBALANCE_MANUAL | Your driver can set the white balance directly by using the [**WIA_DPC_RGB_GAIN**](wia-dpc-rgb-gain.md) property. |
| WHITEBALANCE_ONEPUSH_AUTO | The camera determines the white balance setting when a user presses the capture button while pointing the camera at a white surface. |
| WHITEBALANCE_TUNGSTEN | The camera sets the white balance to a value that is appropriate for use with a tungsten light source. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_RGB_GAIN**](wia-dpc-rgb-gain.md)
