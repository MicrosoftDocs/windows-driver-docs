---
title: MbbRequestCompleteWithInformation
description: 
ms.assetid: 72AA2E74-CECB-4E68-AA3D-E8DDFEE3A40F
keywords:
- Mobile Broadband WDF Class Extension MbbRequestCompleteWithInformation, MBBCx MbbRequestCompleteWithInformation
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestCompleteWithInformation

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The cleint driver uses this method to complete a specified request for receiving MBIM response message from the device.

## Syntax

```C++
VOID
MbbRequestCompleteWithInformation(
    _In_ MBBREQUEST Request,
    _In_ NTSTATUS NtStatus,
    _In_ ULONG_PTR Information
);
```

## Parameters

*Request* [in]  
A handle to the framework request object that passed in from [**EvtMbbDeviceReceiveMbimFragment**](evt-mbb-device-receive-mbim-fragment.md) callback function.

*NtStatus* [in]  
An NTSTAUT value that represents the completion status of the request.

*Information* [in]  
The client driver must pass in the number of bytes it has written to the pre-allocated buffer. 

## Return value
None

## Remarks
It must only be used to complete the request from *EvtMbbDeviceReceiveMbimFragment* callback function.

To complete the request from [**EvtMbbDeviceReceiveMbimFragment**](evt-mbb-device-receive-mbim-fragment.md) callback function, the client driver must use [**MbbRequestCompleteWithInformation**](mbbrequestcompletewithinformation.md).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |