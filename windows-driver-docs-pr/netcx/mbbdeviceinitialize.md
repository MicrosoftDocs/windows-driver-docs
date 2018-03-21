---
title: MbbDeviceInitialize
description: 
ms.assetid: C5319566-7A3D-475F-A38C-9EAC9C40495A
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceInitialize, MBBCx MbbDeviceInitialize
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceInitialize

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
NTSTATUS
MbbDeviceInitialize(
    _In_ WDFDEVICE Device,
    _In_ PMBB_DEVICE_CONFIG Config
);
```

## Parameters

*Device* [in]  


*Config* [in]  


## Return value


## Remarks


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | PASSIVE_LEVEL |