---
title: MbbDeviceInitConfig
description: 
ms.assetid: 6BB95F5C-0EB2-4006-9C18-C82B4FA40032
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceInitConfig, MBBCx MbbDeviceInitConfig
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceInitConfig

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
NTSTATUS
MbbDeviceInitConfig(
    _Inout_ PWDFDEVICE_INIT DeviceInit
);
```

## Parameters

*DeviceInit* [in, out]  


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