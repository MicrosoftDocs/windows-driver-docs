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



## Syntax

```C++
EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT EvtMbbDeviceSendMbimFragment;

VOID
EvtMbbDeviceSendMbimFragment(
    _In_ WDFDEVICE Device,
    _In_ MBBREQUEST Fragment
)
{ ... }

typedef EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT *PFN_MBB_DEVICE_SEND_MBIM_FRAGMENT;
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