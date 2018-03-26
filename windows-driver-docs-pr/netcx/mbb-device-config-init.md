---
title: MBB_DEVICE_MBIM_CONFIG_INIT
description: 
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

Initializes the [**MBB_DEVICE_CONFIG**](mbb-device-config.md) structure.

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
A pointer to the client driver allocated MBB_DEVICE_CONFIG structure.

*SendMbimFragment* [in]  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT*](evt-mbb-device-send-mbim-framgment.md) callback function.

*ReceiveMbimFragment* [in]  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT*](evt-mbb-device-receive-mbim-framgment.md) callback function.

*SendDeviceServiceSessionData* [in]  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA*](evt-mbb-device-send-service-session-data.md) callback function.

*CreateAdapter* [in]  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_CREATE_ADAPTER*](evt-mbb-device-create-adapter.md) callback function.

## Return value
None

## Remarks
The client driver calls this method from its EVT_WDF_DRIVER_DEVICE_ADD event callback function in preparation of calling **MbbDeviceInitilize**.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |