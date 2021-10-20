---
title: WDI_TLV_DOT11_RESET_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_DOT11_RESET_PARAMETERS is a WiFiCx TLV that contains parameters for OID_WDI_TASK_DOT11_RESET.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DOT11_RESET_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DOT11\_RESET\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_DOT11\_RESET\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_DOT11\_RESET](./oid-wdi-task-dot11-reset.md).

## TLV Type


0xA2

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------|
| UINT8 | If (and only if) this is set to 1, all MIB attributes for the port being reset are set to their default values. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

