---
title: KSPROPERTY_PIN_GLOBALCINSTANCES
description: The client uses the KSPROPERTY_PIN_GLOBALCINSTANCES to determine the current number of pins instantiated by a pin factory, as well as the maximum number of pins this pin factory can instantiate. This property is optional.
keywords: ["KSPROPERTY_PIN_GLOBALCINSTANCES Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_GLOBALCINSTANCES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_GLOBALCINSTANCES

The client uses the **KSPROPERTY_PIN_GLOBALCINSTANCES** to determine the current number of pins instantiated by a pin factory, as well as the maximum number of pins this pin factory can instantiate. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | KSPIN_CINSTANCES |

## Remarks

Specify this property using KSP_PIN, where the **PinId** member specifies the pin factory.

**KSPIN_CINSTANCES** is a data structure of the form:

```cpp
typedef struct {
    ULONG PossibleCount;
    ULONG CurrentCount;
} KSPIN_CINSTANCES;
```

The following is a description of each member of the **KSPIN_CINSTANCES** structure.

**PossibleCount**  
Specifies the maximum number of pin the pin factory can instantiate on the driver, or **KSINTANCE_INDETERMINATE** if there is no maximum.

**CurrentCount**  
Specifies the current number of pins the pin factory has instantiated on the driver.

The class driver does not handle this property; the stream minidriver must provide handling on its own.

**KSPROPERTY_PIN_GLOBALCINSTANCES** specifies the absolute current and maximum number of instances, over all instances of the filter. To determine per-filter values, use [**KSPROPERTY_PIN_CINSTANCES**](ksproperty-pin-cinstances.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSPROPERTY_PIN_CINSTANCES**](ksproperty-pin-cinstances.md)
