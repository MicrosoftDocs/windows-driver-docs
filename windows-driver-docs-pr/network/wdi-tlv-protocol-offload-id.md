---
title: WDI_TLV_PROTOCOL_OFFLOAD_ID
ms.topic: reference
description: WDI_TLV_PROTOCOL_OFFLOAD_ID is a TLV that contains the protocol offload identifier.
ms.date: 05/07/2021
keywords:
 - WDI_TLV_PROTOCOL_OFFLOAD_ID Network Drivers Starting with Windows 10, Version 2004
---

# WDI\_TLV\_PROTOCOL\_OFFLOAD\_ID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

WDI\_TLV\_PROTOCOL\_OFFLOAD\_ID is a TLV that contains the protocol offload identifier.

## TLV Type

0x166

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies the the protocol offload identifier. |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
