---
title: KSPROPERTY_BDA_NODE_PROPERTIES
description: Clients use KSPROPERTY_BDA_NODE_PROPERTIES to retrieve a list of properties supported on a node.
keywords: ["KSPROPERTY_BDA_NODE_PROPERTIES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_PROPERTIES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_NODE_PROPERTIES

Clients use **KSPROPERTY_BDA_NODE_PROPERTIES** to retrieve a list of properties supported on a node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | List of GUIDs |

## Remarks

The list of properties supported by a node is a list of GUIDs.

The network provider will use this property to query the capabilities of each node in the BDA template connection list.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyNodeProperties**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertynodeproperties)

[**KSPROPERTY**](ksproperty-structure.md)
