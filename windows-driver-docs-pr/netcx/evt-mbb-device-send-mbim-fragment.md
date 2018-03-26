---
title: EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT
description: 
ms.assetid: 75AD00A8-B472-46D2-89CE-5EAB3E364954
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT, MBBCx EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

A client driver's *EvtMbbDeviceSendMbimFragment* event callabck function informs its device to perform the task specified by the MBIM control message. It's the equivalent of *SendEncapsulatedCommand* request defined in MBIM specification

## Syntax

```C++
EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT EvtMbbDeviceSendMbimFragment;

VOID
EvtMbbDeviceSendMbimFragment(
    _In_ WDFDEVICE Device,
    _In_ MBBREQUEST SendRequest
)
{ ... }

typedef EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT *PFN_MBB_DEVICE_SEND_MBIM_FRAGMENT;
```

## Parameters

*Device* [in]  
A handle to a framework device object

*SendRequest* [in]  
A handle to the framework object which represents the request to send a fragemented MBIM message to the device

## Return value
None

## Remarks
A MbbCx client driver must register an *EvtMbbDeviceSendMbimFragment* callback function by calling [**MbbDeviceInitialize**](mbbdeviceinitialize.md)

The MbbCx framework calls this callback function when it wants to issue a command in the format of MBIM control message to the client driver. If the size of the MBIM control message is larger than the maximum fragment size [**set by the client driver**](), the MbbCx framework would split the MBIM control message to multiple fragmented messages, and calls this callback function once per each fragemented message.

To get the actual MBIM message fragment being sent, the client driver should call [**MbbRequestGetBuffer**]() to get the buffer where the MBIM message fragment is stored. Once its device has successfully accepts the control request, or any failure condition has happend, the client driver must acknowledge that to the MbbCx by calling [**MbbRequestComplete**](), either asynchronously or sychronously. 

Optionally, the client driver can call [**MbbRequestGetActivityId**]() to get an unique GUID that can be used to correlate all MBIM message framgnets belongs to the same control request.

For more information, see [**Handling MBIM control messages**](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).

## Example

> Error handling code has been excised from this example for brevity and clarity.

```cpp
VOID
EvtMbbDeviceSendMbimFragment(
    WDFDEVICE  Device,
    MBBREQUEST SendRequest
)
{
    // the client driver specified framework object context
    PMY_DEVICE_CONTEXT myContext = GetMyDeviceContext(Device);

    size_t bufferSize = 0;
    PVOID buffer = MbbRequestGetBuffer(SendRequest, &bufferSize);

    // this client driver example uses asynchronous completion
    auto myDeviceSendCompletionRoutine = [](MBBREQUEST SendRequest, NTSTATUS NtStatus)
    {
        //acknowledge back to MbbCx
        MbbRequestComplete(SendRequest, NtStatus);
    };

    // the client driver specified function call into its device
    NTSTATUS sendStatus = MyDeviceAsyncSend(
        //the client driver specific handle
        myContext->MyDeviceHandle,
        //the context for completion
        SendRequest,
        //MBIM message               
        buffer,
        //MBIM message size
        bufferSize,   
        //Can be used for logging purpose, for example              
        MbbRequestGetActivityId(SendRequest), 
        //the client driver specific completion routine
        myDeviceSendCompletionRoutine);

    if (sendStatus != STATUS_PENDING)
    {
        //acknowledge back to MbbCx
        myDeviceSendCompletionRoutine(
            SendRequest,
            sendStatus);
    }
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