---
title: WDI_TLV_BSS_ENTRY_AGE_INFO (dot11wificxtypes.h)
description: WDI_TLV_BSS_ENTRY_AGE_INFO is a WiFiCx TLV that contains age information for a BSS entry.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_BSS_ENTRY_AGE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_AGE\_INFO (dot11wificxtypes.h)


WDI\_TLV\_BSS\_ENTRY\_AGE\_INFO is a TLV that contains age information for a BSS entry.

## TLV Type


0xBA

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|UINT64|Timestamp of when this BSS entry was most recently discovered. The timestamp should be obtained with [**NdisGetCurrentSystemTime**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetcurrentsystemtime) or [**KeQuerySystemTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime).|
|UINT8|Specifies whether this information is live (found during a currently running scan) or is coming from the IHV component's BSS list cache. Valid values are 0 (live) or 1 (cached).|


 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN10_NEXT|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|
