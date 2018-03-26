---
title: MbbDeviceSetMbimParameters
description: 
ms.assetid: 6F794479-BDF1-466B-8472-80D6DA942D84
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceSetMbimParameters, MBBCx MbbDeviceSetMbimParameters
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceSetMbimParameters

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver calls this method to report its MBIM specification related parameters.

## Syntax

```C++
VOID
MbbDeviceSetMbimParameters(
    _In_ WDFDEVICE Device,
    _In_ PMBB_DEVICE_MBIM_PARAMETERS MbimParameters
);
```

## Parameters

*Device* [in]  
A handle to a framework device object.

*MbimParameters* [in]  
A pointer to a client driver initialized [**MBB_DEVICE_MBIM_PARAMETERs**](mbb-device-mbim-parameters.md).

## Return value
None

## Remarks
The client driver typically calls this method from within EVT_DEVICE_PREPARE_HARDWARE. For more information, see [**Initialize the device**](writing-an-mbbcx-client-driver.md#initialize-the-device).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |