---
title: WDI_TLV_START_AP_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_START_AP_PARAMETERS is a WiFiCx TLV that contains the parameters for OID_WDI_TASK_START_AP.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_START_AP_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_START\_AP\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_START\_AP\_PARAMETERS is a TLV that contains the parameters for [OID\_WDI\_TASK\_START\_AP](./oid-wdi-task-start-ap.md).

## TLV Type


0xAB

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|UINT32|The beacon period. If non-zero, this parameter specifies the beacon interval.|
|UINT32|The DTIM period. If non-zero, this parameter specifies the number of beacon intervals between transmissions of beacon frames that contain a TIM element with a DTIM Count field that equals zero. This value is transmitted in the DTIM Period field of beacon frames.|
|UINT8|This parameter sets the dot11ExcludeUnencrypted MIB. Valid values are 0 and 1.|
|UINT8|This parameter specifies if the device supports 802.11b speeds. Valid values are 0 (not supported) and 1 (supported). When this value is set to 1, the access point should allow clients using 11b rates to connect to it.|
|UINT8|This parameter specifies whether to allow legacy SoftAP clients to connect. Valid values are 0 (not allowed) and 1 (allowed).|
|UINT8|MustUseSpecifiedChannels. This parameter specifies whether the AP can only be started on the channels specified in [OID_WDI_TASK_START_AP](./oid-wdi-task-start-ap.md) task parameters with [**WDI_TLV_AP_BAND_CHANNEL**](wdi-tlv-ap-band-channel.md). Valid values are 0 and 1. If it is set to 1, the AP can only be started from the specified list. If it is not set, the list is meant to be a recommendation of channels that the firmware can pick from, and it may pick another channel if it is not possible to start the AP on any of the specified channels.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|



