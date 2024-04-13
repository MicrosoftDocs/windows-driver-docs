---
title: KSPROPERTY_BDA_NODE_METHODS
description: Clients use KSPROPERTY_BDA_NODE_METHODS to retrieve a list of methods supported on a node.
keywords: ["KSPROPERTY_BDA_NODE_METHODS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_NODE_METHODS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_NODE_METHODS

Clients use **KSPROPERTY_BDA_NODE_METHODS** to retrieve a list of methods supported on a node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | List of GUIDs |

## Remarks

The list of methods supported by a node is a list of GUIDs.

The network provider will use this property to query the capabilities of each node in the BDA template connection list.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyNodeMethods**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertynodemethods)

[**KSPROPERTY**](ksproperty-structure.md)
