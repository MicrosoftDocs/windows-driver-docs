---
title: KSEVENT\_CLOCK\_INTERVAL\_MARK
description: Clients enable the KSEVENT\_CLOCK\_INTERVAL\_MARK event to be notified when an initial time value is reached, and then at fixed time increments after that.
keywords: ["KSEVENT_CLOCK_INTERVAL_MARK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CLOCK_INTERVAL_MARK
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_CLOCK\_INTERVAL\_MARK


Clients enable the KSEVENT\_CLOCK\_INTERVAL\_MARK event to be notified when an initial time value is reached, and then at fixed time increments after that.

## <span id="ddk_ksevent_clock_interval_mark_ks"></span><span id="DDK_KSEVENT_CLOCK_INTERVAL_MARK_KS"></span>


### <span id="event_data"></span><span id="EVENT_DATA"></span>Event Data

Use a structure of type [**KSEVENT\_TIME\_INTERVAL**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_time_interval) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol) to register for this event.

## Remarks

For information about how to register for events, see [KS Events](./ks-events.md).

 

