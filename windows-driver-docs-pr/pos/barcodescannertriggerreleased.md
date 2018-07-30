---
title: BarcodeScannerTriggerReleased
description: BarcodeScannerTriggerReleased
ms.assetid: '49b655c3-2652-4225-ba4c-5404da672b8e'
ms.localizationpriority: medium
---

# BarcodeScannerTriggerReleased


This event occurs when the barcode scanner trigger is released.

The data buffer for this event is as follows.

Syntax
------

``` syntax
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



Requirements
------------

**Header:** pointofservicedriverinterface.h










