---
title: KSPROPERTY_BDA_PIN_ID
description: Clients use KSPROPERTY_BDA_PIN_ID to retrieve the BDA identifier (ID) for a pin.
keywords: ["KSPROPERTY_BDA_PIN_ID Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_PIN_ID
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_PIN_ID

Clients use **KSPROPERTY_BDA_PIN_ID** to retrieve the BDA identifier (ID) for a pin.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](ksproperty-structure.md) | ULONG |

## Remarks

The returned value specifies the pin ID.

When the network provider creates a pin for a filter using [**KSMETHOD_BDA_CREATE_PIN_FACTORY**](ksmethod-bda-create-pin-factory.md), the BDA minidriver for the filter gives that pin an ID. **KSPROPERTY_BDA_PIN_ID** returns this ID.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSMETHOD_BDA_CREATE_PIN_FACTORY**](ksmethod-bda-create-pin-factory.md)

[**KSPROPERTY**](ksproperty-structure.md)
