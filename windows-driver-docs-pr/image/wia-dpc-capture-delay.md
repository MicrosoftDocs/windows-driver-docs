---
title: WIA_DPC_CAPTURE_DELAY
description: The WIA_DPC_CAPTURE_DELAY property contains a value that represents the amount of time delay, in milliseconds, that should be inserted between the capture trigger and the actual initiation of a data capture.
keywords: ["WIA_DPC_CAPTURE_DELAY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_CAPTURE_DELAY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/29/2021
---

# WIA_DPC_CAPTURE_DELAY

The WIA_DPC_CAPTURE_DELAY property contains a value that represents the amount of time delay, in milliseconds, that should be inserted between the capture trigger and the actual initiation of a data capture.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST or WIA_PROP_RANGE

Access Rights: Read/write

## Remarks

The WIA_DPC_CAPTURE_DELAY property is not intended to be used to describe the time between frames for single-initiation, multiple captures such as burst or time lapse, which have separate interval properties ([**WIA_DPC_BURST_INTERVAL**](wia-dpc-burst-interval.md) and [**WIA_DPC_TIMELAPSE_INTERVAL**](wia-dpc-timelapse-interval.md), respectively). In those cases, WIA_DPC_CAPTURE_DELAY still serves as an initial delay before the first image in the series is captured, independent of the time between frames. For no precapture delay, this property should be set to zero

## Requirements

Obsolete in Windows Vista and later operating systems and should

## See also

[**WIA_DPC_BURST_INTERVAL**](wia-dpc-burst-interval.md)

[**WIA_DPC_TIMELAPSE_INTERVAL**](wia-dpc-timelapse-interval.md)
