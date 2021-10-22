---
title: KSPROPERTY_BDA_TEMPLATE_CONNECTIONS
description: Clients use KSPROPERTY_BDA_TEMPLATE_CONNECTIONS to retrieve a list of connections between pins and nodes in a template topology.
keywords: ["KSPROPERTY_BDA_TEMPLATE_CONNECTIONS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_TEMPLATE_CONNECTIONS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_TEMPLATE_CONNECTIONS

Clients use **KSPROPERTY_BDA_TEMPLATE_CONNECTIONS** to retrieve a list of connections between pins and nodes in a template topology.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](ksproperty-structure.md) | [**BDA_TEMPLATE_CONNECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_template_connection) |

## Remarks

The returned **BDA_TEMPLATE_CONNECTION** structure describes a connection in a template topology.

The list of connections between pins and nodes in a template topology is an array of **BDA_TEMPLATE_CONNECTION** structures.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyTemplateConnections**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertytemplateconnections)

[**BDA_TEMPLATE_CONNECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_template_connection)

[**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex)

[**KSPROPERTY**](ksproperty-structure.md)
