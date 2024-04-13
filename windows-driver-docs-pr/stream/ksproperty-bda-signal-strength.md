---
title: KSPROPERTY_BDA_SIGNAL_STRENGTH
description: Clients use KSPROPERTY_BDA_SIGNAL_STRENGTH to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).
keywords: ["KSPROPERTY_BDA_SIGNAL_STRENGTH Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_SIGNAL_STRENGTH
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SIGNAL_STRENGTH

Clients use **KSPROPERTY_BDA_SIGNAL_STRENGTH** to determine the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin or Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | LONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value specifies the carrier strength of the signal in mDb.

A strength of 0 is nominal strength as expected for the given type of broadcast network. Subnominal strengths are reported as positive mDb. Super-nominal strengths are reported as negative mDb.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
