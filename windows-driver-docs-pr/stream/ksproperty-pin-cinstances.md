---
title: KSPROPERTY_PIN_CINSTANCES
description: The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.
keywords: ["KSPROPERTY_PIN_CINSTANCES Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_CINSTANCES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
---

# KSPROPERTY_PIN_CINSTANCES

The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | **KSPIN_CINSTANCES** |

## Remarks

This property returns a structure of type **KSPIN_CINSTANCES**:

```cpp
typedef struct {
    ULONG PossibleCount;
    ULONG CurrentCount;
} KSPIN_CINSTANCES;
```

The following is a description of each member of the KSPIN_CINSTANCES structure.

**PossibleCount**  
Specifies the maximum number of pins the pin factory can instantiate on the filter, or **KSINTANCE_INDETERMINATE** if there is no maximum.

**CurrentCount**  
Specifies the current number of pins the pin factory has instantiated on the filter.

This property specifies the per-filter maximum for a given pin factory. Use the [**KSPROPERTY_PIN_GLOBALCINSTANCES**](ksproperty-pin-globalcinstances.md) property to specify the overall maximum for a given pin factory.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSPROPERTY_PIN_GLOBALCINSTANCES**](ksproperty-pin-globalcinstances.md)
