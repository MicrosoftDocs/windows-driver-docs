---
title: KS_AM_RATE_SimpleRateChange
description: The KS_AM_RATE_SimpleDataRate property sets the time stamp rate on a filter.
keywords: ["KS_AM_RATE_SimpleRateChange Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KS_AM_RATE_SimpleRateChange
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/11/2021
---

# KS_AM_RATE_SimpleRateChange

The **KS_AM_RATE_SimpleDataRate** property sets the time stamp rate on a filter.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KS_AM_SimpleRateChange**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ks_am_simpleratechange) |

The property value (operation data) is a **KS_AM_SimpleRateChange** structure that describes a simple rate change for an MPEG-2 stream, such as fast-forward or rewind.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KS_AM_SimpleRateChange**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ks_am_simpleratechange)
