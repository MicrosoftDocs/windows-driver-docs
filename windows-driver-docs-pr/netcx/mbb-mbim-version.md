---
title: MBB_MBIM_VERSION
description: The MBB_MBIM_VERSION enumeration defines the version of the MBIM specification that a client driver and its device support. 
ms.assetid: F952E104-83F2-4B07-AB5F-18C1C744B5E7
keywords:
- Mobile Broadband WDF Class Extension MBB_MBIM_VERSION, MBBCx MBB_MBIM_VERSION
ms.author: windowsdriverdev
ms.date: 03/26/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MBB_MBIM_VERSION

[!include[MBBCx Beta Prerelease](../mbbcx-beta-prerelease.md)]

The **MBB_MBIM_VERSION** enumeration defines the version of the MBIM specification that a client driver and its device support. 

## Syntax

```C++
typdedef enum _MBB_MBIM_VERSION {
    MBB_MBIM_VERSION1_0 = 0,
    MBB_MBIM_VERSION1_0_ERRATA,
} MBB_MBIM_VERSION;
```

## Constants

|   |   |
| --- | --- |
| MBB_MBIM_VERSION1_0 | The client driver and device support the MBIM specification Rev 1.0. |
| MBB_MBIM_VERSION1_0_ERRATA | The client driver and device support the MBIM specification Rev 1.0 Errata-1. |

## Remarks

Client drivers set the MBIM specification version they support in the **Version** member of the [**MBB_DEVICE_MBIM_PARAMETERS**](mbb-device-mbim-parameters.md) structure. Currently, client drivers must set the value of this field to **MBB_MBIM_VERSION1_0_ERRATA**.

## Requirements

|     |     |
| --- | --- |
| Minimum KMDF version | 1.27 |
| Minimum NetAdapterCx version | 1.3 |
| Header | Mbbcx.h |