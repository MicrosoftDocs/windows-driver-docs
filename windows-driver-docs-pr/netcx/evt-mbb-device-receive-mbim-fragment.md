---
title: EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT
description: 
ms.assetid: A2C4BF05-48EF-492E-AAF3-A8F144100608
keywords:
- Mobile Broadband WDF Class Extension EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT, MBBCx EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

A client driver's *EvtMbbDeviceReceiveMbimFragment* event callabck function puts the response message returned from its hardware in response to the previous MBIM control message sent from MbbCx. It's the equivalent of *GetEncapsulatedResponse* request defined in MBIM specification

## Syntax

```C++
EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT EvtMbbDeviceReceiveMbimFragment;

VOID
EvtMbbDeviceReceiveMbimFragment(
    _In_ WDFDEVICE Device,
    _In_ MBBREQUEST ReceiveRequest
)
{ ... }

typedef EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT *PFN_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT;
```

## Parameters

*Device* [in]  
A handle to a framework device object

*ReceiveRequest* [in]  
A handle to the framework object which represents the request to receive a fragemented MBIM message from the hardware

## Return value
None

## Remarks
A MbbCx client driver must register an *EvtMbbDeviceReceiveMbimFragment* callback function by calling [**MbbDeviceInitialize**](mbbdeviceinitialize.md)

The MbbCx framework calls this callback function after it being notified by the client driver that [**a response MBIM message is available**](), in response to a previoius MBIM control message [**request from MbbCx framework**].
In this callback function, the client driver shall put the response MBIM message into the buffer space pre-allocated by the MbbCx framework. The size of the pre-allocated buffer is equal to the maximum fragment size [**set by the client driver**](). If the size of a single response message is larger than the size of the pre-allocated buffer, and then it must split this response message into multiple fragmented messages as described in the MBIM specification. When fragmentation happens, the MbbCx will continue to call this callback function, once per fragment, until all fragments of the response MBIM message has been received.

To access the pre-allocated buffer space, the clinet driver should call [**MbbRequestGetBuffer**](). Once the client driver fills this buffer space with the response message, or a fragment of the response message, it must call [**MbbRequestCompleteWithInformation**] with the number of bytes actually being filled. This can be done either asychronously or sychronously.

Optionally, the client driver can call [**MbbRequestGetActivityId**]() to get an unique GUID that can be used to identify the receive request is for which control request sent by the MbbCx earliy on. The framgnets belongs to the same MBIM response message will be retreived by requests with the same GUID.

## Example

> Error handling code has been excised from this example for brevity and clarity.

```cpp
VOID
EvtMbbDeviceReceiveMbimFragment(
    WDFDEVICE  Device,
    MBBREQUEST ReceiveRequest
)
{
    // the client driver specified framework object context
    PMY_DEVICE_CONTEXT myContext = GetMyDeviceContext(Device);

    size_t filledSize = 0;
    size_t bufferSize = 0;
    PVOID buffer = MbbRequestGetBuffer(ReceiveRequest, &bufferSize);

    // 
    // Write the response MBIM message into buffer
    // This example uses memset as an illustration how
    // it can being completed sycnchronously
    //
    memset(buffer, '*', bufferSize);
    filledSize = bufferSize;

    MbbRequestCompleteWithInformation(ReceiveRequest,
        STATUS_SUCCESS,
        filledSize);
}
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |