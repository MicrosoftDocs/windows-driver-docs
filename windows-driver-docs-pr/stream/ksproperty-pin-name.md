---
title: KSPROPERTY_PIN_NAME
description: The client uses KSPROPERTY_PIN_NAME to retrieve the Registry name of a pin factory. This is a localized Unicode string.
keywords: ["KSPROPERTY_PIN_NAME Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_NAME
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_NAME

The client uses **KSPROPERTY_PIN_NAME** to retrieve the Registry name of a pin factory. This is a localized Unicode string.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | A buffer containing the localized Unicode string. |

## Remarks

Specify this property using **KSP_PIN**, where the member specifies the pin factory for which to return the registry name.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)
