---
title: KSPROPERTY_CONNECTION_ALLOCATORFRAMING
description: In the stream class model, clients use the KSPROPERTY_CONNECTION_ALLOCATORFRAMING property to determine framing requirements for a pin.
keywords: ["KSPROPERTY_CONNECTION_ALLOCATORFRAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ALLOCATORFRAMING
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CONNECTION_ALLOCATORFRAMING

In the stream class model, clients use the KSPROPERTY_CONNECTION_ALLOCATORFRAMING property to determine framing requirements for a pin.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSALLOCATOR_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing) |

## Remarks

This property returns a [**KSALLOCATOR_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing), which describes the framing requirements for the pin. For example, the **FrameSize** member specifies the frame size of data on the pin.

AVStream minidrivers should use [**KSPROPERTY_CONNECTION_ALLOCATORFRAMING_EX**](ksproperty-connection-allocatorframing-ex.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSALLOCATOR_FRAMING**](/windows-hardware/drivers/ddi/ks/ns-ks-ksallocator_framing)

[KS Allocators](ks-allocators.md)

[AVStream Allocators](avstream-allocators.md)
