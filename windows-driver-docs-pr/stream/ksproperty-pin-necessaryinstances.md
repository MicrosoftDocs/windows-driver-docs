---
title: KSPROPERTY_PIN_NECESSARYINSTANCES
description: This property returns the minimum number of pins that the pin factory must instantiate before the filter can perform I/O operations.
keywords: ["KSPROPERTY_PIN_NECESSARYINSTANCES Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_NECESSARYINSTANCES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_NECESSARYINSTANCES

This property returns the minimum number of pins that the pin factory must instantiate before the filter can perform I/O operations.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | ULONG |

## Remarks

Specify this property using **KSP_PIN**, where the member specifies the relevant pin factory.

**KSPROPERTY_PIN_NECESSARYINSTANCES** returns a value of type ULONG, specifying the minimum number of pins that the pin factory must instantiate.

The class driver does not handle this property; the stream minidriver must provide handling on its own.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)
