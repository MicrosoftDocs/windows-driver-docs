---
title: BarcodeScannerImagePreviewReceived
description: The BarcodeScannerImagePreviewReceived event occurs when the device receives a bitmap image of the scan.
ms.date: 03/17/2023
---

# BarcodeScannerImagePreviewReceived

This event occurs when the device receives a bitmap image of the scan. The data buffer for this event is as follows.

## Syntax

```cpp
typedef struct _PosEventDataHeader
{
    // Event enumeration value
    PosEventType EventType;

    // Size of buffer required to read entire event (including header)
    UINT32 DataLength;
} PosEventDataHeader;

typedef struct _PosEventDataHeader PosBarcodeScannerImagePreviewEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value | Description |
|---|---|
| 0x00000007 | **EventType** = **PosEventType:: BarcodeScannerImagePreviewReceived** |
| 0x00000008 + length of image data | sizeof(**PosBarcodeScannerImagePreviewEventData**) + the size of the image preview data in bytes |
| Image data | The preview image data |

## Requirements

**Header:** pointofservicedriverinterface.h
