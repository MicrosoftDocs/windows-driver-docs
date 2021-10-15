---
title: KSEVENT_CLOCK_POSITION_MARK
description: A KSEVENT_CLOCK_POSITION_MARK event occurs when a certain time on a clock is reached.
keywords: ["KSEVENT_CLOCK_POSITION_MARK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CLOCK_POSITION_MARK
api_type:
- NA
ms.date: 10/11/2021
ms.localizationpriority: medium
---

# KSEVENT_CLOCK_POSITION_MARK

A **KSEVENT_CLOCK_POSITION_MARK** event occurs when a certain time on a clock is reached.

## Event Data

Use a structure of type [**KSEVENT_TIME_MARK**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_time_mark) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol) to register for this event.

## Remarks

For information about how to register for events, see [KS Events](./ks-events.md).
