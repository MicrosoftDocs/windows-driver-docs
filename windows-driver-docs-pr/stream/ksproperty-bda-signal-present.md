---
title: KSPROPERTY_BDA_SIGNAL_PRESENT
description: Clients use KSPROPERTY_BDA_SIGNAL_PRESENT to determine whether a signal carrier is present.
keywords: ["KSPROPERTY_BDA_SIGNAL_PRESENT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_PRESENT
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_SIGNAL_PRESENT

Clients use **KSPROPERTY_BDA_SIGNAL_PRESENT** to determine whether a signal carrier is present.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin or Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | BOOL |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value indicates whether a signal carrier is present. Returns **TRUE** if a signal carrier is present and **FALSE** otherwise. The RF tuner node should provide this indication.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
