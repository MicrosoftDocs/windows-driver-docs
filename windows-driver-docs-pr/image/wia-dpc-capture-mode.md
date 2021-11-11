---
title: WIA_DPC_CAPTURE_MODE
description: The WIA_DPC_CAPTURE_MODE property sets the image capture mode.
keywords: ["WIA_DPC_CAPTURE_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_CAPTURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# WIA_DPC_CAPTURE_MODE

The WIA_DPC_CAPTURE_MODE property sets the image capture mode.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

The following table describes the three constants that are valid with the WIA_DPC_CAPTURE_MODE property.

| Value | Definition |
|--|--|
| CAPTUREMODE_BURST | Capture more than one image in quick succession as defined by the values of the [**WIA_DPC_BURST_NUMBER**](wia-dpc-burst-number.md) and [**WIA_DPC_BURST_INTERVAL**](wia-dpc-burst-interval.md) properties. |
| CAPTUREMODE_NORMAL | Normal mode for the camera. |
| CAPTUREMODE_TIMELAPSE | Capture more than one image in succession as defined by the [**WIA_DPC_TIMELAPSE_NUMBER**](wia-dpc-timelapse-number.md) and [**WIA_DPC_TIMELAPSE_INTERVAL**](wia-dpc-timelapse-interval.md) properties. |

## Requirements

**Version:** Obsolete in Windows Vista and later operating systems and should not be used.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_DPC_BURST_INTERVAL**](wia-dpc-burst-interval.md)

[**WIA_DPC_BURST_NUMBER**](wia-dpc-burst-number.md)

[**WIA_DPC_TIMELAPSE_INTERVAL**](wia-dpc-timelapse-interval.md)

[**WIA_DPC_TIMELAPSE_NUMBER**](wia-dpc-timelapse-number.md)
