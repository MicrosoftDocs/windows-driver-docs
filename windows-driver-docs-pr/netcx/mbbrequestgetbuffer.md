---
title: MbbRequestGetBuffer
description: 
ms.assetid: 527D4C3E-0A56-43B5-A0B9-3EDC66F0A4A0
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetBuffer, MBBCx MbbRequestGetBuffer
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestGetBuffer

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver shall call this method to get the memory location where the MBIM control message would be stored.

## Syntax

```C++
PVOID
MbbRequestGetBuffer(
    _In_ MBBREQUEST Request,
    _Out_opt_ size_t* BufferSize
);
```

## Parameters

*Request* [in]  
A handle to the framework object which represents a request from MbbCx framework, either to send a MBIM control command message to the device, or receive a MBIM control response message from the device.

*BufferSize* [out, opt]

A pointer to a location that receives the size, in bytes, of the MBIM control message fragment.

## Return value
It returns a pointer to the memory location where the MBIM message is stored:
- When this method is called on a request object passed from [**EvtMbbDeviceSendMbimFragment**](evt-mbb-device-send-mbim-fragment.md) callback function, it points to the MBIM control command fragment sent from the MbbCx framework to the device. It's read-only.

- When this method is called on a request object passed from [**EvtMbbDeviceReceiveMbimFragment**](evt-mbb-device-receive-mbim-fragment.md) callback function, it points to an empty buffer where the client driver should write the MBIM control response to. This buffer is pre-allocated by the MbbCx framework, and *BufferSize* parameter specifies its size.

## Remarks
For more information, see [**Handling MBIM control messages**](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).
## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |