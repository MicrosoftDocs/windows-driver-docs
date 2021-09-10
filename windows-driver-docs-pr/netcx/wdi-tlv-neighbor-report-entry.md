---
title: WDI_TLV_NEIGHBOR_REPORT_ENTRY (dot11wificxtypes.hpp)
description: WDI_TLV_NEIGHBOR_REPORT_ENTRY is a WiFiCx TLV that contains a neighbor report.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_NEIGHBOR_REPORT_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY (dot11wificxtypes.hpp)


WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY is a TLV that contains a neighbor report.

## TLV Type


0x123

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                          | Multiple TLV instances allowed | Optional | Description                                                         |
|---------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                      |                                |          | The BSSID of the AP in the neighbor report.                         |
| [**WDI\_TLV\_BSSID\_INFO**](wdi-tlv-bssid-info.md)           |                                |          | The BSSID information of the AP.                                    |
| [**WDI\_TLV\_OPERATING\_CLASS**](wdi-tlv-operating-class.md) |                                |          | The operating class of the AP indicated by this BSSID.              |
| [**WDI\_TLV\_CHANNEL\_NUMBER**](wdi-tlv-channel-number.md)   |                                |          | The last known operating channel of the AP indicated by this BSSID. |
| [**WDI\_TLV\_PHY\_TYPE**](wdi-tlv-phy-type.md)               |                                |          | The PHY type of the AP indicated by this BSSID.                     |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




