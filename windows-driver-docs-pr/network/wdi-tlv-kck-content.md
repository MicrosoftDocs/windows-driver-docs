---
title: WDI_TLV_KCK_CONTENT
description: WDI_TLV_KCK_CONTENT is a TLV that contains an IEEE 802.11 key confirmation key (KCK).
ms.date: 05/07/2021
keywords:
 - WDI_TLV_KCK_CONTENT Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_KCK\_CONTENT

WDI\_TLV\_KCK\_CONTENT is a TLV that contains an IEEE 802.11 key confirmation key (KCK).

## TLV Type

0x168

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies an IEEE 802.11 key confirmation key (KCK). |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.pp |
