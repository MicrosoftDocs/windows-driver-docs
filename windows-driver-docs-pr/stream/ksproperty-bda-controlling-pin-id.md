---
title: KSPROPERTY_BDA_CONTROLLING_PIN_ID
description: Clients use KSPROPERTY_BDA_CONTROLLING_PIN_ID to retrieve the controlling pin for a node in the BDA template connection list.
keywords: ["KSPROPERTY_BDA_CONTROLLING_PIN_ID Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_CONTROLLING_PIN_ID
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_CONTROLLING_PIN_ID

Clients use **KSPROPERTY_BDA_CONTROLLING_PIN_ID** to retrieve the controlling pin for a node in the BDA template connection list.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSP_BDA_NODE_PIN | ULONG |

## Remarks

The returned value specifies the controlling pin ID.

Nodes are associated with one pin in the filter, either an input pin or an output pin. Nodes can only be accessed through the controlling pin because nodes do not have their own file handle. The network provider can use this property and the KSP_BDA_NODE_PIN structure to query for the controlling pin for each node in the BDA template connection list (KSTOPOLOGY_CONNECTION or BDA_TEMPLATE_CONNECTION array).

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyGetControllingPinId**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertygetcontrollingpinid)

[**BDA_TEMPLATE_CONNECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_template_connection)

[**KSP_BDA_NODE_PIN**](/windows-hardware/drivers/ddi/bdamedia/ns-bdamedia-_ksp_bda_node_pin)

[**KSTOPOLOGY_CONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kstopology_connection)
