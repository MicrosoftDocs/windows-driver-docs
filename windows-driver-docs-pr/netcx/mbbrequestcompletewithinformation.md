---
title: MbbRequestCompleteWithInformation
description: Client drivers call the MbbRequestCompleteWithInformation method to complete a specified request for receiving an MBIM response message from the device.
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

Client drivers call the **MbbRequestCompleteWithInformation** method to complete a specified request for receiving an MBIM response message from the device.

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
A handle to the framework request object passed in from the [*EvtMbbDeviceReceiveMbimFragment*](evt-mbb-device-receive-mbim-fragment.md) callback function.

*NtStatus* [in]  
An NTSTATUS value that represents the completion status of the request.

*Information* [in]  
The client driver must pass in the number of bytes it has written to the pre-allocated buffer. 

## Return value

This method does not return a value.

## Remarks

This method must only be used to complete requests from the [*EvtMbbDeviceReceiveMbimFragment*](evt-mbb-device-receive-mbim-fragment.md) callback function.

To complete requests from the [*EvtMbbDeviceReceiveMbimFragment*](evt-mbb-device-receive-mbim-fragment.md) callback function, the client driver must call the [**MbbRequestCompleteWithInformation**](mbbrequestcompletewithinformation.md) method.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |