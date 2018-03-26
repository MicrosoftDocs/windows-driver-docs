---
title: MbbRequestComplete
description: 
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

The cleint driver uses this method to complete a specified request for sending MBIM control message to the device.

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
A handle to the framework request object that passed in from [**EvtMbbDeviceSendMbimFragment**](evt-mbb-device-send-mbim-fragment.md) callback function

*NtStatus* [in]  
An NTSTAUT value that represents the completion status of the request.

## Return value
None

## Remarks

It must only be used to complete the request from *EvtMbbDeviceSendMbimFragment* callback function.

To complete the request from [**EvtMbbDeviceReceiveMbimFragment**](evt-mbb-device-receive-mbim-fragment.md) callback function, the client driver must use [**MbbRequestCompleteWithInformation**](mbbrequestcompletewithinformation.md) method.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |