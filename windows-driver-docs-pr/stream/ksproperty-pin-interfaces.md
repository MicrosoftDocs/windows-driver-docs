---
title: KSPROPERTY_PIN_INTERFACES
description: This property returns the list of interfaces supported by pins instantiated by a specific pin factory.
keywords: ["KSPROPERTY_PIN_INTERFACES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_INTERFACES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_INTERFACES

This property returns the list of interfaces supported by pins instantiated by a specific pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | A [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, followed by a sequence of [**KSPIN_INTERFACE**](kspin-interface-structure.md) structures. |

## Remarks

Specify **KSPROPERTY_PIN_INTERFACES** using **KSP_PIN**, where the **PinId** member specifies the pin factory for which to return available interfaces.

This property returns the interfaces ordered by class driver preference.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSPIN_INTERFACE**](kspin-interface-structure.md)
