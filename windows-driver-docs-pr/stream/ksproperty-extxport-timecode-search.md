---
title: KSPROPERTY_EXTXPORT_TIMECODE_SEARCH
description: The KSPROPERTY_EXTXPORT_TIMECODE_SEARCH property searches to a specific timecode.
keywords: ["KSPROPERTY_EXTXPORT_TIMECODE_SEARCH Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTXPORT_TIMECODE_SEARCH
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTXPORT_TIMECODE_SEARCH

The **KSPROPERTY_EXTXPORT_TIMECODE_SEARCH** property searches to a specific timecode.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | Embedded **TIMECODE** structure |

The property value (operation data) is an embedded **TIMECODE** structure member of the **KSPROPERTY_EXTXPORT_S** structure that describes the specific timecode to search to, including frame, second, minute and hour.

## Remarks

This method is defined, but not supported.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
