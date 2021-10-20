---
title: WDI_TLV_SCAN_MODE (dot11wificxtypes.hpp)
description: WDI_TLV_SCAN_MODE is a WiFiCx TLV that contains scan mode parameters.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_SCAN_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SCAN\_MODE (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_SCAN\_MODE is a TLV that contains scan mode parameters.

## TLV Type


0x6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                | Description                                                                                                                                                                                                                       |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                               | The number of times the full scan procedure should be repeated. If this value is set to 0, the scan should be repeated until the task is aborted by the host.                                                                     |
| [**WDI\_SCAN\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_scan_type)       | Specifies the type of scan that should be performed. If WDI\_SCAN\_TYPE\_ACTIVE is set, the device must only scan active channels.                                                                                                |
| UINT8                                               | Specifies if live updates are needed and discovered entries must be reported when they are found, with the recommended throttling logic above. This value is always true when the Microsoft component manages the BSS list cache. |
| [**WDI\_SCAN\_TRIGGER**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_scan_trigger) | Specifies the trigger for the scan.                                                                                                                                                                                               |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

