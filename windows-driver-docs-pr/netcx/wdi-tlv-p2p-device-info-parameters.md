---
title: WDI_TLV_P2P_DEVICE_INFO_PARAMETERS (dot11wificxtypes.h)
description: WDI_TLV_P2P_DEVICE_INFO_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Direct device information parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_INFO_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS (dot11wificxtypes.h)


WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS is a TLV that contains Wi-Fi Direct device information parameters.

## TLV Type


0x86

## Length


The sum (in bytes) of the sizes of all contained elements. 

**Note**  WDI\_P2P\_DEVICE\_TYPE is not a WiFiCx structure. It is defined in the WiFiCx TLV parser generator, and is used for documentation purposes only.

## Values


| Type       | Description                                            |
|------------|--------------------------------------------------------|
| UINT8\[6\] | The Wi-Fi Direct Device Address of the peer.           |
| UINT16     | The configuration methods supported by the device.     |
| WDI\_P2P\_DEVICE\_TYPE\[\] | The primary device type for this device. |


WDI\_P2P\_DEVICE\_TYPE consists of the following elements.

| Type       | Description                                   |
|------------|-----------------------------------------------|
| UINT16     | Primary device type: Main type category identifier.    |
| UINT8\[4\] | Primary device type: OUI assigned to this device type. |
| UINT16     | Primary device type: Subcategory type identifier.      |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




