---
title: EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA
description: 
ms.assetid: 216FAF8C-B5F2-4979-8016-BFCE178F5B3A
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA, MBBCx EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



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


*SessionId* [in]  


*Data* [in]  


## Return value


## Remarks


## Example


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |