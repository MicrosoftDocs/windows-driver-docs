---
title: KSPROPERTY_BDA_TABLE_SECTION
description: Clients use KSPROPERTY_BDA_TABLE_SECTION to inform nodes about the table section to use when delivering data on the node's output.
keywords: ["KSPROPERTY_BDA_TABLE_SECTION Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_TABLE_SECTION
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_TABLE_SECTION

Clients use **KSPROPERTY_BDA_TABLE_SECTION** to inform nodes about the table section to use when delivering data on the node's output.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**BDA_TABLE_SECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_table_section) |

## Remarks

The **NodeId** member of KSP_NODE specifies the LNB amplifier node.

The **BDA_TABLE_SECTION** structure describes the table section.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BDA_TABLE_SECTION**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_table_section)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
