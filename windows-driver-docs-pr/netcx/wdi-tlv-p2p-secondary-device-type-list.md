---
title: WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST is a WiFiCx TLV that contains a list of secondary device types.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_SECONDARY_DEVICE_TYPE_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST is a TLV that contains a list of secondary device types.

## TLV Type


0x94

## Length


The size (in bytes) of the array of WDI\_P2P\_DEVICE\_TYPE elements. An array length of 0 is allowed.

**Note**  WDI\_P2P\_DEVICE\_TYPE is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                       | Description                            |
|----------------------------|----------------------------------------|
| WDI\_P2P\_DEVICE\_TYPE\[\] | An array of Wi-Fi Direct device types. |

 

WDI\_P2P\_DEVICE\_TYPE consists of the following elements.

| Type       | Description                                   |
|------------|-----------------------------------------------|
| UINT16     | The main type category ID.                    |
| UINT8\[4\] | The OUI that is assigned to this device type. |
| UINT16     | The subcategory ID.                           |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




