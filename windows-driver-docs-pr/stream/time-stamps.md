---
title: Time Stamps
description: Time Stamps
ms.assetid: a97a57df-294a-4cbb-85d3-56d33ece65c9
keywords:
- video capture WDK AVStream , time stamps
- capturing video WDK AVStream , time stamps
- time stamps WDK video capture
- clocks WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Time Stamps


Minidrivers should time stamp data packets to synchronize multiple data streams. Kernel-mode clocks begin counting time when they first transition out of the **KSSTATE\_STOP** state. Thereafter, clocks should increment time stamps in regular intervals of 100 nanosecond units until the stream transitions to the **KSSTATE\_STOP** state.

Each data packet that is transferred corresponds to a single frame or field of video or ancillary data. Video capture driver writers that are concerned with frame-accurate video capture can choose to provide a clock that all other filters can use as a reference. Digital video minidrivers are an example of minidrivers that should provide clocks to use in a filter graph. Alternatively, video capture minidrivers that run asynchronously to other multimedia streams, such as USB and IEEE 1394 conferencing cameras, should time stamp their data packets with a clock provided by another component, such as an audio digitizer.

If a Stream class minidriver provides master clock, it should specify the following values in the [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) structure:

```cpp
PHW_STREAM_OBJECT *pStreamObject;
 
PStreamObject->HWClockFunction = (PHW_CLOCK_FUNCTION)StreamClockRoutine;
PStreamObject->ClockSupportFlags = CLOCK_SUPPORT_CAN_READ_ONBOARD_CLOCK | CLOCK_SUPPORT_CAN_RETURN_STREAM_TIME;
```

 

 




