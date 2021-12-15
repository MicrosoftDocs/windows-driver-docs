---
title: KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX
description: AVStream clients use the KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX property to determine framing requirements for a pin.
keywords: ["KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX

AVStream clients use the **KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX** property to determine framing requirements for a pin.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSALLOCATOR_FRAMING_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex) |

## Remarks

This property returns a [**KSALLOCATOR_FRAMING_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex), which describes the framing requirements for an AVStream pin.

Minidrivers running under stream class should use [**KSPROPERTY_CONNECTION_ALLOCATORFRAMING**](ksproperty-connection-allocatorframing.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSALLOCATOR_FRAMING_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing_ex)

[KS Allocators](ks-allocators.md)

[AVStream Allocators](avstream-allocators.md)
