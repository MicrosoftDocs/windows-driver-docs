---
title: KSEVENT_CLOCK_INTERVAL_MARK
description: Clients enable the KSEVENT_CLOCK_INTERVAL_MARK event to be notified when an initial time value is reached, and then at fixed time increments after that.
keywords: ["KSEVENT_CLOCK_INTERVAL_MARK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CLOCK_INTERVAL_MARK
api_type:
- NA
ms.date: 10/11/2021
ms.localizationpriority: medium
---

# KSEVENT_CLOCK_INTERVAL_MARK

Clients enable the **KSEVENT_CLOCK_INTERVAL_MARK** event to be notified when an initial time value is reached, and then at fixed time increments after that.

## Event Data

Use a structure of type [**KSEVENT_TIME_INTERVAL**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_time_interval) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol) to register for this event.

## Remarks

For information about how to register for events, see [KS Events](./ks-events.md).
