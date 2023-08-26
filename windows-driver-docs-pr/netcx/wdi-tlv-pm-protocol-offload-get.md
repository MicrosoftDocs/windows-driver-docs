---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_GET (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_GET is a WiFiCx TLV that contains a protocol offload ID for OID_WDI_GET_PM_PROTOCOL_OFFLOAD.
ms.date: 08/25/2023
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_GET (dot11wificxtypes.hpp)


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_GET is a TLV that contains a protocol offload ID for [OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md).

## TLV Type


0xA8

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

