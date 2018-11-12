---
title: KSEVENT\_CLOCK\_POSITION\_MARK
description: A KSEVENT\_CLOCK\_POSITION\_MARK event occurs when a certain time on a clock is reached.
ms.assetid: 489e7441-41e9-40e5-8bf5-0bff2fda9f27
keywords: ["KSEVENT_CLOCK_POSITION_MARK Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_CLOCK_POSITION_MARK
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_CLOCK\_POSITION\_MARK


A KSEVENT\_CLOCK\_POSITION\_MARK event occurs when a certain time on a clock is reached.

### <span id="event_data"></span><span id="EVENT_DATA"></span>Event Data

Use a structure of type [**KSEVENT\_TIME\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561891) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) to register for this event.

Remarks
-------

For information about how to register for events, see [KS Events](https://msdn.microsoft.com/library/windows/hardware/ff567643).

 

 





