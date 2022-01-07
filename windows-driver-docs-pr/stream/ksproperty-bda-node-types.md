---
title: KSPROPERTY_BDA_NODE_TYPES
description: Clients use KSPROPERTY_BDA_NODE_TYPES to retrieve a list of node types.
keywords: ["KSPROPERTY_BDA_NODE_TYPES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_TYPES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_NODE_TYPES

Clients use **KSPROPERTY_BDA_NODE_TYPES** to retrieve a list of node types.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | List of KSNODE_DESCRIPTORs |

## Remarks

In a template topology each node type can only occur once, but it can occur multiple times in an actual topology. This list of node types is an array of **KSNODE_DESCRIPTOR** structures. Typically, the index of each element in this array is used to identify each particular node type.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyNodeTypes**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertynodetypes)

[**KSNODE_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksnode_descriptor)

[**KSPROPERTY**](ksproperty-structure.md)
