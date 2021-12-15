---
title: WDI_TLV_OPERATION_MODE (dot11wificxtypes.hpp)
description: WDI_TLV_OPERATION_MODE is a WiFiCx TLV that contains the desired operation mode.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_OPERATION_MODE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_OPERATION\_MODE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_OPERATION\_MODE is a TLV that contains the desired operation mode.

## TLV Type


0x95

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                        |
|--------|----------------------------------------------------------------------------------------------------|
| UINT32 | The desired operation mode, as defined in [**WDI\_OPERATION\_MODE**](/windows-hardware/drivers/ddi/dot11wificxintf/ne-dot11wificxintf-wdi_operation_mode). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

