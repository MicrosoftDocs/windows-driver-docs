---
title: KSEVENT\_CLOCK\_INTERVAL\_MARK
description: Clients enable the KSEVENT\_CLOCK\_INTERVAL\_MARK event to be notified when an initial time value is reached, and then at fixed time increments after that.
ms.assetid: 5292606e-d0b3-4e64-a236-c1cecf3fd53a
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

Use a structure of type [**KSEVENT\_TIME\_INTERVAL**](https://msdn.microsoft.com/library/windows/hardware/ff561887) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) to register for this event.

Remarks
-------

For information about how to register for events, see [KS Events](https://msdn.microsoft.com/library/windows/hardware/ff567643).

 

 





