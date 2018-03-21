---
title: MbbDeviceSendServiceSessionDataComplete
description: 
ms.assetid: 83004F03-95AC-4B70-AE9B-1DA1956281C5
keywords:
- Mobile Broadband WDF Class Extension MbbDeviceSendServiceSessionDataComplete, MBBCx MbbDeviceSendServiceSessionDataComplete
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbDeviceSendServiceSessionDataComplete

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
VOID
MbbDeviceSendServiceSessionDataComplete(
    _In_ WDFMEMORY Data,
    _In_ NTSTATUS NtStatus
);
```

## Parameters

*Data* [in]  


*NtStatus* [in]  


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