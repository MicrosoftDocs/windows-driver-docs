---
title: KSPROPERTY_PIN_CTYPES
description: Clients use the KSPROPERTY_PIN_CTYPES property to determine how many pin types a KS filter supports.
keywords: ["KSPROPERTY_PIN_CTYPES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_CTYPES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
ms.localizationpriority: medium
---

# KSPROPERTY_PIN_CTYPES

Clients use the **KSPROPERTY_PIN_CTYPES** property to determine how many pin types a KS filter supports.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | ULONG |

## Remarks

**KSPROPERTY_PIN_CTYPES** returns a value of type ULONG, specifying the number of pin factories the KS filter supports.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)
