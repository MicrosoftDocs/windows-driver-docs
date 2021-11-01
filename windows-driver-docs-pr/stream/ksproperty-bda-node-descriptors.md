---
title: KSPROPERTY_BDA_NODE_DESCRIPTORS
description: Clients use KSPROPERTY_BDA_NODE_DESCRIPTORS to retrieve a list of nodes.
keywords: ["KSPROPERTY_BDA_NODE_DESCRIPTORS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_NODE_DESCRIPTORS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_NODE_DESCRIPTORS

Clients use **KSPROPERTY_BDA_NODE_DESCRIPTORS** to retrieve a list of nodes.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | List of GUIDs |

## Remarks

The list of nodes is an array of GUIDs for available nodes.

For a list of BDA nodes that are available to create in a template topology, see [BDA Node Category GUIDs](bda-node-category-guids.md).

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyNodeDescriptors**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertynodedescriptors)

[**KSPROPERTY**](ksproperty-structure.md)
