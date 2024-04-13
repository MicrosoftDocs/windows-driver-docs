---
title: KSPROPERTY_DROPPEDFRAMES_CURRENT
description: The KSPROPERTY_DROPPED_FRAMES_CURRENT property dynamically retrieves the video capture minidriver for the number of frames captured, the number of frames dropped, and the average frame size. This property must be implemented.
keywords: ["KSPROPERTY_DROPPEDFRAMES_CURRENT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DROPPEDFRAMES_CURRENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DROPPEDFRAMES_CURRENT

The **KSPROPERTY_DROPPED_FRAMES_CURRENT** property dynamically retrieves the video capture minidriver for the number of frames captured, the number of frames dropped, and the average frame size. This property must be implemented.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSPROPERTY_DROPPEDFRAMES_CURRENT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s) | [**KSPROPERTY_DROPPEDFRAMES_CURRENT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s) |

The property value (operation data) is a **KSPROPERTY_DROPPEDFRAMES_CURRENT_S** structure that specifies the current picture number, the count of dropped frames, and the average size of the frames captured.

## Remarks

The counts of frames captured and frames dropped should reset when the stream state transitions from stop to pause.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_DROPPEDFRAMES_CURRENT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s)
