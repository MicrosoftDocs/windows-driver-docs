---
title: Restarting Processing in AVStream
description: Restarting Processing in AVStream
ms.assetid: f60d4dbd-61e6-4ae2-aa43-9edc8f36c3ff
keywords:
- restarting AVStream processing
- AVStream process restarting WDK
- resume processing WDK AVStream
- pending status WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting Processing in AVStream





AVStream stops processing if any of the following conditions are true:

-   In a pin-centric environment, no data is currently available on the pin.

-   In a filter-centric environment, at least one pin for which the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure does not set KSPIN\_FLAG\_FRAMES\_NOT\_REQUIRED\_FOR\_PROCESSING, does not have data waiting to be processed. By default, this flag is not set.

-   The minidriver's processing dispatch callback routine returns STATUS\_PENDING, regardless of frame availability. Note that the processing dispatch can be either [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) or [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351), depending on whether the minidriver implements [pin-centric processing](pin-centric-processing.md) or [filter-centric processing](filter-centric-processing.md).

AVStream initiates processing when new data arrives into a previously empty queue. Therefore, if the minidriver's processing dispatch returns STATUS\_PENDING when the associated queues are full, the minidriver will never be called on to resume processing. If the minidriver sets STATUS\_PENDING, the minidriver must call [**KsPinAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff563494) or [**KsFilterAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff562527) to resume processing.

Do not return STATUS\_SUCCESS from the processing dispatch if the minidriver does not actually process data. This causes AVStream to immediately call the minidriver again, resulting in an infinite loop between AVStream and the processing dispatch.

 

 




