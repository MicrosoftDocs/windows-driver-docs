---
title: WDI_TLV_ETHERTYPE_ENCAP_TABLE (dot11wificxtypes.h)
description: WDI_TLV_ETHERTYPE_ENCAP_TABLE is a WiFiCx TLV that contains the Ethertype encapsulations for the association.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ETHERTYPE_ENCAP_TABLE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE (dot11wificxtypes.h)


WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE is a TLV that contains the Ethertype encapsulations for the association.

## TLV Type


0x31

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                                       | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ns-dot11wificxtypes-wdi_ethertype_encapsulation_entry)\[\] | An array of [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ns-dot11wificxtypes-wdi_ethertype_encapsulation_entry) elements that specifies the Ethertype encapsulations for the association. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

