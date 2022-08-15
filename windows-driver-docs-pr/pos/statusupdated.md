---
title: StatusUpdated
description: The device-specific StatusUpdated event represents events such as a power change notification.
ms.date: 09/07/2018
---

# StatusUpdated

This device-specific event represents events such as a power change notification.

The data buffer for this event is as follows.

## Syntax

```cpp
typedef struct _PosStatusUpdatedEventData
{
    PosEventDataHeader Header;
    UINT32 Status;
    UINT32 ExtendedStatus;
} PosStatusUpdatedEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value    | Description |
|-----------------| -------------------------------------------|
| 0x00000002 | **Header.EventType = PosEventType::StatusUpdated**  |
| 0x00000010 | **Header.DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**PosStatusUpdatedEventData.Status** + sizeof(**PosStatusUpdatedEventData.ExtendedStatus**) |
| UINT32     | **Status**. See [BarcodeStatus](/windows-hardware/drivers/ddi/pointofservicecommontypes/ne-pointofservicecommontypes-_barcodestatus).   |
| UINT32     | **ExtendedStatus** |

## Requirements

**Header:** pointofservicedriverinterface.h
