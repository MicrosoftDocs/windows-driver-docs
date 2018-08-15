---
title: EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA
description: A client driver's EvtMbbDeviceSendServiceSessionData event callback function sends device service session data down to its modem device.
ms.assetid: 216FAF8C-B5F2-4979-8016-BFCE178F5B3A
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA, MBBCx EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

A client driver's *EvtMbbDeviceSendServiceSessionData* event callback function sends device service session data down to its modem device.

## Syntax

```C++
EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA EvtMbbDeviceSendServiceSessionData;

NTSTATUS
EvtMbbDeviceSendServiceSessionData(
    _In_ WDFDEVICE Device,
    _In_ DSS_SESSION_ID SessionId,
    _In_ WDFMEMORY Data
)
{ ... }

typedef EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA *PFN_MBB_DEVICE_SEND_SERVICE_SESSION_DATA;
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*SessionId* [in]  
The ID of the device service session obtained from a previous call to [**MbbAdapterGetSessionId**](mbbadaptergetsessionid.md).

*Data* [in]  
A WDFMEMORY object containing the data to pass to the device.

## Return value

This callback function returns STATUS_SUCCESS if the operation was successful. Otherwise, it returns an appropriate NTSTATUS error code.

## Remarks

MBBCx invokes a client driver's *EvtMbbDeviceSendServiceSessionData* callback function when an application sends DSS data down to the modem device. After sending the data to the device asynchronously, the client driver must call [**MbbDeviceSendServiceSessionDataComplete**](mbbdevicesendservicesessiondatacomplete.md) so MBBCx can free the memory allocated for the data.

## Example

The following example shows how a client might send DSS data down to its modem device. Error handling has been left out of this example for brevity and clarity.

```C++
NTSTATUS
MyEvtMbbDeviceSendServiceSessionData(
    _In_ WDFDEVICE Device,
    _In_ DSS_SESSION_ID SessionId,
    _In_ WDFMEMORY Data
)
{
    NTSTATUS status = STATUS_SUCCESS;

    // Get the device context and NETADAPTER context
    PMY_DEVICE_CONTEXT deviceContext = GetMyDeviceContext(Device);

    // Set up a driver-defined DSS packet structure
    PMY_DSS_PACKET packet = NULL;

    // Get the data to send from the WDFMEMORY object
    size_t bufferSize = 0;
    PVOID buffer = WdfMemoryGetBuffer(Data, 
                                      &bufferSize);

    // Populate the DSS packet
    packet = MyAllocateDssPacket(Data,
                                buffer,
                                bufferSize,
                                SessionId);

    // Send the data asynchronously, which returns STATUS_PENDING when successful
    status = MyModemBusWriteData(deviceContext->BusHandle,
                                 packet);

    // Increment count of sent packets
    deviceContext->DSSPacketsSentCount++;

    // Clean up the memory
    MbbDeviceSendServiceSessionDataComplete(Data,
                                            status);
    MyCleanupDssPacket(packet);

    // Convert STATUS_PENDING to NDIS_STATUS_SUCCESS for this callback.
    // This is in a successful case and doesn't take into account other
    // normal error handling that has been left out of this example.
    status = NDIS_STATUS_SUCCESS;

    return status;
}
```

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
