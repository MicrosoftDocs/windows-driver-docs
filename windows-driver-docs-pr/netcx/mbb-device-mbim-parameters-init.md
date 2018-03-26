---
title: MBB_DEVICE_MBIM_PARAMETERS_INIT
description: 
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

Initializes the [**MBB_DEVICE_MBIM_PARAMETERS**](mbb-device-mbim-parameters.md) structure.

## Syntax

```C++
VOID
MBB_DEVICE_MBIM_PARAMETERS_INIT(
    _Out_ PMBB_DEVICE_MBIM_PARAMETERS MbimParameters,
    _In_ USHORT Version,
    _In_ ULONG MaximumFragmentSize
);
```

## Parameters

*MbimParameters* [out]  
A pointer to the client driver allocated MBB_DEVICE_MBIM_PARAMETERS structure.

*Version* [in]  
The version of MBIM specification that the client driver supports. The value of this field must be *MBB_MBIM_VERSION1_0_ERRATA*.

*MaximumFragmentSize* [in]  
The maximum size of the MBIM control message the client driver can support.

## Return value
None

## Remarks
The client driver typically calls this method from its EVT_WDF_DEVICE_PREPARE_HARDWARE event callback function in preparation of calling **MbbDeviceSetMbimParameters**.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |