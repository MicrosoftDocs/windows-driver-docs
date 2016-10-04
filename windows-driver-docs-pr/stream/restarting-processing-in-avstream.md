---
title: Restarting Processing in AVStream
author: windows-driver-content
description: Restarting Processing in AVStream
MS-HAID:
- 'avsover\_8e88a507-318c-4b0f-ae4a-8851d932ced5.xml'
- 'stream.restarting\_processing\_in\_avstream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f60d4dbd-61e6-4ae2-aa43-9edc8f36c3ff
keywords: ["restarting AVStream processing", "AVStream process restarting WDK", "resume processing WDK AVStream", "pending status WDK AVStream"]
---

# Restarting Processing in AVStream


## <a href="" id="ddk-restarting-processing-in-avstream-ksg"></a>


AVStream stops processing if any of the following conditions are true:

-   In a pin-centric environment, no data is currently available on the pin.

-   In a filter-centric environment, at least one pin for which the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure does not set KSPIN\_FLAG\_FRAMES\_NOT\_REQUIRED\_FOR\_PROCESSING, does not have data waiting to be processed. By default, this flag is not set.

-   The minidriver's processing dispatch callback routine returns STATUS\_PENDING, regardless of frame availability. Note that the processing dispatch can be either [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) or [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351), depending on whether the minidriver implements [pin-centric processing](pin-centric-processing.md) or [filter-centric processing](filter-centric-processing.md).

AVStream initiates processing when new data arrives into a previously empty queue. Therefore, if the minidriver's processing dispatch returns STATUS\_PENDING when the associated queues are full, the minidriver will never be called on to resume processing. If the minidriver sets STATUS\_PENDING, the minidriver must call [**KsPinAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff563494) or [**KsFilterAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff562527) to resume processing.

Do not return STATUS\_SUCCESS from the processing dispatch if the minidriver does not actually process data. This causes AVStream to immediately call the minidriver again, resulting in an infinite loop between AVStream and the processing dispatch.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Restarting%20Processing%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


