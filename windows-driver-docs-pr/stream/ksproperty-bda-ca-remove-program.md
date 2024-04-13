---
title: KSPROPERTY_BDA_CA_REMOVE_PROGRAM
description: Clients use KSPROPERTY_BDA_CA_REMOVE_PROGRAM to prevent access to a specific program.
keywords: ["KSPROPERTY_BDA_CA_REMOVE_PROGRAM Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_CA_REMOVE_PROGRAM
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_CA_REMOVE_PROGRAM

Clients use **KSPROPERTY_BDA_CA_REMOVE_PROGRAM** to prevent access to a specific program.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ULONG |

## Remarks

The property value specifies the program to make inaccessible.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED**](ksevent-bda-program-flow-status-changed.md)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
