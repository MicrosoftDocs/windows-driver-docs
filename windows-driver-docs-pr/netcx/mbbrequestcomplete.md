---
title: MbbRequestComplete
description: Client drivers call the MbbRequestComplete method to complete a specified request for sending an MBIM control message to the device.
ms.assetid: 7BD76E70-4F63-4F76-A8B9-B7FACBE0936C
keywords:
- Mobile Broadband WDF Class Extension MbbRequestComplete, MBBCx MbbRequestComplete
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestComplete

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

Client drivers call the **MbbRequestComplete** method to complete a specified request for sending an MBIM control message to the device.

## Syntax

```C++
VOID
MbbRequestComplete(
    _In_ MBBREQUEST Request,
    _In_ NTSTATUS NtStatus
);
```

## Parameters

*Request* [in]  
A handle to the framework request object passed in from the [*EvtMbbDeviceSendMbimFragment*](evt-mbb-device-send-mbim-fragment.md) callback function.

*NtStatus* [in]  
An NTSTATUS value that represents the completion status of the request.

## Return value

This method does not return a value.

## Remarks

This method must only be used to complete requests from the [*EvtMbbDeviceSendMbimFragment*](evt-mbb-device-send-mbim-fragment.md) callback function.

To complete the request from [*EvtMbbDeviceReceiveMbimFragment*](evt-mbb-device-receive-mbim-fragment.md) callback function, the client driver must call the [**MbbRequestCompleteWithInformation**](mbbrequestcompletewithinformation.md) method.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |