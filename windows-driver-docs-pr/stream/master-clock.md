---
title: Master Clock
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Master Clock


## <a href="" id="ddk-master-clock-ksg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Master%20Clock%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


