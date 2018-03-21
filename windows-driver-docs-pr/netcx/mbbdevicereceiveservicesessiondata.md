---
title: MbbDeviceReceiveServiceSessionData
description: 
ms.assetid: 609629F4-20F9-4942-89C9-9C47A87992A6
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceReceiveServiceSessionData, MBBCx MbbDeviceReceiveServiceSessionData
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceReceiveServiceSessionData

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
VOID
MbbDeviceReceiveServiceSessionData(
    _In_ WDFDEVICE Device,
    _In_ DSS_SESSION_ID SessionId,
    _In_ WDFMEMORY Data
);
```

## Parameters

*Device* [in]  


*SessionId* [in]  


*Data* [in]  


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