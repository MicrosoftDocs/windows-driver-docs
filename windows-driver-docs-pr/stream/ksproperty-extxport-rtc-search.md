---
title: KSPROPERTY_EXTXPORT_RTC_SEARCH
description: The KSPROPERTY_EXTXPORT_RTC_SEARCH property searches to a relative time counter (RTC) on a tape.
keywords: ["KSPROPERTY_EXTXPORT_RTC_SEARCH Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTXPORT_RTC_SEARCH
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTXPORT_RTC_SEARCH

The **KSPROPERTY_EXTXPORT_RTC_SEARCH** property searches to a relative time counter (RTC) on a tape.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | DWORD |

The property value (operation data) is a DWORD that specifies the timecode, in hour:minute:second:frame, to search to on a tape.

## Remarks

The **dwTimecode** member of the **KSPROPERTY_EXTXPORT_S** structure specifies the relative time counter setting to search to.

This method is defined, but not supported.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
