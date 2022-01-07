---
title: KSPROPERTY_NUM_SOURCES
description: The KSPROPERTY_NUM_SOURCES property specifies the number of input pins on the selector unit.
keywords: ["KSPROPERTY_NUM_SOURCES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_NUM_SOURCES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_NUM_SOURCES

The **KSPROPERTY_NUM_SOURCES** property specifies the number of input pins on the selector unit.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter or node | [**KSPROPERTY_SELECTOR_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_selector_s) or [**KSPROPERTY_SELECTOR_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_selector_node_s) | LONG |

## Remarks

When making a get request, the client receives the number of available source pins in the **Value** member of the property descriptor structure.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_SELECTOR_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_selector_s)

[**KSPROPERTY_SELECTOR_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_selector_node_s)
