---
title: BarcodeScannerTriggerReleased
description: The BarcodeScannerTriggerReleased event occurs when the barcode scanner trigger is released.
ms.date: 09/07/2018
---

# BarcodeScannerTriggerReleased

This event occurs when the barcode scanner trigger is released.

The data buffer for this event is as follows.

## Syntax

```cpp
typedef struct _PosEventDataHeader
{
    // Event enumeration value
    PosEventType EventType;

    // Size of buffer required to read entire event (including header)
    UINT32 DataLength;
} PosEventDataHeader;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value          | Description                                                                |
|-----------------------|----------------------------------------------------------------------------|
| 0x00000004 | **EventType** = **PosEventType::BarcodeScannerTriggerReleased** |
| 0x00000008 | sizeof(**PosEventDataHeader**)                                  |

## Requirements

**Header:** pointofservicedriverinterface.h
