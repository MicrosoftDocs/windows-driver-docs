---
title: WDI_TLV_KEK_CONTENT
description: WDI_TLV_KEK_CONTENT is a TLV that contains .
ms.assetid: 
ms.date: 04/30/2021
keywords:
 - WDI_TLV_KEK_CONTENT Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_KEK\_CONTENT

WDI\_TLV\_KEK\_CONTENT is a TLV that contains cipher algorithm key data.

## TLV Type

0x169

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies KEK content cipher algorithm key data. |

## Requirements

|     |     |
| --- | --- |
| **Minimum supported client** | Windows 10, Version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
