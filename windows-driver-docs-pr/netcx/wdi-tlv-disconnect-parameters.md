---
title: WDI_TLV_DISCONNECT_PARAMETERS (dot11wificxtypes.h)
description: WDI_TLV_DISCONNECT_PARAMETERS is a WiFiCx TLV that contains parameters for OID_WDI_TASK_DISCONNECT.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DISCONNECT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISCONNECT\_PARAMETERS (dot11wificxtypes.h)


WDI\_TLV\_DISCONNECT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_DISCONNECT](./oid-wdi-task-disconnect.md).

## TLV Type


0x36

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The MAC address of the peer to disassociate.                                                                                                                                        |
| UINT16                                            | The reason for the host-triggered disassociation. This value is provided in little endian byte order and should be appropriately copied into the reason code of the outgoing frame. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

