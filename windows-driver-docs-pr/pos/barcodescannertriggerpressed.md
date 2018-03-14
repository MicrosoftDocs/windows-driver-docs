---
title: BarcodeScannerTriggerPressed
description: BarcodeScannerTriggerPressed
ms.assetid: '6f0a373f-bf3f-4201-9430-3474f84b9037'
---

# BarcodeScannerTriggerPressed


This event occurs when the barcode scanner trigger is pressed.

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

| Memory value          | Description                                                               |
|-----------------------|---------------------------------------------------------------------------|
| 0x00000003 | **EventType** = **PosEventType::BarcodeScannerTriggerPressed** |
| 0x00000008 | sizeof(**PosEventDataHeader**)                                 |



Requirements
------------

**Header:** pointofservicedriverinterface.h










