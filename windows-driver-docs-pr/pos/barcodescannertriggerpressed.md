---
title: BarcodeScannerTriggerPressed
description: The BarcodeScannerTriggerPressed event occurs when the barcode scanner trigger is pressed.
ms.date: 03/17/2023
---

# BarcodeScannerTriggerPressed

This event occurs when the barcode scanner trigger is pressed. The data buffer for this event is as follows.

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

| Memory value | Description |
|---|---|
| 0x00000003 | **EventType** = **PosEventType::BarcodeScannerTriggerPressed** |
| 0x00000008 | sizeof(**PosEventDataHeader**) |

## Requirements

**Header:** pointofservicedriverinterface.h
