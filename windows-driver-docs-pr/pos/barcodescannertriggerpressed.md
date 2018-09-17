---
title: BarcodeScannerTriggerPressed
description: The BarcodeScannerTriggerPressed event occurs when the barcode scanner trigger is pressed.
ms.assetid: '6f0a373f-bf3f-4201-9430-3474f84b9037'
ms.author: windowsdriverdev
ms.date: 9/7/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# BarcodeScannerTriggerPressed

This event occurs when the barcode scanner trigger is pressed.

The data buffer for this event is as follows.

## Syntax

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

## Requirements

**Header:** pointofservicedriverinterface.h
