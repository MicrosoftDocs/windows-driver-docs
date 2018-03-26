---
title: MBB_DEVICE_MBIM_PARAMETERS_INIT
description: The MBB_DEVICE_MBIM_PARAMETERS_INIT method initializes a MBB_DEVICE_MBIM_PARAMETERS structure.
ms.assetid: 511D61B2-9017-4800-805C-3F5ED3985293
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_MBIM_PARAMETERS_INIT, MBBCx MBB_DEVICE_MBIM_PARAMETERS_INIT
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_DEVICE_MBIM_PARAMETERS_INIT

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MBB_DEVICE_MBIM_PARAMETERS_INIT** method initializes a [**MBB_DEVICE_MBIM_PARAMETERS**](mbb-device-mbim-parameters.md) structure.

## Syntax

```C++
VOID
MBB_DEVICE_MBIM_PARAMETERS_INIT(
    _Out_ PMBB_DEVICE_MBIM_PARAMETERS MbimParameters,
    _In_ MBB_MBIM_VERSION Version,
    _In_ ULONG MaximumFragmentSize
);
```

## Parameters

*MbimParameters* [out]  
A pointer to the client driver-allocated [**MBB_DEVICE_MBIM_PARAMETERS**](mbb-device-mbim-parameters.md) structure.

*Version* [in]  
An [**MBB_MBIM_VERSION**](mbb-mbim-version.md) value that defines the version of the MBIM specification that the client driver supports. The value of this field must be **MBB_MBIM_VERSION1_0_ERRATA**.

*MaximumFragmentSize* [in]  
The maximum size, in bytes, of MBIM control messages that the client driver can support.

## Return value

This method does not return a value.

## Remarks

The client driver typically calls this method from its [*EVT_WDF_DEVICE_PREPARE_HARDWARE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) event callback function in preparation for calling [**MbbDeviceSetMbimParameters**](mbbdevicesetmbimparameters.md).

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |