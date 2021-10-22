---
title: KSPROPERTY_BDA_PIN_TYPES
description: Clients use KSPROPERTY_BDA_PIN_TYPES to retrieve a list of pin types.
keywords: ["KSPROPERTY_BDA_PIN_TYPES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIN_TYPES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_PIN_TYPES

Clients use **KSPROPERTY_BDA_PIN_TYPES** to retrieve a list of pin types.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](ksproperty-structure.md) | List of [**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structures |

## Remarks

In a template topology each pin type can only occur once, but it can occur multiple times in an actual topology. This list of pin types is an array of [**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structures.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BdaPropertyPinTypes**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertypintypes)

[**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex)

[**KSPROPERTY**](ksproperty-structure.md)
