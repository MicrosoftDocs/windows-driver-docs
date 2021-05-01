---
title: WDI_TLV_REPLAY_COUNTER
description: WDI_TLV_REPLAY_COUNTER is a TLV that contains .
ms.assetid: 
ms.date: 04/30/2021
keywords:
 - WDI_TLV_REPLAY_COUNTER Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_REPLAY\_COUNTER

WDI\_TLV\_REPLAY\_COUNTER is a TLV that contains GCMP 256 cipher algorithm key data.

## TLV Type

0x164

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies GCMP 256 cipher algorithm key data. |

## Requirements

|     |     |
| --- | --- |
| **Minimum supported client** | Windows 10, Version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
