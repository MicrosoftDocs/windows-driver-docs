---
title: OID_WDI_IHV_REQUEST (dot11wificxintf.h)
ms.topic: reference
description: The OID_WDI_IHV_REQUEST command is used to forward information that an IHV extensibility module has sent to the miniport.
ms.date: 07/31/2021
keywords:
 - OID_WDI_IHV_REQUEST Network Drivers Starting with Windows Vista
---

# OID\_WDI\_IHV\_REQUEST (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

OID\_WDI\_IHV\_REQUEST is used to forward information that an IHV extensibility module has sent to the miniport.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command is not serialized with any tasks. It is serialized with other properties and with the M1-M3 of a task.

## Command parameter


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                        |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The information from the IHV extensibility module. |

 

## Response result


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                 |
|------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The response to be sent to the IHV extensibility module. The data value is forwarded as-is to the IHV extensibility module. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


 

