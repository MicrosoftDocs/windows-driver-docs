---
title: OID_WDI_SET_OWE_DH_IE (dot11wificxintf.h)
ms.topic: reference
description: The WDI_SET_OWE_DH_IE command sets the Diffie-Hellman Extension IE blob parameters.
ms.date: 08/23/2023
---

# WDI_SET_OWE_DH_IE (dot11wificxintf.h)

OID_WDI_SET_OWE_DH_IE sets the Diffie-Hellman Extension IE blob parameters that must be included in the association request sent by the station when auth type is OWE.

## Command parameters

| TLV | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_TLV_OWE_DH_IE](wdi-tlv-owe-dh-ie.md) |  |  | The Owe DH IE parameters to be set. |


## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
