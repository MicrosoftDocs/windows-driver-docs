---
title: KSPROPERTY_STREAM_DEGRADATION
description: The KSPROPERTY_STREAM_DEGRADATION property is an optional property that should be implemented if the pin allows degradation strategies.
keywords: ["KSPROPERTY_STREAM_DEGRADATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_DEGRADATION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 07/13/2021
---

# KSPROPERTY_STREAM_DEGRADATION

The **KSPROPERTY_STREAM_DEGRADATION** property is an optional property that should be implemented if the pin allows degradation strategies.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](ksproperty-structure.md) | [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item), [**KSDEGRADE**](ksdegrade-structure.md) |

## Remarks

When queried, the property returns the size and count of the structures to be returned in [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) format, followed by [**KSDEGRADE**](ksdegrade-structure.md) structures.

On a query, this property returns the size and count of the structures to be returned in **KSMULTIPLE_ITEM** format, followed by **KSDEGRADE** structures. The multiple item format must be used on both querying and setting degradation strategies.

A client can query this property to retrieve the current degradation settings or it can set this property to change the current degradation settings. The degradation settings are used to modify the usage of resources by a filter pin in response to a quality management (QM) complaint, or to adjust quality back to some higher level. This is typically used by a quality manager to adjust degradation settings, and query the type of setting that can be adjusted and their current values. It may pass multiple **KSDEGRADE** structures when setting values. For more information about quality managers, see [Quality Management](quality-management.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSDEGRADE**](ksdegrade-structure.md)
