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



## Syntax

```C++
EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT EvtMbbDeviceReceiveMbimFragment;

VOID
EvtMbbDeviceReceiveMbimFragment(
    _In_ WDFDEVICE Device,
    _In_ MBBREQUEST Fragment
)
{ ... }

typedef EVT_MBIM_DEVICE_RECEIVE_MBIM_FRAGMENT *PFN_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT;
```

## Parameters

*Device* [in]  


*Fragment* [in]  


## Return value


## Remarks


## Example


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |