---
title: EVT_MBB_DEVICE_CREATE_ADAPTER
description: 
ms.assetid: 42F04BBD-22B5-45B2-A158-FE52E07104CD
keywords:
- Mobile Broadband WDF Class Extension EVT_MBB_DEVICE_CREATE_ADAPTER, MBBCx EVT_MBB_DEVICE_CREATE_ADAPTER
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EVT_MBB_DEVICE_CREATE_ADAPTER

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
EVT_MBB_DEVICE_CREATE_ADAPTER EvtMbbDeviceCreateAdapter;

NTSTATUS
EvtMbbDeviceCreateAdapter(
    _In_ WDFDEVICE Device,
    _In_ PNETADAPTER_INIT AdapterInit
)
{ ... }

typedef EVT_MBB_DEVICE_CREATE_ADAPTER *PFN_MBB_DEVICE_CREATE_ADAPTER;
```

## Parameters

*Device* [in]  


*AdapterInit* [in]  


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