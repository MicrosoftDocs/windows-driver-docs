---
title: WDI_TLV_CANCEL_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_CANCEL_PARAMETERS is a WiFiCx TLV that contains parameters for OID_WDI_ABORT_TASK.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CANCEL_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CANCEL\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CANCEL\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_ABORT\_TASK](./oid-wdi-abort-task.md).

## TLV Type


0x2B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                   | Description                                             |
|------------------------|---------------------------------------------------------|
| NDIS\_OID              | Specifies the OID from the original task being aborted. |
| UINT32                 | Specifies the transaction ID from the original task.    |
| WDI\_PORT\_ID (UINT16) | Specifies the port ID from the original task.           |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

