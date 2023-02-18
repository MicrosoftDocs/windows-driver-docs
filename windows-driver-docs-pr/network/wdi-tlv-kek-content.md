---
title: WDI_TLV_KEK_CONTENT
ms.topic: reference
description: WDI_TLV_KEK_CONTENT is a TLV that contains an IEEE 802.11 key encryption key (KEK).
ms.date: 05/07/2021
keywords:
 - WDI_TLV_KEK_CONTENT Network Drivers Starting with Windows 10, Version 2004
---

# WDI\_TLV\_KEK\_CONTENT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

WDI\_TLV\_KEK\_CONTENT is a TLV that contains an IEEE 802.11 key encryption key (KEK).

## TLV Type

0x169

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies an IEEE 802.11 key encryption key (KEK). |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
