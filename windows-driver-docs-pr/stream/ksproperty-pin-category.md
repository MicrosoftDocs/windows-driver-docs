---
title: KSPROPERTY_PIN_CATEGORY
description: The client uses the KSPROPERTY_PIN_CATEGORY property to retrieve the category of a pin factory.
keywords: ["KSPROPERTY_PIN_CATEGORY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_CATEGORY
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_CATEGORY

The client uses the **KSPROPERTY_PIN_CATEGORY** property to retrieve the category of a pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | GUID |

## Remarks

The **PinId** member of the KSP_PIN structure specifies the pin factory for which to return the category GUID.

The KS filter uses this property to indicate the standard functional *Category* of pins instantiated by the pin factory.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information where necessary.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)
