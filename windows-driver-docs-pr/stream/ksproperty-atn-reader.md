---
title: KSPROPERTY_ATN_READER
description: The KSPROPERTY_ATN_READER property retrieves the absolute track number (ATN) of the current tape position.
keywords: ["KSPROPERTY_ATN_READER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ATN_READER
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_ATN_READER

The KSPROPERTY_ATN_READER property retrieves the absolute track number (ATN) of the current tape position.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Device | [**KSPROPERTY_TIMECODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_timecode_s) | [**TIMECODE_SAMPLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagtimecode_sample) |

The property value (operation data) is a TIMECODE_SAMPLE structure that specifies the absolute track number of the current tape position.

## Remarks

The **TimecodeSamp** member of the KSPROPERTY_TIMECODE_S structure describes the absolute track number of the current tape position.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_TIMECODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_timecode_s)

[**TIMECODE_SAMPLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagtimecode_sample)
