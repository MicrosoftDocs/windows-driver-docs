---
title: MbbDeviceInitialize
description: 
ms.assetid: DDB50DBD-B52D-4212-99CC-167E2014B29E
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
    _In_ NETADAPTER Adapter
);
```

## Parameters

*Adapter* [in]  


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