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
---

# KSEVENT\_CLOCK\_POSITION\_MARK


A KSEVENT\_CLOCK\_POSITION\_MARK event occurs when a certain time on a clock is reached.

### <span id="event_data"></span><span id="EVENT_DATA"></span>Event Data

Use a structure of type [**KSEVENT\_TIME\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561891) as the *OutBuffer* parameter when calling [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) to register for this event.

Remarks
-------

For information about how to register for events, see [KS Events](https://msdn.microsoft.com/library/windows/hardware/ff567643).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENT_CLOCK_POSITION_MARK%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




