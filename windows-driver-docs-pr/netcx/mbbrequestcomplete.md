---
title: MbbRequestComplete
description: 
ms.assetid: 7BD76E70-4F63-4F76-A8B9-B7FACBE0936C
keywords:
- Mobile Broadband WDF Class Extension MbbRequestComplete, MBBCx MbbRequestComplete
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestComplete

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
VOID
MbbRequestComplete(
    _In_ MBBREQUEST Fragment,
    _In_ NTSTATUS NtStatus
);
```

## Parameters

*Fragment* [in]  


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
| IRQL | <= DISPATCH_LEVEL |