---
title: MBB_DEVICE_MBIM_PARAMETERS
description: 
ms.assetid: 90DDEB14-17EB-4B6A-B88E-257AAB2586DC
keywords:
- Mobile Broadband WDF Class Extension MBB_DEVICE_MBIM_PARAMETERS, MBBCx MBB_DEVICE_MBIM_PARAMETERS
ms.author: windowsdriverdev
ms.date: 03/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_DEVICE_MBIM_PARAMETERS

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]



## Syntax

```C++
typedef struct _MBB_DEVICE_MBIM_PARAMETERS
{
    ULONG Size;

    USHORT Version;
    ULONG MaximumFragmentSize;
} MBB_DEVICE_MBIM_PARAMETERS, *PMBB_DEVICE_MBIM_PARAMETERS;
```

## Members

**Size**  

**Version**  

**MaximumFragmentSize**  

## Remarks


## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.25 |
| Minimum NetAdapterCx version | 1.2 |
| Header | Mbbcx.h |