---
title: KSPROPERTY_BDA_PIN_TYPE
description: Clients use KSPROPERTY_BDA_PIN_TYPE to retrieve the value that specifies the type of a pin.
keywords: ["KSPROPERTY_BDA_PIN_TYPE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_PIN_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_PIN_TYPE

Clients use **KSPROPERTY_BDA_PIN_TYPE** to retrieve the value that specifies the type of a pin.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](ksproperty-structure.md) | ULONG |

## Remarks

The returned value specifies the pin type.

When the network provider creates a pin for a filter using [**KSMETHOD_BDA_CREATE_PIN_FACTORY**](ksmethod-bda-create-pin-factory.md), it specifies a pin type from the list of pin types included in the filter's BDA template topology. **KSPROPERTY_BDA_PIN_TYPE** returns this pin type. In the filter's BDA template topology each pin type can only occur once, but it can occur multiple times in an actual topology. The value for the pin type corresponds to the index of the element in the zero-based array of pin types. This array of pin types is an array of [**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structures.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSMETHOD_BDA_CREATE_PIN_FACTORY**](ksmethod-bda-create-pin-factory.md)

[**KSPIN_DESCRIPTOR_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex)

[**KSPROPERTY**](ksproperty-structure.md)
