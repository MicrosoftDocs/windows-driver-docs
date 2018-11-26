---
title: Master Clock
description: Master Clock
ms.assetid: 87a99371-9c72-4310-bcc7-02af19207b3e
keywords:
- DVD decoder minidrivers WDK , master clock
- decoder minidrivers WDK DVD , master clock
- master clocks WDK DVD decoder
- clocks WDK DVD decoder
- onboard clock WDK DVD decoder
- current stream time WDK DVD decoder
- time WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Master Clock





The DVD decoder minidriver may indicate that a given stream is capable of providing master clock information. This indicates that the stream is the one to which all others should synchronize. Only two members of the SRB structure are needed.

The *HwClockFunction* member is set to a pointer to the DVD decoder minidriver routine that processes calls for clock information. The routine is set when the SRB\_OPEN\_STREAM call for the master clock stream is received. This indicates that a stream is capable of being a master clock for the system.

The *ClockSupportFlags* member of the [**HW\_CLOCK\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559671) structure is set to one of the following values:

<a href="" id="clock-support-can-set-onboard-clock"></a>CLOCK\_SUPPORT\_CAN\_SET\_ONBOARD\_CLOCK  
Indicates the device can change the onboard clock time to any arbitrary value.

<a href="" id="clock-support-can-read-onboard-clock"></a>CLOCK\_SUPPORT\_CAN\_READ\_ONBOARD\_CLOCK  
Indicates the current clock time can be read for this stream from the hardware. This clock does not have to correlate to the current stream time, it just indicates the ability of the driver to return the value in 100ns units of the onboard clock.

<a href="" id="clock-support-can-return-stream-time"></a>CLOCK\_SUPPORT\_CAN\_RETURN\_STREAM\_TIME  
Indicates this stream can return the current stream time being processed in the hardware.

For more information, see [Master Clocks](master-clocks.md).

 

 




