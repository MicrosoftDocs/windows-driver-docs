---
title: Time Stamps
author: windows-driver-content
description: Time Stamps
ms.assetid: a97a57df-294a-4cbb-85d3-56d33ece65c9
keywords:
- video capture WDK AVStream , time stamps
- capturing video WDK AVStream , time stamps
- time stamps WDK video capture
- clocks WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Time Stamps


Minidrivers should time stamp data packets to synchronize multiple data streams. Kernel-mode clocks begin counting time when they first transition out of the **KSSTATE\_STOP** state. Thereafter, clocks should increment time stamps in regular intervals of 100 nanosecond units until the stream transitions to the **KSSTATE\_STOP** state.

Each data packet that is transferred corresponds to a single frame or field of video or ancillary data. Video capture driver writers that are concerned with frame-accurate video capture can choose to provide a clock that all other filters can use as a reference. Digital video minidrivers are an example of minidrivers that should provide clocks to use in a filter graph. Alternatively, video capture minidrivers that run asynchronously to other multimedia streams, such as USB and IEEE 1394 conferencing cameras, should time stamp their data packets with a clock provided by another component, such as an audio digitizer.

If a Stream class minidriver provides master clock, it should specify the following values in the [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) structure:

```
PHW_STREAM_OBJECT *pStreamObject;
 
PStreamObject->HWClockFunction = (PHW_CLOCK_FUNCTION)StreamClockRoutine;
PStreamObject->ClockSupportFlags = CLOCK_SUPPORT_CAN_READ_ONBOARD_CLOCK | CLOCK_SUPPORT_CAN_RETURN_STREAM_TIME;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Time%20Stamps%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


