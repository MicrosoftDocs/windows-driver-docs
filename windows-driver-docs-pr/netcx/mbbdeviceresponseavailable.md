---
title: MbbDeviceResponseAvailable
description: 
ms.assetid: A8BECE96-3845-4A9D-BA36-50A2666E52E1
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceResponseAvailable, MBBCx MbbDeviceResponseAvailable
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceResponseAvailable

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
VOID
MbbDeviceResponseAvailable(
    _In_ WDFDEVICE Device
);
```

## Parameters

*Device* [in]  


## Return value


## Remarks


## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |
| IRQL | <= DISPATCH_LEVEL |