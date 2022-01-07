---
title: BarcodeScannerDataReceived
description: The BarcodeScannerDataReceived event occurs after a successful scan event.
ms.date: 09/07/2018
---

# BarcodeScannerDataReceived

This event occurs after a successful scan event.

The scanned data is variable length and consists of the [PosBarcodeScannerDataReceivedEventData](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ns-pointofservicedriverinterface-_posbarcodescannerdatareceivedeventdata) structure followed by **ScanDataLength** bytes of raw scan data followed by **ScanDataLabelLength** bytes of decoded scan data in which the header and footer information is removed, leaving only the scanner data. The data buffer for this event is as follows.

## Syntax

```cpp
typedef struct _PosBarcodeScannerDataReceivedEventData
{
    PosEventDataHeader Header;
    UINT32 DataType;
    UINT32 ScanDataLength;
    UINT32 ScanDataLabelLength;
} PosBarcodeScannerDataReceivedEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                            | Description                                                                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000005                                   | **Header.EventType = PosEventType::BarcodeScannerDataReceived**                                                           |
| 0000020+Scan data length + label data length | **Header.DataLength** = sizeof(**PosBarcodeScannerDataReceivedEventData**) + **ScanDataLength** + **ScanDataLabelLength** |
| UINT32                                       | **PosBarcodeScannerDataReceivedEventData.DataType**                                                                       |
| UINT32                                       | **PosBarcodeScannerDataReceivedEventData.ScanDataLength**                                                                 |
| UINT32                                       | **PosBarcodeScannerDataReceivedEventData.ScanDataLabelLength**                                                            |
| byte \[\]                                    | **ScanDataLength** bytes of raw scan data                                                                                 |
| byte \[\]                                    | **ScanDataLabelLength** bytes of decoded scan data                                                                     |

## Requirements

**Header:** pointofservicedriverinterface.h
