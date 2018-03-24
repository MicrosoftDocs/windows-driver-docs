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

This structure describes pointers to a client driver's MBB specific callback functions. The client driver must supply an initialized **MBB_DEVICE_CONFIG** structure as an input parameter to [**MbbDeviceInitialize**](mbbdeviceinitialize.md)

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
Size of the **MBB_DEVICE_CONFIG** structure

**SendMbimFragment**
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_SEND_MBIM_FRAGMENT*](evt-mbb-device-send-mbim-framgment.md) callback function.

**ReceiveMbimFragment**  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_RECEIVE_MBIM_FRAGMENT*](evt-mbb-device-receive-mbim-framgment.md) callback function.

**SendDeviceServiceSessionData**  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_SEND_SERVICE_SESSION_DATA*](evt-mbb-device-send-service-session-data.md) callback function.

**CreateAdapter**  
A pointer to the client driver's implementation of [*EVT_MBB_DEVICE_CREATE_ADAPTER*](evt-mbb-device-create-adapter.md) callback function.

## Remarks

Call [**MBB_DEVICE_CONFIG_INIT**](mbb-device-config-init.md) to intialize this structure.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |