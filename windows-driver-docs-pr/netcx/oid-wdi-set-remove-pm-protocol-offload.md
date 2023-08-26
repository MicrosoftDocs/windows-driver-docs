---
title: OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD (dot11wificxintf.h)
ms.topic: reference
description: The OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD OID removes the protocol offload specified by the protocol offload ID.
ms.date: 08/25/2023
---

# OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD (dot11wificxintf.h)


OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD removes the protocol offload specified by the protocol offload ID.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description          |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_REMOVE**](./wdi-tlv-pm-protocol-offload-remove.md) |                                |          | Protocol offload ID. |

 

## Set property results


No additional parameters. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md)

[OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-add-pm-protocol-offload.md)

 

