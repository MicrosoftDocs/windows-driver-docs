---
title: ReleaseDeviceRequested
description: The ReleaseDeviceRequested event occurs when another client attempts to claim a device.
ms.assetid: '0fcb8905-1370-4260-9456-6c80e2186dfc'
ms.author: windowsdriverdev
ms.date: 9/7/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ReleaseDeviceRequested

This event occurs when another client attempts to claim a device. The data buffer for this event is as follows.

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

| Memory value          | Description                               |
|-----------------------|-------------------------------------------|
| 0x00000001 | **EventType = PosEventType::ReleaseDeviceRequested** |
| 0x00000008 | sizeof(**PosEventDataHeader**)                       |

## Remarks

This event is handled on behalf of the device driver by Point of Service Class Extension (PosCx). When a client attempts to claim a device that another client is using, PosCx raises this event in the client that currently has a claim on the scanner device to indicate that another client is attempting to claim the device. The current client is expected to either retain its claim ([IOCTL\_POINT\_OF\_SERVICE\_RETAIN\_DEVICE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/pointofservicedriverinterface/ni-pointofservicedriverinterface-ioctl_point_of_service_retain_device)) or release its claim ([IOCTL\_POINT\_OF\_SERVICE\_RELEASE\_DEVICE](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/pointofservicedriverinterface/ni-pointofservicedriverinterface-ioctl_point_of_service_release_device)) of the device in response to this event. If the current client does not retain its claim on the device, its **ClaimedBarcodeScanner** object will no longer be valid.

## Requirements

**Header:** pointofservicedriverinterface.h
