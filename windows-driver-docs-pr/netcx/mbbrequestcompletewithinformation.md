---
title: MbbRequestCompleteWithInformation
description: 
ms.assetid: 72AA2E74-CECB-4E68-AA3D-E8DDFEE3A40F
keywords:
- Mobile Broadband WDF Class Extension MbbRequestCompleteWithInformation, MBBCx MbbRequestCompleteWithInformation
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestCompleteWithInformation

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
VOID
MbbRequestCompleteWithInformation(
    _In_ MBBREQUEST Fragment,
    _In_ NTSTATUS NtStatus,
    _In_ ULONG_PTR Information
);
```

## Parameters

*Fragment* [in]  


*NtStatus* [in]  


*Information* [in]  


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