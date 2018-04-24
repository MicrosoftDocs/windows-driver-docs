---
title: MBB_DEVICE_MBIM_CONFIG_INIT
description: The MBB_DEVICE_CONFIG_INIT method initializes the MBB_DEVICE_CONFIG structure.
ms.assetid: 6561CA32-6AF7-4436-87BD-9BB449AD4F58
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_CONFIG_INIT, MBBCx MBB_DEVICE_CONFIG_INIT
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_DEVICE_CONFIG_INIT

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MBB_DEVICE_CONFIG_INIT** method initializes the [**MBB_DEVICE_CONFIG**](mbb-device-config.md) structure.

## Syntax

```C++
VOID
MBB_DEVICE_CONFIG_INIT(
    _Out_ PMBB_DEVICE_CONFIG Config,
    _In_ PFN_MBB_DEVICE_SEND_MBIM_FRAGMENT SendMbimFragment,
    _In_ PFN_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT ReceiveMbimFragment,
    _In_ PFN_MBB_DEVICE_SEND_SERVICE_SESSION_DATA SendDeviceServiceSessionData,
    _In_ PFN_MBB_DEVICE_CREATE_ADAPTER CreateAdapter
);
```

## Parameters

*Config* [out]  
A pointer to the client driver-allocated [**MBB_DEVICE_CONFIG**](mbb-device-config.md) structure.

*SendMbimFragment* [in]  
A pointer to the client driver's implementation of the [*EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT*](evt-mbb-device-send-mbim-fragment.md) callback function.

*ReceiveMbimFragment* [in]  
A pointer to the client driver's implementation of the [*EVT_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT*](evt-mbb-device-receive-mbim-fragment.md) callback function.

*SendDeviceServiceSessionData* [in]  
A pointer to the client driver's implementation of the [*EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA*](evt-mbb-device-send-service-session-data.md) callback function.

*CreateAdapter* [in]  
A pointer to the client driver's implementation of the [*EVT_MBB_DEVICE_CREATE_ADAPTER*](evt-mbb-device-create-adapter.md) callback function.

## Return value

This method does not return a value.

## Remarks

The client driver calls this method from its [*EVT_WDF_DRIVER_DEVICE_ADD*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) event callback function in preparation for calling [**MbbDeviceInitialize**](mbbdeviceinitialize.md).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |