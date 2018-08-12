---
title: MbbDeviceSetMbimParameters
description: The client driver calls the MbbDeviceSetMbimParameters method to report its MBIM-specification related parameters.
ms.assetid: 6F794479-BDF1-466B-8472-80D6DA942D84
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceSetMbimParameters, MBBCx MbbDeviceSetMbimParameters
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MbbDeviceSetMbimParameters

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The client driver calls the **MbbDeviceSetMbimParameters** method to report its MBIM-specification related parameters.

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
A handle to a framework device object the client driver obtained from a previous call to [WdfDeviceCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate).

*MbimParameters* [in]  
A pointer to a client driver-allocated and initialized [**MBB_DEVICE_MBIM_PARAMETERs**](mbb-device-mbim-parameters.md).

## Return value

This method does not return a value.

## Remarks

The client driver typically calls this method from within [*EVT_DEVICE_PREPARE_HARDWARE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware). 

For more information, see [**Initialize the device**](writing-an-mbbcx-client-driver.md#initialize-the-device).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |
