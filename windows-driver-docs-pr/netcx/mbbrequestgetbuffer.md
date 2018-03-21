---
title: MbbRequestGetBuffer
description: 
ms.assetid: 527D4C3E-0A56-43B5-A0B9-3EDC66F0A4A0
keywords:
- Mobile Broadband WDF Class Extension MbbRequestGetBuffer, MBBCx MbbRequestGetBuffer
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MbbRequestGetBuffer

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
PVOID
MbbRequestGetBuffer(
    _In_ MBBREQUEST Fragment,
    _Out_opt_ size_t* BufferSize
);
```

## Parameters

*Fragment* [in]  


*BufferSize* [out, opt]  


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