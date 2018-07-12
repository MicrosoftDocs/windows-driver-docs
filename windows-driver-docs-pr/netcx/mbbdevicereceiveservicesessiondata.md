---
title: MbbDeviceReceiveServiceSessionData
description: Client drivers call the MbbDeviceReceiveServiceSessionData method to pass received device service session data up to an application through the MBBCx framework.
ms.assetid: 609629F4-20F9-4942-89C9-9C47A87992A6
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceReceiveServiceSessionData, MBBCx MbbDeviceReceiveServiceSessionData
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceReceiveServiceSessionData

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

Client drivers call the **MbbDeviceReceiveServiceSessionData** method to pass received device service session data up to an application through the MBBCx framework.

## Syntax

```C++
VOID
MbbDeviceReceiveServiceSessionData(
    _In_ WDFDEVICE Device,
    _In_ DSS_SESSION_ID SessionId,
    _In_ WDFMEMORY Data
);
```

## Parameters

*Device* [in]  
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*SessionId* [in]  
The ID of the device service session obtained from a previous call to [**MbbAdapterGetSessionId**](mbbadaptergetsessionid.md).

*Data* [in]  
A driver-allocated WDFMEMORY object containing the data to pass to the application.

## Return value

This method does not return a value.

## Remarks

For more information, see [Handling device service sessions](writing-an-mbbcx-client-driver.md#handling-device-service-sessions).

## Example

The following example shows how a client driver might pass received DSS data to the framework's DSS receive handler.

```C++
VOID
MyReceiveDssData(
    _In_ PMY_DEVICE_CONTEXT DeviceContext,
    _In_ ULONG SessionId,
    _In_ PUCHAR InBuffer,
    _In_ ULONG InBufferSize
)
{
    NTSTATUS status = STATUS_SUCCESS;
    WDFMEMORY data;

    // Allocate the WDFMEMORY object from the received data buffer
    status = WdfMemoryAllocatePreallocated(WDF_NO_OBJECT_ATTRIBUTES,
                                            InBuffer,
                                            InBufferSize,
                                            &data);

    // Pass the received data to the framework
    if(NT_SUCCESS(status))
    {
        DeviceContext->DSSPacketsReceivedCount++;

        MbbDeviceReceiveServiceSessionData(DeviceContext->WdfDevice,
                                            SessionId,
                                            data);
        WdfObjectDelete(data);
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