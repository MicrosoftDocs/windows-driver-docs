---
title: EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT
description: A client driver's EvtMbbDeviceSendMbimFragment event callabck function informs its device to perform the task specified by the MBIM control message. This callback function is the equivalent of the SendEncapsulatedCommand request defined in the MBIM specification.
ms.assetid: 75AD00A8-B472-46D2-89CE-5EAB3E364954
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT, MBBCx EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

A client driver's *EvtMbbDeviceSendMbimFragment* event callabck function informs its device to perform the task specified by the MBIM control message. This callback function is the equivalent of the *SendEncapsulatedCommand* request defined in the MBIM specification.

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
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*SendRequest* [in]  
A handle to the framework object that represents the request to send a fragemented MBIM message to the device.

## Return value

This callback function does not return a value.

## Remarks

An MBBCx client driver must register an *EvtMbbDeviceSendMbimFragment* callback function by calling [**MbbDeviceInitialize**](mbbdeviceinitialize.md).

The MBBCx framework calls this callback function when it wants to issue a command in the format of an MBIM control message to the client driver. If the size of the MBIM control message is larger than the maximum fragment size set by the client driver in the [**MBB_DEVICE_MBIM_PARAMETERS**](mbb-device-mbim-parameters.md) structure, the MBBCx framework splits the MBIM control message into multiple fragmented messages and calls this callback function once per fragemented message.

To get the actual MBIM message fragment being sent, the client driver should call [**MbbRequestGetBuffer**](mbbrequestgetbuffer.md) to get the buffer where the MBIM message fragment is stored. Once its device has successfully accepted the control request, or any failure condition has occurred, the client driver must acknowledge this to MBBCx by calling [**MbbRequestComplete**](mbbrequestcomplete.md) either asynchronously or sychronously. 

Optionally, the client driver can call [**MbbRequestGetActivityId**](mbbrequestgetactivityid.md) to get a unique GUID that can be used to correlate all MBIM message framgnets belonging to the same control request.

For more information, see [Handling MBIM control messages](writing-an-mbbcx-client-driver.md#handling-mbim-control-messages).

## Example

Error handling code has been left out of this example for brevity and clarity.

```C++
VOID
EvtMbbDeviceSendMbimFragment(
    WDFDEVICE  Device,
    MBBREQUEST SendRequest
)
{
    // The client driver-specified framework object context
    PMY_DEVICE_CONTEXT myContext = GetMyDeviceContext(Device);

    size_t bufferSize = 0;
    PVOID buffer = MbbRequestGetBuffer(SendRequest, &bufferSize);

    // This client driver example uses asynchronous completion
    auto myDeviceSendCompletionRoutine = [](MBBREQUEST SendRequest, NTSTATUS NtStatus)
    {
        //Acknowledge back to MBBCx
        MbbRequestComplete(SendRequest, NtStatus);
    };

    // The client driver-specified function call into its device
    NTSTATUS sendStatus = MyDeviceAsyncSend(
        
        // The client driver-specific handle
        myContext->MyDeviceHandle,

        // The context for completion
        SendRequest,

        // MBIM message               
        buffer,

        // MBIM message size
        bufferSize,   

        // Can be used for logging purpose, for example              
        MbbRequestGetActivityId(SendRequest), 

        // The client driver-specific completion routine
        myDeviceSendCompletionRoutine);

    if (sendStatus != STATUS_PENDING)
    {
        // Acknowledge back to MBBCx
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
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
