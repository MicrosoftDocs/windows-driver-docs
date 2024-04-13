---
title: KSPROPERTY_BDA_SYMBOL_RATE
description: Clients use KSPROPERTY_BDA_SYMBOL_RATE to control the symbol rate of a demodulator node.
keywords: ["KSPROPERTY_BDA_SYMBOL_RATE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_SYMBOL_RATE
api_type:
- NA
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SYMBOL_RATE

Clients use **KSPROPERTY_BDA_SYMBOL_RATE** to control the symbol rate of a demodulator node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The returned value specifies the symbol rate.

The **NodeId** member of **KSP_NODE** specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
