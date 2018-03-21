---
title: MBB_DEVICE_CONFIG
description: 
ms.assetid: 92AE903-9D6D-45C3-A9B3-1C03DB0ABEED
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_CONFIG, MBBCx MBB_DEVICE_CONFIG
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_DEVICE_CONFIG

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
typedef struct _MBB_DEVICE_CONFIG
{
    ULONG Size;

    PFN_MBB_DEVICE_SEND_MBIM_FRAGMENT SendMbimFragment;
    PFN_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT ReceiveMbimFragment;
    PFN_MBB_DEVICE_SEND_SERVICE_SESSION_DATA SendDeviceServiceSessionData;
    PFN_MBB_DEVICE_CREATE_ADAPTER CreateAdapter;
} MBB_DEVICE_CONFIG, *PMBB_DEVICE_CONFIG;
```

## Members

**Size**  

**ReceiveMbimFragment**  

**SendDeviceServiceSessionData**  

**CreateAdapter**  

## Remarks


## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |