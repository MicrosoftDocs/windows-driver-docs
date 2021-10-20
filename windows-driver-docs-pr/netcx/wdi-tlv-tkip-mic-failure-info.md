---
title: WDI_TLV_TKIP_MIC_FAILURE_INFO (dot11wificxtypes.hpp)
description: WDI_TLV_TKIP_MIC_FAILURE_INFO is a WiFiCx TLV that contains TKIP-MIC failure information.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_TKIP_MIC_FAILURE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO is a TLV that contains TKIP-MIC failure information.

## TLV Type


0x57

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Specifies which cipher key type detected that the TKIP-MIC failure occurred. If this value is 1, the TKIP-MIC failure was detected through a default cipher key. If this value is 0, the TKIP-MIC failure was detected through a key mapping cipher key. |
| UINT32                                            | Specifies the index of the cipher key in the default key array. Valid value range is from 0 through 3.                                                                                                                                                   |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Specifies the MAC address of the peer that transmitted the packet that failed MIC verification.                                                                                                                                                          |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

