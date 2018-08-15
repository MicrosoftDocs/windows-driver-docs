---
title: MbbRequestGetBuffer
description: The client driver calls the MbbRequestGetBuffer method to get the memory location where an MBIM control message is stored or should be stored.
ms.assetid: 527D4C3E-0A56-43B5-A0B9-3EDC66F0A4A0
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetBuffer, MBBCx MbbRequestGetBuffer
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MbbRequestGetBuffer

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver calls the **MbbRequestGetBuffer** method to get the memory location where an MBIM control message is stored or should be stored.

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
A handle to the framework object which represents a request from MBBCx framework, either to send a MBIM control command message to the device or to receive an MBIM control response message from the device.

*BufferSize* [out, opt]  
A pointer to the location that receives the size, in bytes, of the MBIM control message fragment.

## Return value

Returns a pointer to the memory location where the MBIM message is stored:

- When this method is called on a request object passed from the [*EvtMbbDeviceSendMbimFragment*](evt-mbb-device-send-mbim-fragment.md) callback function, it points to the MBIM control command fragment sent from the MBBCx framework to the device. This memory location is read-only.

- When this method is called on a request object passed from the [*EvtMbbDeviceReceiveMbimFragment*](evt-mbb-device-receive-mbim-fragment.md) callback function, it points to an empty buffer to which the client driver should write the MBIM control response. This buffer is pre-allocated by the MBBCx framework and the *BufferSize* parameter specifies its size.

## Remarks

For more information, see [**Handling MBIM control messages**](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
