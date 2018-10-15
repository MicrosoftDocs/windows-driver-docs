---
title: BarcodeScannerImagePreviewReceived
description: The BarcodeScannerImagePreviewReceived event occurs when the device receives a bitmap image of the scan.
ms.assetid: 'ec05bffb-95e6-4d9c-b632-adee1cbd5bad'
ms.author: windowsdriverdev
ms.date: 9/7/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# BarcodeScannerImagePreviewReceived

This event occurs when the device receives a bitmap image of the scan.

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

typedef struct _PosEventDataHeader PosBarcodeScannerImagePreviewEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                 | Description                                                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 0x00000007                        | **EventType** = **PosEventType:: BarcodeScannerImagePreviewReceived**                            |
| 0x00000008 + length of image data | sizeof(**PosBarcodeScannerImagePreviewEventData**) + the size of the image preview data in bytes |
| Image data                        | The preview image data                                                                           |

## Requirements

**Header:** pointofservicedriverinterface.h
