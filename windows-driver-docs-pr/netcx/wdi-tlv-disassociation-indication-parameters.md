---
title: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS is a WiFiCx TLV that contains disassociation indication parameters for NDIS_STATUS_WDI_INDICATION_DISASSOCIATION.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS is a TLV that contains disassociation indication parameters for [NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](./ndis-status-wdi-indication-disassociation.md).

## TLV Type


0xBC

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                         | Description                                                                |
|--------------------------------------------------------------|----------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)            | The MAC address of the peer associated with the disassociation indication. |
| [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_assoc_status) (UINT32) | The trigger for the disassociation indication.                             |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

