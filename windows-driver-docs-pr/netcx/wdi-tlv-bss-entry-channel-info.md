---
title: WDI_TLV_BSS_ENTRY_CHANNEL_INFO (dot11wificxtypes.h)
description: WDI_TLV_BSS_ENTRY_CHANNEL_INFO is a WiFiCx TLV that contains BSS entry channel information.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_BSS_ENTRY_CHANNEL_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO (dot11wificxtypes.h)


WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO is a TLV that contains BSS entry channel information.

## TLV Type


0x3A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                          | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| WDI\_CHANNEL\_NUMBER (UINT32) | The logical channel number on which the peer was discovered. |
| UINT32                        | The band ID for the BSS entry.                               |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




