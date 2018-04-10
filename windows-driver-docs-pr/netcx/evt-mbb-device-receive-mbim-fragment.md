---
title: EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT
description: A client driver's EvtMbbDeviceReceiveMbimFragment event callback function provides the response message returned from its device in response to a previous MBIM control message sent from MBBCx. This callback function is the equivalent of the *GetEncapsulatedResponse* request defined in the MBIM specification.
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

A client driver's *EvtMbbDeviceReceiveMbimFragment* event callback function provides the response message returned from its device in response to a previous MBIM control message sent from MBBCx. This callback function is the equivalent of the *GetEncapsulatedResponse* request defined in the MBIM specification.

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
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*ReceiveRequest* [in]  
A handle to the framework object which represents the request to receive a fragemented MBIM message from the device.

## Return value

This callback function does not return a value.

## Remarks

An MBBCx client driver must register an *EvtMbbDeviceReceiveMbimFragment* callback function by calling [**MbbDeviceInitialize**](mbbdeviceinitialize.md).

The MBBCx framework calls this callback function after it is notified by the client driver that [an MBIM message is available from the device](mbbdeviceresponseavailable.md), either as a response to [a previous MBIM control message request from the framework](evt-mbb-device-send-mbim-fragment.md), or as an unsolicated device event.

In this callback function, the client driver puts the response MBIM message into the buffer space pre-allocated by the MBBCx framework. If the size of a single response message is larger than the size of the pre-allocated buffer, and then it must split this response message into multiple fragmented messages as described in the MBIM specification. When fragmentation happens, MBBCx will continue to call this callback function, once per fragment, until all fragments of the response MBIM message has been received.

To access the pre-allocated buffer space and its size, the client driver should call [**MbbRequestGetBuffer**](mbbrequestgetbuffer.md). Once the client driver fills this buffer space with the response message, or a fragment of the response message, it must call [**MbbRequestCompleteWithInformation**](mbbrequestcompletewithinformation.md) with the number of bytes actually being filled. This can be done either asychronously or sychronously.

Optionally, the client driver can call [**MbbRequestGetActivityId**](mbbrequestgetactivityid.md) to get a unique GUID that can be used to identify this receive request's matching control request that was previously sent by MBBCx. Fragments belonging to the same MBIM response message will be retreived by requests with the same GUID.

For more information, see [**Handling MBIM control messages**](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).

## Example

Error handling code has been left out of this example for brevity and clarity.

```C++
VOID
EvtMbbDeviceReceiveMbimFragment(
    WDFDEVICE  Device,
    MBBREQUEST ReceiveRequest
)
{
    size_t filledSize = 0;
    size_t bufferSize = 0;
    PVOID buffer = MbbRequestGetBuffer(ReceiveRequest, &bufferSize);

    // 
    // Write the response MBIM message into the buffer.
    // This example uses memset as an illustration of how
    // it can being completed sycnchronously.
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
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |