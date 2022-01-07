---
title: KSPROPERTY_PIN_MEDIUMS
description: This property returns the list of mediums supported by pins instantiated by a specific pin factory.
keywords: ["KSPROPERTY_PIN_MEDIUMS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_MEDIUMS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_MEDIUMS

This property returns the list of mediums supported by pins instantiated by a specific pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | A [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, followed by a sequence of [**KSPIN_MEDIUM**](kspin-medium-structure.md) structures. |

## Remarks

Clients use this property to request a list of all mediums supported by pins instantiated by the pin factory. Clients then specify the actual medium to use when they connect to the pin.

Specify this property using **KSP_PIN**, where the member specifies the pin factory for which to return the list of mediums.

**KSPROPERTY_PIN_MEDIUMS** returns mediums ordered by class driver preference.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSPIN_MEDIUM**](kspin-medium-structure.md)
