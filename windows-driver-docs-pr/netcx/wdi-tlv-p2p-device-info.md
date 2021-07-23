---
title: WDI_TLV_P2P_DEVICE_INFO (dot11wificxtypes.h)
description: WDI_TLV_P2P_DEVICE_INFO is a WiFiCx TLV that contains Wi-Fi Direct device information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_INFO (dot11wificxtypes.h)


WDI\_TLV\_P2P\_DEVICE\_INFO is a TLV that contains Wi-Fi Direct device information.

## TLV Type


0x96

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_INFO\_PARAMETERS**](wdi-tlv-p2p-device-info-parameters.md) |                                |          | The device information, including Wi-Fi Direct device address, supported configuration methods, and primary device type. |
| [**WDI\_TLV\_P2P\_DEVICE\_NAME**](wdi-tlv-p2p-device-name.md)                        |                                |          | The device name for this device.                                                                                         |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|


 

 




